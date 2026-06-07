# Compatible Hardware — Borg Collective

## It's Not Recycling — It's Universality

The Borg does not discriminate by age, brand, or capacity. A brand new
state-of-the-art PC and a 2018 cell phone are both valid nodes. Each
contributes according to what it has.

The Borg does NOT refer to 486 CPUs or 90s Pentiums.
The target hardware is that capable of running **Windows 10 or higher**,
manufactured approximately between 2016 and 2020, with x86 64-bit architecture
(or ARM in the case of cell phones and Raspberry Pi).

## Why Not 2011?

Because a decade is the real limit where hardware begins to become an obstacle,
not just "old but usable". A 2011 machine typically has 2GB of RAM, a 32-bit CPU,
and an unsupported Windows 7 installation. That is not functional recycling —
it is archaeology. The Borg is a lizard, not a paleontologist.

**The principle remains:** we do not ask for new hardware. We use what is already
turned on in institutions, but within a range that can still do something useful
without frustrating the user.

---

## Real Minimum Requirements (2026 Update)

- 64-bit CPU manufactured approximately between 2016 and 2020
  (Intel Core 6th to 10th generation, AMD Ryzen 1xxx to 3xxx,
   or equivalent ARM on mobile devices)
- 4 GB of RAM as minimum recommended (2 GB can work for very light tasks
   but with degraded experience)
- Storage: 8 GB free (for base system plus persistent history)
- Internet connection (WiFi, mobile data, ethernet) — may be intermittent
- Some resource to offer: CPU, RAM, or time availability

**Note on older equipment:** A decade-old machine with 2GB of RAM and a 32-bit CPU
can still be an Executor node for extremely simple microtasks (sums, basic validations).
But it cannot be the design target. The Borg does not exclude those machines,
but neither is it tied to them.

---

## Minimum Hardware Table by Device Type

| Device | Minimum Requirement | CPU / Chip | RAM | Recommended OS | Role in the Borg |
|--------|---------------------|------------|-----|-----------------|------------------|
| Desktop / Laptop | 2015 onwards | 64-bit CPU, 2+ cores | 4 GB | Linux minimal (Alpine/Debian) or Windows 10 LTSC | Executor, Light Aggregator |
| Android Phone | 2018 onwards (Android 8+) | ARM 64-bit, 4+ cores | 3 GB | Android 8 Oreo or higher | Mobile Executor, Itinerant node |
| Raspberry Pi / SBC | Raspberry Pi 3B+ onwards | ARM Cortex-A53 64-bit | 1 GB (Pi 3) / 4 GB (Pi 4) | Raspberry Pi OS Lite / Alpine ARM | Light Lighthouse Node, Permanent Executor |
| Very old PC (optional) | 2010-2014, 2 GB RAM | x86 32-bit or slow 64-bit | 2 GB | Alpine Linux 32-bit | Executor for minimal microtasks |

**Note:** devices in the last row are not the Borg's design target, but they are not excluded.
They can participate as low-capacity nodes for elementary microtasks. The system adapts
task assignment to the hardware profile declared by the node upon registration.

---

## Preloaded Static Knowledge Base

To ensure the first node has immediate value even without a network, the Embryo
pendrive will include a portable, incorruptible library with:

- Local dictionaries and lightweight compression models
- Local agriculture manuals, first aid guides, and WISP technical documentation
- Philosophy texts, basic law, and general knowledge (public domain)
- Complete Borg Collective documentation

This knowledge base occupies less than 500 MB and allows the user to access
useful information from Day Zero, without depending on the internet or corporate
servers. The pendrive is not just a network key. It is a pocket-sized library
that travels with the user.

---

## Approximate Power by Era (2016-2026 Update)

| Period | Approx. Power | Examples | What it can do for the Borg |
|--------|---------------|----------|----------------------------|
| 2016-2017 (~10 years ago) | 100-200 GFLOPS | Intel Core i5-6400, AMD A10-9700, Raspberry Pi 3 | Simple microtasks: basic classification, calculation, short audio transcription with light models |
| 2018-2019 (~7 years ago) | 200-500 GFLOPS | Intel Core i7-8700, AMD Ryzen 5 2600, Apple A12 | Local inference of tiny models, simple aggregation |
| 2020-2021 (~5 years ago) | ~1 TFLOP | AMD Ryzen 7 5800X, Intel Core i9-11900K, Apple M1 | Smooth local inference, small models, aggregation |
| 2024-2026 (today) | 1-5 TFLOPS CPU / 50+ GPU | AMD Ryzen 9 7950X, Intel Core Ultra 7, Apple M4 | High-capacity Aggregator or Validator node |

**Key fact:** a machine manufactured a decade ago (2016) is still useful for
distributed microtasks. What 10 years ago was a "normal PC" is today the Borg's
entry floor. The digital divide is not crossed by demanding modern hardware —
it is crossed by using what already exists, not what existed 15 years ago.

---

## Deployment Modalities by Hardware

### Old PC with no other use (Borg Dedicated)
- Without hard drive: boots from pendrive with RootFS on RAM
- With hard drive: dedicated installation, no desktop
- Consumes minimal resources — old CPU working within its range

### PC or laptop in use (Borg Installed)
- Runs as a background service
- Only uses idle resources
- Transparent to the user

### Android Cell Phone (Termux)
- Termux installs Linux environment without root
- Requires Android 8 or higher, 3GB RAM minimum recommended
- Mobile node connected via WiFi or mobile data
- In Latin America and Africa: one of the most common entry points

### Bootable Pendrive (Borg Portable)
- 64 GB or 128 GB recommended (for preloaded knowledge base)
- Alpine Linux (~500 MB) + Python + Borg core
- Preloaded knowledge base (~500 MB)
- All remaining space belongs to the Collective
- RootFS on RAM: when unplugged, the PC remains untouched

---

## Thermal Control for Older Hardware

The `BORG_CYCLE=4.0` parameter (4 seconds pause between cycles) is crucial
for equipment from the last decade. It prevents busy-waiting and keeps the
hardware cool and stable during continuous operation.

Adjust to lower values (0.5-1 second) only on modern hardware with good cooling.

---

## Scale Compensates for Individual Efficiency

A biological neuron is inefficient compared to a modern chip. But 86 billion
neurons together produce something no chip can replicate. A slow node in the
Borg is not a problem — it is one more neuron. The system does not depend on
each node being powerful. It depends on there being many nodes.

---

*The machine is temporary. The Borg stays with you.*
