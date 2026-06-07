# Colectivo B.O.R.G.
### Benefit Optimization & Resource Grid
### *Distributed AI collective for the 60% left behind*

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-AGPL_v3-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/milestone-Embryo_🧬-yellowgreen.svg)]()
[![Hardware](https://img.shields.io/badge/hardware-2016_era_%2B-orange.svg)]()
[![Donate](https://img.shields.io/badge/Donate-Mercado_Pago-009ee3.svg)](https://link.mercadopago.com.ar/donaralcolectivoborg)

---

🌐 [Español](README.md) | **English** | [Português](README.pt.md) | [हिन्दी](README.hi.md) | [中文](README.zh.md)

---

> *"The machine is temporary. The Borg stays with you."*
>
> *"Memory is never alienated — it remains on the user's local node.*
> *Computing is socialized — the peer network resolves it.*
> *The Borg is the identity. The Collective is the muscle."*
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

### Trust Rank (Gold/Silver/Bronze)

Measures the node's **consistency and reliability**. Does not depend on hardware. Built from participation history.

| Rank | Condition (participation only) | Benefit |
|------|--------------------------------|---------|
| 🥇 **GOLD** | Score ≥ 80 | Maximum priority in microtasks. Chooses first. |
| 🥈 **SILVER** | Score 40-79 | Standard participation. |
| 🥉 **BRONZE** | Score < 40 (or new node) | Subject to audits. Receives tasks when available. |

**Contribution Score base formulas:**

| Event | Score Change |
|-------|---------------|
| New node (first boot) | Score = 100.0 |
| Microtask completed successfully | +0.5 |
| Microtask failed / timeout | -15.0 |
| Validator audit (honest node) | +5.0 (every 100 tasks) |
| Validator audit (fraudulent node) | -30.0 + possible isolation |

> *"Reputation is earned through consistency, not purchasing power."*

### Capacity Profile (High/Medium/Basic)

Measures the **hardware's raw power**. Detected automatically on each boot. Does not affect trust rank.

| Profile | Condition | What tasks it receives |
|---------|-----------|------------------------|
| **HIGH** | RAM ≥ 4GB or modern CPU (2018+) | Heavy tasks (local inference, aggregation) |
| **MEDIUM** | RAM ≥ 2GB, CPU 2014-2017 | Standard tasks (classification, short transcription) |
| **BASIC** | RAM < 2GB or CPU pre-2014 | Light tasks (sums, validations, handshakes) |

### Practical Combination

- A **Gold + Basic** node (old PC always on) receives priority for light tasks and handshakes. It is the backbone of the network.
- A **Bronze + High** node (new PC but rarely used) receives heavy tasks when available, but without priority.
- The network does not penalize limited hardware. It only measures real commitment.

---

## Linguistic Processing Pipeline

Inspired by compiler architecture: resolve deterministic issues first, reserve probabilities for genuinely ambiguous cases.

**Fundamental rule:** `WORD NOT FOUND ≠ INCORRECT WORD`

---

## Hardware (Updated for 2026)

The Borg targets equipment manufactured between **2016 and 2020** — machines that still circulate in schools, libraries, homes, and cooperatives.

| Device | Minimum Requirement | RAM | Role |
|--------|---------------------|-----|------|
| Desktop / Laptop | 2015 onwards, 64-bit CPU | 4 GB | Executor, Light Aggregator |
| Android Phone | 2018 onwards (Android 8+) | 3 GB | Mobile Executor, Itinerant node |
| Raspberry Pi / SBC | Raspberry Pi 3B+ onwards | 1-4 GB | Light Lighthouse Node |
| Very old PC (optional) | 2010-2014, 2 GB RAM | 2 GB | Executor for minimal microtasks |

> *"A phone can contribute minutes. A laptop can contribute hours. An old PC can be a permanent node. Everyone participates according to their possibilities."*

### Preloaded Knowledge Base

The Embryo pendrive includes a portable library (<500 MB) with local dictionaries, agriculture manuals, first aid guides, WISP documentation, and public domain texts. The first node has immediate value even without a network.

---

## Three Modes of Incorporation

| Mode | Description | Device Owner |
|---|---|---|
| **Portable Borg** | Bootable USB drive. RootFS on RAM. Doesn't touch the disk. Portable identity. | The user |
| **Installed Borg** | Background service on Windows / Linux / Android. Like an antivirus. | The user |
| **Dedicated Borg** | Old PC fully dedicated. No desktop. No icons. Only the Collective. | The Collective |

---

## Installation and First Node

```bash
# 1. Clone the repository
git clone https://github.com/dominguezeddie/colectivo-borg.git
cd colectivo-borg

# 2. Start the server node (Terminal 1)
python embrion.py --modo servidor --identidad "node-1"

# 3. Send a test microtask (Terminal 2)
python embrion.py --modo cliente --host localhost --mensaje "HELLO BORG"
