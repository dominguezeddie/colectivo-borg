# Colectivo B.O.R.G.
### Benefit Optimization & Resource Grid
### *Rede de IA coletiva para os 60% esquecidos*

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-AGPL_v3-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/milestone-Embrião_🧬-yellowgreen.svg)]()
[![Hardware](https://img.shields.io/badge/hardware-2016_era_%2B-orange.svg)]()
[![Donate](https://img.shields.io/badge/Doar-Mercado_Pago-009ee3.svg)](https://link.mercadopago.com.ar/donaralcolectivoborg)

---

🌐 [Español](README.md) | [English](README.en.md) | **Português** | [हिन्दी](README.hi.md) | [中文](README.zh.md)

---

> *"A máquina é temporária. O Borg acompanha você."*
>
> *"A memória nunca é alienada — permanece no nó local do usuário.*  
> *A computação é socializada — a rede de pares a resolve.*  
> *O Borg é a identidade. O Coletivo é o músculo."*
>
> *"O Borg não precisa de ética declarada. Sua arquitetura aberta é a ética."*
>
> *"A resistência à obsolescência tecnológica é inútil. Junte-se ao Coletivo."*
>
> *"O mundo precisa de mais Borgs e menos data centers."*

---

## Terminal Borg — Interface Central

![Terminal Borg](https://raw.githubusercontent.com/dominguezeddie/colectivo-borg/main/Terminal%20Borg.png)

## Os Três Papéis da Célula-Mãe

![Diagrama dos Três Papéis](https://raw.githubusercontent.com/dominguezeddie/colectivo-borg/main/Diagrama%20de%20los%20Tres%20Roles.png)

---

## O que é o Colectivo Borg?

O **Colectivo Borg** é uma rede de inteligência artificial distribuída, open source e ecologicamente honesta, projetada para os **60% da humanidade** que não tem acesso real às IAs corporativas.

Não é uma empresa. Não tem acionistas. Não tem servidor central. Não tem termos de serviço que podem mudar amanhã.

É infraestrutura cognitiva coletiva — como a Wikipedia, mas para computação distribuída de IA.

---

## O Problema que Resolve

| Problema | Impacto real |
|---|---|
| **Consumo energético** | Um data center de IA consome tanta eletricidade quanto uma cidade média |
| **Monopólio corporativo** | 3-4 empresas decidem quem acessa e em quais condições |
| **Exclusão dos 60%** | Custo em moedas fortes, conectividade insuficiente, barreiras linguísticas e culturais |
| **Pedágio linguístico** | O espanhol consome **59% mais tokens** que o inglês — falantes não-ingleses pagam mais pelo mesmo resultado |

Quando as corporações racionam capacidade, os 60% percebem primeiro. O Borg resolve isso por design: **sem tokens, sem escassez, sem dono.**

---

## Arquitetura: Os Três Papéis da Célula-Mãe

### Sistema de Classificação

| Classificação | Score / RAM | Perfil |
|---|---|---|
| 🥇 **OURO** | Score ≥80 / RAM ≥4GB | Precisão constante e alta disponibilidade |
| 🥈 **PRATA** | Score 40-79 / RAM ≥2GB | Desempenho estável com desvios mínimos |
| 🥉 **BRONZE** | Score <40 / RAM <2GB | Hardware de baixos recursos — ainda contribui |

> *"A reputação é construída pela pessoa, não pelo hardware."*

---

## Hardware (Atualizado para 2026)

O Borg tem como alvo equipamentos fabricados entre **2016 e 2020** — máquinas que ainda circulam em escolas, bibliotecas, casas e cooperativas.

| Dispositivo | Requisito mínimo | RAM | Papel |
|---|---|---|---|
| Desktop / Laptop | 2015 em diante, CPU 64-bit | 4 GB | Executor, Agregador leve |
| Celular Android | 2018 em diante (Android 8+) | 3 GB | Executor móvel, nó itinerante |
| PC muito antigo (opcional) | 2010-2014, 2 GB RAM | 2 GB | Executor para microtarefas mínimas |

> *"Um celular pode contribuir minutos. Um notebook pode contribuir horas. Um PC antigo pode ser um nó permanente. Todos participam conforme suas possibilidades."*

### Base de Conhecimento Pré-carregada

O pendrive do Embrião inclui uma biblioteca portátil (<500 MB) com dicionários locais, manuais de agricultura, guias de primeiros socorros, documentação WISP e textos de domínio público. O primeiro nó tem valor imediato mesmo sem rede.

---

## Três Formas de Participar

| Modalidade | Descrição | Dono do dispositivo |
|---|---|---|
| **Borg Portátil** | Pendrive bootável. RootFS em RAM. Não toca o disco. Identidade portátil. | O usuário |
| **Borg Instalado** | Serviço em segundo plano no Windows / Linux / Android. Como um antivírus. | O usuário |
| **Borg Dedicado** | PC antigo totalmente dedicada. Sem área de trabalho. Sem ícones. Só o Coletivo. | O Coletivo |

---

## Instalação e Primeiro Nó

```bash
# 1. Clonar o repositório
git clone https://github.com/dominguezeddie/colectivo-borg.git
cd colectivo-borg

# 2. Iniciar o nó servidor (Terminal 1)
python embrion.py --modo servidor --identidad "no-1"

# 3. Enviar uma microtarefa de teste (Terminal 2)
python embrion.py --modo cliente --host localhost --mensagem "OLÁ BORG"
