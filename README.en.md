# Colectivo B.O.R.G.
### Benefit Optimization & Resource Grid
### *Distributed AI collective for the 60% left behind*

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-AGPL_v3-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/milestone-Embryo_🧬-yellowgreen.svg)]()
[![Hardware](https://img.shields.io/badge/hardware-Windows_7_era_%2B-orange.svg)]()
[![Donar con Mercado Pago](https://img.shields.io/badge/Donar-Mercado_Pago-009ee3.svg)](https://link.mercadopago.com.ar/donaralcolectivoborg)

---

🌐 [Español](README.md) | **English** | [Português](README.pt.md) | [हिन्दी](README.hi.md) | [中文](README.zh.md)

---

> *"The machine is temporary. The Borg stays with you."*
>
> *"The Borg doesn't need declared ethics. Its open architecture is the ethics."*
>
> *"Resistance to technological obsolescence is futile. Join the Collective."*
>
> *"The world needs more Borgs and fewer data centers."*

---

## Terminal Borg — Central Interface

![Terminal Borg](https://raw.githubusercontent.com/dominguezeddie/colectivo-borg/main/Terminal%20Borg.png)

## The Three Roles of the Mother Cell

![Diagram of the Three Roles](https://raw.githubusercontent.com/dominguezeddie/colectivo-borg/main/Diagrama%20de%20los%20Tres%20Roles.png)

---

## What is the Colectivo Borg?

The **Colectivo Borg** is a distributed, open source, and ecologically honest artificial intelligence network, designed for the **60% of humanity** that has no real access to corporate AIs.

It is not a company. It has no shareholders. It has no central server. It has no terms of service that can change tomorrow.

It is collective cognitive infrastructure — like Wikipedia, but for distributed AI computing.

---

## The Problem It Solves

| Problem | Real Impact |
|---|---|
| **Energy consumption** | An AI data center consumes as much electricity as a medium-sized city |
| **Corporate monopoly** | 3-4 companies decide who gets access and under what conditions |
| **Exclusion of 60%** | Cost in hard currencies, insufficient connectivity, linguistic and cultural barriers |
| **Linguistic toll** | Spanish consumes **59% more tokens** than English — non-English speakers pay more for the same result |

When corporations ration capacity, the 60% notices first. The Borg solves this by design: **no tokens, no scarcity, no owner.**

---

## Architecture: The Three Roles of the Mother Cell

```
┌──────────────────────────────────────────────────────────────┐
│                      COLECTIVO BORG                          │
│                                                              │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐      │
│  │  VALIDATOR  │    │  AGGREGATOR │    │   EXECUTOR  │      │
│  │ "The Auditor"│   │"The Synth." │    │ "The Muscle"│      │
│  │             │    │             │    │             │      │
│  │ Verifies    │    │ Assembles   │    │ Processes   │      │
│  │ data        │    │ partial     │    │ atomic      │      │
│  │ integrity   │    │ results     │    │ microtasks  │      │
│  └─────────────┘    └─────────────┘    └─────────────┘      │
│                                                              │
│            ATOMIC MICROTASKS (1 to 30 seconds)              │
│               Immune to disconnections                       │
└──────────────────────────────────────────────────────────────┘
```

### Ranking System

| Rank | Score / RAM | Profile |
|---|---|---|
| 🥇 **GOLD** | Score ≥80 / RAM ≥4GB | Constant precision and high availability |
| 🥈 **SILVER** | Score 40-79 / RAM ≥2GB | Stable performance with minimal deviations |
| 🥉 **BRONZE** | Score <40 / RAM <2GB | 2011-era hardware — resistance is futile, it still contributes |

> *"Reputation is built by the person, not the hardware."*

---

## Linguistic Processing Pipeline

Inspired by compiler architecture: resolve deterministic issues first, reserve probabilities for genuinely ambiguous cases.

```
Input text
      │
      ▼
┌──────────────────┐
│  LEXICAL ANALYSIS│  → Tokenize + search hash dictionary O(1)
│  (deterministic) │  → KNOWN / UNCERTAIN / SPECIAL
└────────┬─────────┘
         │  Clean ground — verified certainties
         ▼
┌──────────────────┐
│SYNTACTIC ANALYSIS│  → Grammar structure on verified ground
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│   PROBABILISTIC  │  → LLM works with fewer tokens and less noise
│    INFERENCE     │  → The 59% linguistic toll is reduced here
└──────────────────┘
```

**Fundamental rule: `WORD NOT FOUND ≠ INCORRECT WORD`**

---

## Three Modes of Incorporation

| Mode | Description | Device Owner |
|---|---|---|
| **Portable Borg** | Bootable USB drive. RootFS on RAM. Doesn't touch the disk. Portable identity. | The user |
| **Installed Borg** | Background service on Windows / Linux / Android. Like an antivirus. | The user |
| **Dedicated Borg** | Old PC fully dedicated. No desktop. No icons. Only the Collective. | The Collective |

> *"A phone can contribute minutes. A laptop can contribute hours. An old PC can be a permanent node. Everyone participates according to their possibilities."*

---

## Minimum Requirements

Designed for hardware capable of running **Windows 7 or later** (2007 onwards):

| Component | Minimum | Notes |
|---|---|---|
| CPU | x86/x64, any post-2007 | Core 2 Duo, i3 2011, AMD FX — all valid |
| RAM | 512 MB | 1 GB recommended for RootFS on RAM |
| Network | WiFi / Ethernet / Mobile data | Intermittent connectivity tolerated |
| Python | 3.8+ | 3.12 recommended |
| External dependencies | **None** | Standard Python library only |

---

## Installation and First Node

```bash
# 1. Clone the repository
git clone https://github.com/dominguezeddie/colectivo-borg.git
cd colectivo-borg

# 2. Start the Executor node (Terminal 1)
python main.py

# 3. Send a test microtask (Terminal 2)
python emisor.py --texto "The house was very big and had a garden."
```

---

## Roadmap (Biological Milestones)

| Milestone | Status | Objective |
|---|---|---|
| 🧬 **Embryo** | ✅ In progress | Two nodes communicating with protocol and confirmation |
| 🦠 **Cell** | ⏳ Pending | Three nodes, differentiated roles, basic failover |
| 🧵 **Tissue** | ⏳ Pending | Working reputation + first real useful task (audio/image/text) |
| 🫀 **Organ** | ⏳ Pending | Bootable USB drive, portable cryptographic identity |
| 🌐 **Organism** | ⏳ Pending | Public network, embedded OS, Terminal Borg, active community |

---

## Why the Borg Is Incorruptible

| Aspect | Corporate AI | Colectivo Borg |
|---|---|---|
| Owner | A corporation with shareholders | Nobody. The network belongs to everyone. |
| Code | Closed and secret | Open — auditable by anyone |
| Incentive | Maximize corporate profit | Common good |
| Corruption | Possible in silence | Impossible — the code is public |
| Corporate acquisition | Possible | **Impossible** — no central asset to buy |

> *"The Borg cannot be bought. There is no central asset to acquire."*

---

## About the Origin

**Raúl Edmundo "Eddie" Domínguez** — La Consulta, Mendoza, Argentina.

University-level Microprocessor Technician. 25 years as a WISP network operator.

This project does not come from a corporate laboratory. It comes from the field — from someone who saw the problem up close for decades and decided to build the solution. Born in May 2026.

Sustained by voluntary donations — Wikipedia / Linux model.

---

## Contributing

The Borg grows like a living organism. The community is the immune system.

1. Fork the repository
2. Branch: `git checkout -b feature/clear-description`
3. Commit: `git commit -m "description of the problem it solves"`
4. Pull Request with context

Any device with Python can be a node.
Any person with the same spirit can contribute.

---

## License

**AGPL v3** — This belongs to everyone, but to no one in particular so that it can be closed.

---

*Assimilation begins here.*
