# Colectivo B.O.R.G.
### Benefit Optimization & Resource Grid
### *为被遗忘的60%人类而生的分布式AI集体*

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-AGPL_v3-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/milestone-胚胎_🧬-yellowgreen.svg)]()
[![Hardware](https://img.shields.io/badge/hardware-2016时代_%2B-orange.svg)]()
[![Donate](https://img.shields.io/badge/捐款-Mercado_Pago-009ee3.svg)](https://link.mercadopago.com.ar/donaralcolectivoborg)

---

🌐 [Español](README.md) | [English](README.en.md) | [Português](README.pt.md) | [हिन्दी](README.hi.md) | **中文**

---

> *"机器是短暂的。Borg与你同行。"*
>
> *"记忆永远不会被异化——它保留在用户的本地节点上。*  
> *计算被社会化——对等网络解决它。*  
> *Borg是身份。集体是肌肉。"*
>
> *"Borg不需要声明的道德准则。其开放架构本身就是道德。"*
>
> *"抵制技术淘汰是徒劳的。加入集体吧。"*
>
> *"世界需要更多Borg，更少数据中心。"*

---

## Terminal Borg — 中央界面

![Terminal Borg](https://raw.githubusercontent.com/dominguezeddie/colectivo-borg/main/Terminal%20Borg.png)

## 母细胞的三个角色

![三个角色图示](https://raw.githubusercontent.com/dominguezeddie/colectivo-borg/main/Diagrama%20de%20los%20Tres%20Roles.png)

---

## 什么是Colectivo Borg？

**Colectivo Borg** 是一个分布式、开源且对生态负责的人工智能网络，专为**全球60%**无法真正使用企业AI的人而设计。

它不是公司。没有股东。没有中央服务器。没有可能随时更改的服务条款。

它是集体认知基础设施——就像维基百科，但用于分布式AI计算。

---

## 它解决的问题

| 问题 | 实际影响 |
|---|---|
| **能源消耗** | 一个AI数据中心消耗的电力相当于一座中等城市 |
| **企业垄断** | 3-4家公司决定谁能访问以及在什么条件下访问 |
| **60%被排除** | 强势货币成本、网络连接不足、语言和文化障碍 |
| **语言税** | 西班牙语比英语多消耗**59%的token**——非英语用户为相同结果支付更多 |

当企业开始配给算力时，那60%的人首先感受到。Borg通过设计解决了这个问题：**无token，无稀缺，无所有者。**

---

## 架构：母细胞的三个角色

### 排名系统

| 排名 | 分数 / 内存 | 简介 |
|---|---|---|
| 🥇 **黄金** | 分数≥80 / 内存≥4GB | 持续精准，高可用性 |
| 🥈 **白银** | 分数40-79 / 内存≥2GB | 稳定表现，偏差最小 |
| 🥉 **青铜** | 分数<40 / 内存<2GB | 低资源硬件——仍然贡献 |

> *"声誉由人构建，而非由硬件构建。"*

---

## 硬件（2026年更新）

Borg的目标设备是**2016年至2020年**期间制造的——那些仍在学校、图书馆、家庭和合作社中运行的机器。

| 设备 | 最低要求 | 内存 | 角色 |
|---|---|---|---|
| 台式机 / 笔记本 | 2015年起，64位CPU | 4 GB | 执行者，轻量聚合者 |
| Android手机 | 2018年起（Android 8+） | 3 GB | 移动执行者，移动节点 |
| 很旧的电脑（可选） | 2010-2014，2 GB内存 | 2 GB | 最小微任务的执行者 |

> *"手机可以贡献几分钟。笔记本可以贡献几小时。旧电脑可以成为永久节点。每个人根据自己的能力参与。"*

### 预加载知识库

胚胎U盘包含一个便携式库（<500 MB），其中有本地词典、农业手册、急救指南、WISP文档和公共领域文本。第一个节点即使没有网络也有即时价值。

---

## 三种参与方式

| 方式 | 描述 | 设备所有者 |
|---|---|---|
| **便携式Borg** | 可启动U盘。RAM上的RootFS。不触碰硬盘。便携身份。 | 用户 |
| **已安装Borg** | Windows / Linux / Android上的后台服务。像杀毒软件一样。 | 用户 |
| **专用Borg** | 完全用于集体的旧电脑。没有桌面。没有图标。只有集体。 | 集体 |

---

## 安装和第一个节点

```bash
# 1. 克隆仓库
git clone https://github.com/dominguezeddie/colectivo-borg.git
cd colectivo-borg

# 2. 启动服务器节点（终端1）
python embrion.py --modo servidor --identidad "节点-1"

# 3. 发送测试微任务（终端2）
python embrion.py --modo cliente --host localhost --mensaje "你好 BORG"
