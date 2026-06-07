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

### Practical Combination

- A **Gold + Basic** node (old PC always on) receives priority for light tasks and handshakes. It is the backbone of the network.
- A **Bronze + High** node (new PC but rarely used) receives heavy tasks when available, but without priority.
- The network does not penalize limited hardware. It only measures real commitment.

**Fundamental principle:** Reputation is earned through consistency, not purchasing power.
