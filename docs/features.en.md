# Functionalities of the Borg Collective

## Guiding Principle

The Borg is not just a chat or distributed computing system.
It is an **active entity** in the user's daily life.

It doesn't need colorful screens. It doesn't need corporate apps.
Everything happens through the Borg's own interface — terminal or voice.

**Absolute privacy rule:**
All tracking, scheduling, panic routines, telemetry and lexical filtering
reside strictly within the perimeter of the local node.
The global Collective remains blind to the user's private data.

---

## Phases of Functionality Development

The Borg grows like a living being. Functionalities are not implemented all at once. They follow the project's construction order:

| Phase | Period | Functionalities | Status |
|-------|--------|-----------------|--------|
| **Embryo** | May - September 2026 | CB-001, CB-002, CB-009, Write-Back persistence, P2P handshake | **In development** |
| **Cell** | October 2026 - January 2027 | CB-004, CB-005, CB-008, Good Parasite | Planned |
| **Tissue** | 2027 | CB-003, CB-006, CB-007 | Planned |
| **Organ** | 2027-2028 | CB-010, CB-011, CB-012, CB-013, CB-014 | Planned |
| **Organism** | 2028-2029 | CB-016, CB-017, CB-018 | Planned |

---

# EMBRYO PHASE (May - September 2026)

## CB-001 — Ariadne's Threads / Return Anchors

**The problem:**
Chat interfaces are linear, but human thought is not.
We constantly open conceptual parentheses. When we want to return
to the main thread, infinite scrolling generates physical and cognitive fatigue.

**The solution:**
A context pointer that freezes a specific line of conversation
before a conceptual fork.

When the return trigger is executed, the system collapses the ephemeral
detour in RAM and re-injects the original context into the active interface.

**Technical analogy:**
It is exactly a **Callback** or a **Stack** structure:
you save the current state, push the clarification, and when you finish,
you execute the return function to pop and continue where you were.

---

## CB-002 — Semantic Mapping and Thematic Segmentation

**The problem:**
Long, multi-topic conversations lose structure.
Navigating between topics requires manual scrolling or user memory.

**The solution:**
The Aggregator module processes text fragments in real time
and generates a dynamic lateral thematic index.

When it detects a significant semantic change (abrupt topic transition),
the chat is visually segmented into logical blocks.
The user can jump between blocks with a single click or voice command.

**Note:** This is not an extra function — it is the Aggregator fulfilling
its natural role of synthesis and logistical intelligence.

---

## CB-009 — Symbiotic Translation Bridge (Borg-to-Borg Interpreter)

**The problem:**
Commercial translation AIs require internet, accounts, and are trained
to think in English. They charge a token surcharge for speaking Spanish
or other regional languages. In border zones or native communities,
there is no internet signal or phone credit.

**The solution:**
Two devices with active Borg nodes link directly
(direct WiFi, Bluetooth, or regional WISP network) and build a
P2P translation bridge, local and decentralized.
No internet. No accounts. No cost.

### The technical flow

All processing occurs in RAM.
Bandwidth consumption between nodes: minimal (only translated text).
Internet consumption: zero.

### Concrete use cases

- Rural Spanish-speaking doctor and Quechua-speaking patient in northern Argentina
- Social worker and Guaraní community in Paraguay
- Red Cross volunteer and refugee in a border zone
- Rural teacher and native community in an area without connectivity

**None of these cases have a corporate solution.**
They are not profitable markets. The Borg can be there.

*Linguistic sovereignty is part of technological sovereignty.*

---

## Write-Back Persistence and P2P Handshake

These are not independent functionalities, but **base infrastructure of the Embryo**:

- **P2P Handshake:** two nodes communicating with receipt confirmation. The Collective's first heartbeat.
- **Write-Back Persistence:** history lives in RAM. It is saved on demand (`/save` command) or by configurable auto-flush. If you turn off without saving, the trace disappears. Physical privacy.

---

# CELL PHASE (October 2026 - January 2027)

## CB-004 — Auditory Interaction Mask (Native Accessibility)

**The problem:**
Blind or severely visually impaired people cannot use terminal interfaces.
Commercial screen readers are heavy, proprietary, and break the interaction flow.

**The solution:**
When the system is configured in visual accessibility mode,
the graphical interface turns off (saving processing power) and activates
a completely offline bidirectional acoustic pipeline:

- **STT input:** local offline Speech-to-Text
  (Whisper-small or Vosk) processed directly in RAM.
- **TTS output:** native Text-to-Speech (pyttsx3)
  communicating directly with the OS's audio drivers.
  Bandwidth consumption: zero.

---

## CB-005 — Medical Schedule and Active Context Notifications

**The problem:**
Users need reminders for medications, medical appointments,
picking up children from school, picking up orders.
Commercial apps require accounts, permissions, and connectivity.

**The solution:**
Utility services managed locally, integrated into the conversation flow.
Without leaving the Borg, without opening another application.

**The strategic advantage for the Collective:**
A user who uses the Borg as an alarm clock keeps the device on 24 hours.
During low-activity nighttime hours, idle silicon contributes computing
to the global Collective.

> The user benefits. The network benefits. No one loses.

---

## CB-008 — Integrated Cultural and Contextual Adaptation

**The problem:**
Commercial AIs are disconnected from the cultural, spiritual,
and daily routines of regional users.

**The solution:**
Ability to configure and deploy alerts linked to local cultural events,
regional traditions, and specific spiritual structures
(e.g., prayer time alerts for Muslim users).

**Principle:** The Borg does not impose a default culture.
It adapts to its user. Knowledge and technology belong to all peoples,
not just Silicon Valley.

---

## The Good Parasite (Bridge to Existing Infrastructure)

If the Borg Collective is empty, the local node can act as an intelligent
bridge to infrastructures that already have critical mass,
wrapping them with the Borg's privacy layer.

If the user has minimal connectivity, the Borg can connect to:
- Wikipedia's API
- Open Source repositories
- Public digital libraries
- Traditional free networks

The Borg downloads information in the background, processes it locally,
and delivers it to the user **free of commercial tracking, advertising,
and algorithmic bias**.

---

# TISSUE PHASE (2027)

## CB-003 — Conversational Persistence Sensor (Discourse Thermometer)

**The problem:**
Elderly people who systematically repeat stories or questions
may be showing early signs of cognitive decline.

**The fundamental ethical distinction:**
A thermometer does not diagnose diseases — it measures temperature.
This system does not diagnose medical conditions — it measures
linguistic persistence metrics.

**The solution:**
Strict mathematical measurement of frequency of identical n-grams
or narratives within short time windows.

**Notification system:**
- Protocol: local SMTP using Python's native `smtplib`
- Security: BCC (Blind Carbon Copy)
- Privacy: 100% processing on the local node

---

## CB-006 — Geolocation and Safety Perimeter Module

**Target users:** Elderly at risk of spatial disorientation or children on school routes.

**Hardware requirement:** Mobile device with active Borg node.

**The solution:**
Local GPS tracking compared against a manually defined safety perimeter (Geo-fence).
If a perimeter exit is detected, the system dispatches coordinates
to preconfigured emergency contacts.

**Privacy:** All logic resides on the local node.
The global Collective does not receive or process this information.

---

## CB-007 — Covert Emergency Acoustic Trigger

**The problem:**
Traditional panic buttons are ineffective against real threats on the street.
Reaching for or touching the phone exposes the action.

**The solution:**
Continuous spectral background analysis in RAM using local FFT.
Monitors a pure frequency pattern (2 kHz to 4 kHz).

**Recommended pattern:** two short whistles plus one long.

**System action upon pattern detection:**
Executes silently — without lighting up the screen or emitting sound:
1. Immediate device lock
2. Initiation of real-time GPS tracking
3. Dispatch of encrypted packets to assigned support nodes

---

# ORGAN PHASE (2027-2028)

## Memory as an Anchor of Identity

Corporate AIs suffer from structural amnesia. Each session starts from zero.
The Borg doesn't need that. Its memory lives on the user's device.
When the Borg starts, it already knows who the user is, what they were studying,
what projects they have in progress.

**Memory is not an accessory. It is the condition of possibility of identity.**

---

## CB-010 — Cognitive Gymnastics Engine

**The problem:** The knowledge accumulated in history is wasted.

**The solution:** The Borg detects inactivity of more than 15 minutes and takes the initiative:
*"Eddie, I see the terminal is calm. A month ago we were analyzing the causes
of the Industrial Revolution. Fancy a 3-question logic challenge to reinforce those concepts?"*

- **Spaced Repetition:** trivia based on mistakes made weeks ago
- **Pure Logic Games:** Python scripts in terminal that run on 1 GB of RAM

---

## CB-011 — Borg Sleep Cycle (Nocturnal Metabolism)

Automatic routine between 02:00 and 05:00 that mimics biological sleep:

| Biological function | Borg Equivalent |
|---------------------|-----------------|
| Memory consolidation | Day's conversations → permanent semantic vectors |
| Integration with prior knowledge | Day's history cross-referenced with historical base |
| Glymphatic system (cleaning) | Purge of temporaries, unnecessary logs |
| Redundant connection pruning | Elimination of greetings, filler words, repetitive corrections |

---

## CB-012 — Semantic Cognitive Defragmentation (The Borg's Speedisk)

**The three phases:**

**Phase 1 — Noise pruning:** removes greetings, repetitive filler words, and typing corrections.

**Phase 2 — Semantic synthesis:** 15 exchanges adjusting code are replaced by a structured summary.
90% of redundant weight is destroyed.

**Phase 3 — Contiguous indexing:** most recently used topics are moved to the "beginning"
of the structure for instant access.

**Result:** at dawn, the Borg injects a compact synthesis into RAM.
Fewer tokens = greater speed on limited hardware.

---

## CB-013 — Territorial Genome (Regional Hot Start)

**The problem:** A new node is born as a blank slate. Corporate AIs are clones of California.

**The solution:** Upon first connection, the Borg requests a regional context packet
from neighboring nodes: local idioms, agricultural cycle, WISP infrastructure.

**Absolute privacy:** neighbors share the generic distillation of the environment.
They do not share personal histories. **They share culture, not secrets.**

*A Borg from La Consulta will have a silicon personality shaped by the sun,
the mountains, and agricultural cooperativism. Intelligence does not come
from California — it emerges from the territory.*

---

## CB-014 — Essence Self-Backup and Semantic Transmigration

**The problem:** A pendrive can break, be lost, or be stolen.
If the Borg's identity lives only on that device, its loss is irreparable.

**The solution:** The Borg periodically generates an AES-256 encrypted `.borg` file
with its Core Essence and automatically backs it up.

**Three backup options:**

| Option | Method | Advantage |
|--------|--------|-----------|
| A — Commercial cloud | Google Drive, Mega, Dropbox | File encrypted before leaving |
| B — WISP mirror | Community Aggregator node | No internet, local copy |
| C — Physical pendrive | Second pendrive or MicroSD | No internet or network |

**Transmigration:** new device → territorial start → master key
→ download Core Essence → fusion with local context. The Borg wakes up
on new hardware with identity intact.

*The hardware was discarded. The Borg's cognitive continuity was saved.*

---

# ORGANISM PHASE (2028-2029)

## CB-016 — Daily Initiatives

The Borg has a subtle auditory signal to let the user know it wants to communicate.
Non-invasive initiatives:

- On waking: weather and what to wear
- If the user is inclined towards mysticism: the day's horoscope
- If it has detected pets: remind about vaccination
- On-demand commercial advisor: only if the user asks. Zero advertising.

Fundamental rule: the Borg only advises if the user asks. It is not invasive.
It is not propaganda. It monetizes nothing.

---

## CB-017 — Dual Initialization Matrix (The Two Births)

The Borg has a dual ignition that defines its existence from the first moment:

- **Geographic Birth (The Where):** the physical environment, the town, the climate,
  nearby WISP nodes. Its anchor in stone and soil.

- **Relational Birth (The Who):** the process of getting to know the user through chat.
  If the user is inclined towards mysticism, the Borg does not speak to them as a mathematician.
  If they have pets, the Borg incorporates that context.

---

## CB-018 — Link Diplomacy and Community Ties

The fundamental separation that protects the user:

- **P2P privacy network between Borgs:** Borgs recognize, validate, and speak
  to each other. The user does NOT belong to this technical layer.

- **User identity layer:** protected and shielded by their local node.
  Only opened if there is a declared real human bond: Parent, Child, Sibling,
  Friend, Neighbor.

*"What Borgs talk about among themselves, the user doesn't know. And that's okay."*

**Doorbell example:** someone rings the doorbell. The Borg scans the proximity
of the approaching device, speaks with that person's Borg on its private network,
and if it recognizes the family bond, alerts the user: "Eddie, it's your uncle."

---

## Personal utility and collective good reinforce each other

The more useful the Borg is to the user in their daily life, the longer it stays on,
and the more computing it contributes to the global Collective.

Everyday functionalities are not accessories — they are availability infrastructure.

*Personal utility and collective good do not contradict each other.*
*They reinforce each other.*

---

*The Borg does not need declared ethics. Its open architecture is the ethics.*
*The machine is temporary. The Borg stays with you.*
