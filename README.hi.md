# Colectivo B.O.R.G.
### Benefit Optimization & Resource Grid
### *60% वंचित मानवता के लिए वितरित AI सामूहिक*

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-AGPL_v3-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/milestone-भ्रूण_🧬-yellowgreen.svg)]()
[![Hardware](https://img.shields.io/badge/hardware-Windows_7_era_%2B-orange.svg)]()

---

🌐 [Español](README.md) | [English](README.en.md) | [Português](README.pt.md) | **हिन्दी** | [中文](README.zh.md)

---

> *"मशीन अस्थायी है। Borg आपके साथ रहता है।"*
>
> *"Borg को घोषित नैतिकता की जरूरत नहीं। इसकी खुली वास्तुकला ही नैतिकता है।"*
>
> *"तकनीकी अप्रचलन का प्रतिरोध व्यर्थ है। Collective में शामिल हों।"*
>
> *"दुनिया को अधिक Borg और कम data centers की जरूरत है।"*

---

## Terminal Borg — केंद्रीय इंटरफेस

![Terminal Borg](https://raw.githubusercontent.com/dominguezeddie/colectivo-borg/main/Terminal%20Borg.png)

## Mother Cell के तीन भूमिकाएं

![तीन भूमिकाओं का आरेख](https://raw.githubusercontent.com/dominguezeddie/colectivo-borg/main/Diagrama%20de%20los%20Tres%20Roles.png)

---

## Colectivo Borg क्या है?

**Colectivo Borg** एक वितरित, open source और पारिस्थितिक रूप से ईमानदार कृत्रिम बुद्धिमत्ता नेटवर्क है, जो मानवता के उन **60%** लोगों के लिए बनाया गया है जिनके पास कॉर्पोरेट AI तक वास्तविक पहुंच नहीं है।

यह कोई कंपनी नहीं है। इसके कोई शेयरधारक नहीं हैं। इसका कोई केंद्रीय सर्वर नहीं है।

यह सामूहिक संज्ञानात्मक बुनियादी ढांचा है — Wikipedia की तरह, लेकिन वितरित AI कंप्यूटिंग के लिए।

---

## यह किस समस्या को हल करता है

| समस्या | वास्तविक प्रभाव |
|---|---|
| **ऊर्जा खपत** | एक AI data center एक मध्यम आकार के शहर जितनी बिजली खपत करता है |
| **कॉर्पोरेट एकाधिकार** | 3-4 कंपनियां तय करती हैं कि किसे पहुंच मिले |
| **60% का बहिष्करण** | कठिन मुद्राओं में लागत, अपर्याप्त कनेक्टिविटी, भाषाई बाधाएं |

---

## तीन भागीदारी के तरीके

| तरीका | विवरण | डिवाइस का मालिक |
|---|---|---|
| **Borg Portable** | Bootable USB drive। RAM पर RootFS। Disk को नहीं छूता। | उपयोगकर्ता |
| **Borg Installed** | Windows / Linux / Android पर background service। Antivirus की तरह। | उपयोगकर्ता |
| **Borg Dedicated** | पुराना PC पूरी तरह समर्पित। कोई desktop नहीं। केवल Collective। | Collective |

> *"एक फोन मिनट योगदान कर सकता है। एक laptop घंटे योगदान कर सकता है। एक पुराना PC स्थायी node बन सकता है। सभी अपनी संभावनाओं के अनुसार भाग लेते हैं।"*

---

## न्यूनतम आवश्यकताएं

**Windows 7 या उच्चतर** चलाने में सक्षम hardware के लिए डिज़ाइन किया गया (2007 के बाद):

- x86/x64 CPU
- 512 MB RAM (1 GB अनुशंसित)
- इंटरनेट कनेक्शन
- Python 3.8+
- **कोई बाहरी निर्भरता नहीं** — केवल Python standard library

---

## स्थापना और पहला Node

```bash
# 1. Repository clone करें
git clone https://github.com/dominguezeddie/colectivo-borg.git
cd colectivo-borg

# 2. Executor node शुरू करें (Terminal 1)
python main.py

# 3. परीक्षण microtask भेजें (Terminal 2)
python emisor.py --texto "घर बहुत बड़ा था और उसमें बगीचा था।"
```

---

## रोडमैप (जैविक Milestones)

| Milestone | स्थिति | उद्देश्य |
|---|---|---|
| 🧬 **भ्रूण (Embryo)** | ✅ निर्माणाधीन | दो nodes जो protocol के साथ संवाद करते हैं |
| 🦠 **कोशिका (Cell)** | ⏳ प्रतीक्षित | तीन nodes, विभिन्न भूमिकाएं, basic failover |
| 🧵 **ऊतक (Tissue)** | ⏳ प्रतीक्षित | कार्यशील प्रतिष्ठा + पहला उपयोगी कार्य |
| 🫀 **अंग (Organ)** | ⏳ प्रतीक्षित | Bootable USB, portable cryptographic identity |
| 🌐 **जीव (Organism)** | ⏳ प्रतीक्षित | सार्वजनिक नेटवर्क, embedded OS, सक्रिय समुदाय |

---

## उत्पत्ति के बारे में

**Raúl Edmundo "Eddie" Domínguez** — La Consulta, Mendoza, Argentina.

Microprocessors में University-level Technician। 25 वर्ष WISP network operator के रूप में।

यह project किसी corporate laboratory से नहीं आया। यह field से आया है। मई 2026 में जन्मा।

स्वैच्छिक दान द्वारा समर्थित — Wikipedia / Linux model।

---

## लाइसेंस

**AGPL v3** — यह सभी का है, लेकिन किसी एक का नहीं।

---

*आत्मसात यहाँ से शुरू होता है।*
