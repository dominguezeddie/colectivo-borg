# Technical Architecture — Borg Collective

> *"Memory is never alienated — it remains on the user's local node.*  
> *Computing is socialized — the peer network resolves it.*  
> *The Borg is the identity. The Collective is the muscle."*

## The Three Roles of the Mother Cell

Each node in the Collective assumes one or more roles according to its real physical capabilities. The same device can fulfill multiple roles simultaneously (e.g., a node with good RAM and CPU can be both Aggregator and Executor).

### The Executor ("The Muscle")

- Atomic computing unit
- Processes microtasks of 1 to 30 seconds
- State-agnostic architecture — no context maintained between tasks
- Ideal hardware: high CPU capacity
- Target: any PC with Python, even 2011 hardware
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
**Server → Client (confirmation):**
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

## Reputation System (Contribution Score)

Each node has a numerical reputation that determines its priority in microtask assignment. Implemented in `core/reputation.py`.

### Base Formulas

| Event | Score Change |
|-------|---------------|
| New node (first boot) | Score = 100.0 |
| Microtask completed successfully | +0.5 |
| Microtask failed / timeout | -15.0 |
| Validator audit (honest node) | +5.0 (every 100 tasks) |
| Validator audit (fraudulent node) | -30.0 + possible isolation |

**Note:** the penalty for failure is deliberately high to quickly isolate unstable or malicious nodes. A distributed network cannot afford "noisy nodes."

### Ranks (by Score or raw capacity)

| Rank | Condition | Benefit |
|------|-----------|---------|
| **GOLD** | Score ≥ 80 **or** RAM ≥ 4GB | Maximum priority in critical microtasks. The Aggregator chooses them first. |
| **SILVER** | Score 40-79 **or** RAM ≥ 2GB | Standard participation. Normal fragment flow. |
| **BRONZE** | Score < 40 **or** RAM < 2GB | Subject to frequent audits. Receives low-priority microtasks. |

Reputation is **personal**, not hardware-bound. It travels with the user's cryptographic identity, not with the machine.

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

## Configuration Parameters Summary (Environment Variables)

| Variable | Default | Description |
|----------|---------|-------------|
| `BORG_HOST` | `0.0.0.0` | Address where the node listens |
| `BORG_PORT` | `65432` | TCP port for P2P communication |
| `BORG_NAME` | `node-{hostname}` | Friendly node identifier (not cryptographic) |
| `BORG_CYCLE` | `4.0` | Seconds to wait between cycles (thermal control for 2011 CPUs) |
| `BORG_PERSIST_CHAT` | `true` | Enables/disables automatic chat history saving |
| `BORG_AUTOFLUSH_MINUTES` | `10` | Auto-save interval in minutes |
| `BORG_MAX_CONNECTIONS` | `5` | Maximum number of simultaneous incoming connections |

---

*The Borg does not need declared ethics. Its open architecture is the ethics.*  
*The machine is temporary. The Borg stays with you.*
