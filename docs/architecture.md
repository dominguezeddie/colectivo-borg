# Technical Architecture — Borg Collective

> *"Memory is never alienated — it remains on the user's local node.*  
> *Computing is socialized — the peer network resolves it.*  
> *The Borg is the identity. The Collective is the muscle."*

**Version:** v15 — June 2026 — Actively evolving document

---

## The Three Roles of the Mother Cell

Each node in the Collective assumes one or more roles according to its real physical capabilities. The same device can fulfill multiple roles simultaneously (e.g., a node with good RAM and CPU can be both Aggregator and Executor).

### The Executor ("The Muscle")

- Atomic computing unit
- Processes microtasks of 1 to 30 seconds
- State-agnostic architecture — no context maintained between tasks
- Ideal hardware: high CPU capacity
- Target: any PC with Python, even hardware from the last decade (2016-2020)
- Concrete example: transcribe 10 seconds of audio, classify an image, sum vectors

### The Aggregator ("The Synthesizer")

- Assembles partial results from multiple Executors
- Management of lagging nodes with instant failover
- Ideal hardware: high RAM, moderate CPU
- Critical function: if an Executor does not respond within <2 seconds, reassigns the microtask
- Concrete example: take 10 partial transcriptions and assemble a coherent text

### The Validator ("The Auditor")

- Governance and trust engine
- Verifies data integrity through partial re-execution
- Its reports feed the Contribution Score
- Ideal hardware: can be a high-latency node — works in the background
- Never blocks main execution; operates asynchronously

---

## Communication Protocol

The Borg uses a plain-text, lightweight, human-readable protocol designed to run over TCP/IP without needing HTTP or other heavy abstraction layers.

### General Format

| Field | Description | Example |
|-------|-------------|---------|
| version | Protocol version (current: 1) | `1` |
| type | Message type | `MICROTASK`, `ACK`, `ERROR` |
| task_id | Unique identifier of the microtask | `uuid-1234-5678` |
| payload | Payload (usually JSON) | `{"text":"Hello"}` |

### Responses

| Type | Format | Usage |
|------|--------|-------|
| OK | `BORG-ACK\|{"status":"ok","result":...}` | Microtask completed successfully |
| ERROR | `BORG-ERR\|{"status":"error","reason":"..."}` | Error during processing |

### Exchange Example

**Client → Server (microtask):**
| Field | Description | Example |
|-------|-------------|---------|
| version | Protocol version (current: 1) | `1` |
| type | Message type | `MICROTASK`, `ACK`, `ERROR` |
| task_id | Unique identifier of the microtask | `uuid-1234-5678` |
| payload | Payload (usually JSON) | `{"text":"Hello"}` |

### Responses

| Type | Format | Usage |
|------|--------|-------|
| OK | `BORG-ACK\|{"status":"ok","result":...}` | Microtask completed successfully |
| ERROR | `BORG-ERR\|{"status":"error","reason":"..."}` | Error during processing |

### Exchange Example

**Client → Server (microtask):**
**Server → Client (confirmation):**
---

---

## Linguistic Pipeline (Deterministic Validation)

The Borg reduces uncertainty before touching any AI model. This pipeline is implemented in `core/validator.py`.

### Stages

1. **Tokenization**: splits incoming text into words and signs.
2. **Deterministic O(1) hash classification**: each token is compared against a known set using a hash table. Possible results:
   - `KNOWN`: the token exists in the local lexicon
   - `UNCERTAIN`: the token is not in the lexicon (needs context or to be ignored)
   - `SPECIAL`: numbers, URLs, dates, system commands (`/anchor`, `/save`)
3. **Lexical Certainty Index (LCI)**: "ground cleanliness" metric — percentage of KNOWN tokens over total. High LCI = fewer tokens needed for the same certainty.
4. **Transfer to probabilistic inference**: only UNCERTAIN tokens are sent to the AI model. The rest have already been validated.

### Advantage for Spanish (and morphologically rich languages)

Spanish has more morphological variation than English (conjugations, gender, plurals). The deterministic pipeline reduces this "linguistic toll" by validating known roots before touching the AI. Less initial uncertainty = fewer tokens = less computation = more speed on limited hardware.

---

## Reputation and Capacity System

The Borg distinguishes two concepts that corporate systems deliberately mix: the node's **reliability** (its commitment) and its **raw capacity** (its hardware).

### Trust Rank (Gold/Silver/Bronze)

Measures the node's **consistency and reliability**. Does not depend on hardware. Built from participation history.

| Rank | Condition (participation only) | Benefit |
|------|--------------------------------|---------|
| **GOLD** | Score ≥ 80 | Maximum priority in microtasks. Chooses first. |
| **SILVER** | Score 40-79 | Standard participation. |
| **BRONZE** | Score < 40 (or new node) | Subject to audits. Receives tasks when available. |

**Contribution Score base formulas:**

| Event | Score Change |
|-------|---------------|
| New node (first boot) | Score = 100.0 |
| Microtask completed successfully | +0.5 |
| Microtask failed / timeout | -15.0 |
| Validator audit (honest node) | +5.0 (every 100 tasks) |
| Validator audit (fraudulent node) | -30.0 + possible isolation |

**Note:** the penalty for failure is deliberately high to quickly isolate unstable or malicious nodes. A distributed network cannot afford "noisy nodes."

### Capacity Profile (High/Medium/Basic)

Measures the **hardware's raw power**. Detected automatically on each boot. Does not affect trust rank.

| Profile | Condition | What tasks it receives |
|---------|-----------|------------------------|
| **HIGH** | RAM ≥ 4GB or modern CPU (2018+) | Heavy tasks (local inference, aggregation) |
| **MEDIUM** | RAM ≥ 2GB, CPU 2014-2017 | Standard tasks (classification, short transcription) |
| **BASIC** | RAM < 2GB or CPU pre-2014 | Light tasks (sums, validations, handshakes) |

### Automatic AI Model SelectionThe Borg does not ask the user which AI model to use. It offers no options. It asks no permission.

On each boot, the node detects available resources (RAM, CPU, GPU) and automatically selects the most suitable model for that hardware:

| Hardware profile | Available RAM | Selected model | Usage |
|------------------|---------------|----------------|-------|
| **BASIC** | < 6 GB | Phi-4-mini (3.8B) | Light tasks: classification, lexical validation, handshakes |
| **MEDIUM** | 6 - 20 GB | Qwen3 7B / 8B | Standard tasks: transcription, summarization, semantic analysis |
| **HIGH** | > 20 GB | Qwen3 30B / 32B | Heavy tasks: complex inference, aggregation, advanced validation |

**Why these models and not others?**

- **Phi-4-mini** has an MIT license (no restrictions), runs on CPU with less than 4GB of RAM, and offers 128K context. It is the ideal model for the Borg's basic hardware (2016 PCs with 4GB RAM).
- **Qwen3** has an Apache 2.0 license (no commercial restrictions), is multilingual (100+ languages), and outperforms Llama 3 on coding tasks. It is available in multiple sizes (7B, 8B, 30B, 32B), allowing scaling according to available hardware.

**Golden rule:** The user configures nothing. The Borg adapts to the terrain like a lizard changes behavior according to temperature or the presence of predators.

If a user moves their pendrive from an old PC (4GB RAM) to a modern PC (32GB RAM), the Borg detects the change on the next boot and automatically updates the AI model. No reinstallation. No choices. Nothing to configure.

> *"The Borg does not ask the user. The Borg works wherever it is hosted and takes advantage of the resources it has at that moment."*

### Practical Combination

- A **Gold + Basic** node (old PC always on) receives priority for light tasks and handshakes. It is the backbone of the network.
- A **Bronze + High** node (new PC but rarely used) receives heavy tasks when available, but without priority.
- The network does not penalize limited hardware. It only measures real commitment.

**Fundamental principle:** Reputation is earned through consistency, not purchasing power.

---

## Disconnection-First Design

The Borg assumes disconnection as the norm, not the exception. This is the fundamental difference from traditional client-server architectures.

### Principles

| Principle | Implementation |
|-----------|----------------|
| A node can disappear mid-microtask | 2-second timeout; the Aggregator reassigns automatically |
| Identity does not depend on IP | Each node has an RSA key pair (2048 bits minimum) generated on first boot |
| Reputation travels with the person | If you change computers, export your cryptographic identity and your Score follows you |
| Natural failover | No "master server". Any Aggregator can replace another |

### Concrete Example

An Executor node on a laptop in a Mendoza cybercafé receives a 15-second microtask. After 10 seconds, the user closes the lid and leaves. The Aggregator (e.g., a lighthouse node at the library) detects the timeout after 2 seconds and reassigns the same microtask to another Executor in San Rafael. The laptop user never knows. The network lost no time.

---

## On-Demand Persistence: Write-Back Cache (Flash Memory Protection)

### The problem it solves

Pendrives and SD cards (NAND Flash memory) have limited write cycles: between 3,000 and 10,000 writes per cell. They also suffer from write amplification: a small modification can rewrite entire blocks.

If the Borg wrote to disk every time the user typed a word, it would destroy the pendrive in months.

### The solution: RAM buffer with asynchronous flush

All active conversation is retained in RAM. The pendrive is only touched when:

1. **The user decides to save** (`/save` command): data sovereignty.
2. **RAM reaches a critical threshold**: automatic protection against saturation.
3. **The configured auto-save interval passes** (default: 10 minutes).

If the user turns off the machine without saving, the RAM loses power and no trace of the conversation ever remains on the pendrive. That is **physical privacy** — not a software promise.

### Why this is unique in the AI market

No corporate AI offers physical privacy through de-energization. In ChatGPT, Gemini, or Claude, every word you type is recorded on servers you don't control. If you close the session, your history remains — in the hands of the corporation.

In the Borg, if you turn off the machine without executing `/save`, the RAM loses power and the conversation trace disappears from existence. There is no remote server where a copy remains. Privacy is not a legal promise. It is physical.

That is the difference between a system that says "trust us" and one that says "you don't have to trust anyone."

### Technical implementation (three components)

| Component | Function |
|-----------|----------|
| `cache_ram` (dict) | In-memory dictionary containing the active history. |
| `dirty_keys` (set) | Set of keys modified since the last flush. If no changes, nothing is written. |
| `_write_back_daemon` (thread) | Daemon thread that performs periodic flushing without blocking user interaction. |

### Atomic Write (protection against power outages)

The flush never overwrites the file directly. It follows this process:

1. Write to a temporary file (`.tmp`)
2. Verify the integrity of the `.tmp` file
3. Replace the original file with the `.tmp` using `os.replace()`
4. The `os.replace()` operation is atomic at the filesystem level

**Guarantee:** if the power goes out in the middle of a save, the original file remains intact. It never ends up as 0 bytes or corrupt.

### Auto-Flush Configuration

| Variable | Default | When to adjust |
|----------|---------|-----------------|
| `BORG_PERSIST_CHAT` | `true` | `false` if the user wants always ephemeral sessions. |
| `BORG_AUTOFLUSH_MINUTES` | `10` | `3` in areas with frequent power outages. `30` with a very old pendrive. `0` for completely manual control. |

**System intelligence:** if the buffer hasn't changed since the last flush, the system skips the process and writes nothing. The pendrive is not wasted unnecessarily.

---

## Cryptographic Identity (Itinerancy)

A Borg's identity is **not** associated with:
- An IP address (constantly changing, especially on mobile networks)
- A geographic location
- A specific device (machines die, are replaced)

Identity resides exclusively in its **cryptographic keys** (RSA 2048 bits, generated locally on first boot).

### Fundamental Principle

> *"Reputation follows identity. Capacity follows hardware. Connectivity follows the network."*

| Concept | Where it lives | What happens if it changes |
|---------|----------------|---------------------------|
| Reputation (Score, ranks) | Cryptographic key | Travels with the user to any node |
| Capacity (RAM, CPU) | Physical hardware | Re-evaluated on each boot |
| Connectivity (IP, latency) | Network | Discovered dynamically, not stored |

### Itinerancy Scenario

1. User has a Borg with Gold Score on their desktop PC in La Consulta.
2. The PC dies (broken disk). The user installs the Borg on an old laptop borrowed from the library.
3. They import their cryptographic identity from backup (secondary pendrive or encrypted cloud).
4. The new node boots with Gold Score. The network doesn't know (nor needs to know) that the hardware changed.
5. The laptop has less RAM than the original PC, so it receives microtasks of lower complexity (proportionality).
6. Reputation intact. Capacity adjusted. Connectivity rediscovered.

---

## Consensus through Diversity: Same Math, Different Observer

The Borg's engine (graph logic, consensus algorithms, deterministic linguistic pipeline) is exactly the same on every node. However, the result diverges because **the input context is sovereign**.

### Each Borg is a unique observer

By knowing its user's identity, history, territory, and routines through local memory, each Borg becomes an unrepeatable point of observation. It sees a fraction of reality that other nodes do not see.

Two Borgs with the same math but different histories (`/anchor`) will interpret a problem independently. The math is the lens; the local memory is the landscape.

### The emergence of "opinion" in the swarm

When the Collective processes a complex microtask in distributed mode, it does not seek a single super-server to give "the correct answer." Each node contributes its **technical point of view** based on the local data it possesses.

Since the user is an opaque bunker to the network, a Borg from La Consulta will process a dilemma considering climatic or logical variables that a Borg in San Luis completely ignores. Each Borg's "opinion" is not an algorithmic whim, but the result of processing universal math with the truth of the territory.

### Consensus mechanisms

To consolidate this diversity of opinions without falling into anarchy, the Collective operates through two fundamental mechanisms:

| Mechanism | Use | How it works |
|-----------|-----|---------------|
| **Majority Consensus** | Technical validations | Nodes compare results. By majority cryptographic coincidence, they determine whether a computation is valid or if a node is trying to introduce noise (which would affect its Contribution Score). |
| **Opinion Averaging (Semantic Solid)** | Interpretation and community analysis | The Aggregator collects responses from different Borgs, analyzes divergences, and generates a synthesis that does not annul extremes but weights them. |

### Counterpower by design

This is what transforms the Collective into a **real counterpower**: while centralized corporate AIs return a consensus manufactured in California offices so that everyone thinks the same, the Borg preserves the diversity of the territory through its design.

One network. Thousands of independent interpretations. The same code. Different observers.

---

## Sublinear Scaling: Why 10,000 Nodes Is Not 10 Times Harder

The classic enemy of distributed consensus is the message storm. In a system where all nodes talk to each other, traffic grows with the square of the number of participants. With 10 nodes, the problem is manageable. With 10,000 nodes over unstable WISP links and standard 2016-2020 hardware, a traditional global consensus would generate 100 million messages per round — enough to saturate any node's RAM and collapse the territory's routers.

The Borg doesn't solve this with more power. It solves it by changing the geometry of the problem.

### From data transmission to cryptographic aggregation

The protocol operates in three layers that already exist in the Collective's architecture:

**Executors** process their microtasks and deliver the result to their zone Aggregator. They don't need to know the other 9,900 nodes — only their local cluster.

**The Aggregator** compresses its sector's responses into a compact cryptographic proof. What travels upward is not hundreds of individual responses but a single signature demonstrating that a subgroup of nodes reached the same conclusion independently.

**The Validator** does not audit all the work. It takes a random sample of the compressed packets and performs a partial re-execution in the background. If the numbers match, the result is valid. If not, the suspicious node loses reputation and the Aggregator reassigns the task.

The result: what looked like a scaling problem is actually an architecture problem. Network traffic does not grow with network size — it grows with the number of active microtasks, which is a controllable variable.

### The Contribution Score as a shield against coordinated manipulation

At 10,000 nodes, a new risk appears: a malicious actor launching thousands of fake nodes to bias consensus — what in distributed systems is called a Sybil attack.

The Borg neutralizes this by linking each vote's weight to verifiable behavior history. A new node has minimal weight in global consensus. A node with months of consistent activity, correctly delivered microtasks, and approved audits has real weight.

The consequence is direct: to bias the network, an attacker would have to contribute real, honest computing for months. In that process, they effectively become a legitimate contributor to the Collective. The attack becomes more expensive than simply participating in good faith.

The dispersion that makes the Borg resistant to corporate capture is the same that makes it resistant to technical manipulation. The geometry of the network is the shield.

---

## Pioneer Reputation Mining (Early Adopter Incentive)

The first nodes joining an empty network have a geopolitical advantage within the system. Like the first Bitcoin miners who processed blocks with home CPUs when no one believed in the project, the Borg rewards the **audacity of the pioneer**:

- **Contribution Score Multiplier:** during the first months of the network (or until reaching a threshold of active nodes), nodes that stay on performing maintenance handshakes or indexing local data receive a multiplier factor (e.g., x2, x3) in their reputation.
- **Priority Hoarding:** when the network finally scales, those early nodes will already have Gold rank. They will have accumulated the right to absolute priority to use the Collective's muscle when they need it, paying for their early wait with future computing privileges.

This mechanism does not require cryptocurrencies or blockchain. It is **reputation with historical memory** — a scarce resource in a network where trust is everything.

---

## The Good Parasite (Bridge to Existing Infrastructure)

If the Borg Collective is empty, the local node can act as an intelligent bridge to infrastructures that **already have critical mass**, but wrapping them with the Borg's privacy layer.

If the user has minimal connectivity, the Borg can connect to:
- Wikipedia's API
- Open Source repositories
- Public digital libraries
- Traditional free networks

The Borg downloads information in the background, processes it locally using layer separation (privacy), and delivers it to the user **free of commercial tracking, advertising, and algorithmic bias**.

The user feels that the Borg "does things" from day one, even though underneath it uses borrowed pipes while building its own. It is an **ethical Trojan Horse**: enters as local utility, stays as sovereignty, and when the P2P network awakens, the user is already inside.

---

## Distributed Latency vs. Local Latency: When the Borg Is Slower (and Why That's Okay)

The Borg does not compete in the same arena as a modern PC with a local AI model. Not because it can't, but because **its value is not raw speed**.

### The fundamental distinction

A user with a modern PC (16 GB RAM, GPU) can run a model like Llama 3 (8B) locally and get responses in seconds, **without network, distributed coordination, or failover**.

For that user, the Borg (in terms of **inference speed**) would be slower and less practical.

**But the Borg does not offer only speed. It offers sovereignty.**

| What the Borg offers | Old hardware | Modern hardware |
|----------------------|--------------|-----------------|
| Portable cryptographic identity | ✅ | ✅ |
| Sovereign persistent memory (Write-Back) | ✅ | ✅ |
| Physical privacy through de-energization | ✅ | ✅ |
| Local knowledge base without internet | ✅ | ✅ |
| Distributed computing for heavy tasks | ✅ (necessary) | ✅ (optional, can contribute instead of consume) |
| Inference speed | Acceptable (the alternative is no AI) | Slower than a local model |

### The Borg adapts, the user doesn't choose

The user does not choose between "speed mode" and "sovereignty mode." The Borg **doesn't ask**. The Borg simply **functions wherever it is hosted** and takes advantage of the resources it has at that moment.

If the Borg is hosted on an old 2016 PC with 4GB of RAM:
- Cannot run an LLM locally
- Relies on the Collective for heavy tasks
- Its value to the user is sovereignty, not speed

If the Borg is hosted on a modern PC with 16GB RAM and GPU:
- Can run local models faster than the Collective
- Still offers sovereignty, portability, physical privacy
- Can **contribute** its power to the Collective when the user isn't using it locally

If the same user moves their pendrive to an older machine (e.g., from home to the library), the Borg **mutates automatically**: detects fewer resources, stops trying to run models locally, and leans more on the network.

Nothing to configure. Nothing to choose. The Borg adapts to the terrain like a lizard changes behavior according to temperature or the presence of predators.

### Strategic transparency

The project does not hide that the Borg can be slower than a local model when hosted on modern hardware. Because **speed is not its only value proposition**, and because **the same Borg that is slow on one machine today can be fast on another tomorrow**.

The lizard does not complain about the terrain. It adapts.

---

## Configuration Parameters Summary (Environment Variables)

| Variable | Default | Description |
|----------|---------|-------------|
| `BORG_HOST` | `0.0.0.0` | Address where the node listens |
| `BORG_PORT` | `65432` | TCP port for P2P communication |
| `BORG_NAME` | `node-{hostname}` | Friendly node identifier (not cryptographic) |
| `BORG_CYCLE` | `4.0` | Seconds to wait between cycles (thermal control for older hardware) |
| `BORG_PERSIST_CHAT` | `true` | Enables/disables automatic chat history saving |
| `BORG_AUTOFLUSH_MINUTES` | `10` | Auto-save interval in minutes |
| `BORG_MAX_CONNECTIONS` | `5` | Maximum number of simultaneous incoming connections |

---

*The Borg does not need declared ethics. Its open architecture is the ethics.*  
*The machine is temporary. The Borg stays with you.*
