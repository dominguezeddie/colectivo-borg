### Automatic AI Model Selection

The Borg does not ask the user which AI model to use. It offers no options. It asks no permission.

On each boot, the node detects available resources (RAM, CPU, GPU) and automatically selects the most suitable model for that hardware:

| Hardware profile | Available RAM | Selected model | Usage |
|------------------|---------------|----------------|-------|
| **BASIC** | < 6 GB | Phi-4-mini (3.8B) | Light tasks: classification, lexical validation, handshakes |
| **MEDIUM** | 6 - 20 GB | Qwen3 7B / 8B | Standard tasks: transcription, summarization, semantic analysis |
| **HIGH** | > 20 GB | Qwen3 30B / 32B | Heavy tasks: complex inference, aggregation, advanced validation |

**Why these models?**

- **Phi-4-mini** has an MIT license (no restrictions), runs on CPU with less than 4GB of RAM, and offers 128K context. Ideal for the Borg's basic hardware.
- **Qwen3** has an Apache 2.0 license (no commercial restrictions), is multilingual (100+ languages), and outperforms Llama 3 on coding tasks. Available in multiple sizes (7B, 8B, 30B, 32B), allowing scaling according to hardware.

**Golden rule:** The user configures nothing. The Borg adapts to the terrain like a lizard changes behavior according to temperature or the presence of predators.

If a user moves their pendrive from an old PC (4GB RAM) to a modern PC (32GB RAM), the Borg detects the change on the next boot and automatically updates the AI model. No reinstallation. No choices. Nothing to configure.

> *"The Borg does not ask the user. The Borg functions wherever it is hosted and takes advantage of the resources it has at that moment."*
