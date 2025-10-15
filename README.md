# :robot::brain: Awesome Memory-Mechanism for Agent
The Memory-Mechanism in Agent Field can be devided to different kinds of memeory.
The repo provides a collection of **research papers on memory mechanisms for intelligent agents**.  

[![Awesome](https://awesome.re/badge.svg)](https://github.com/SiyuanWan99/Memory-Mechanism)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/license/MIT)
![Last Commit](https://img.shields.io/github/last-commit/SiyuanWan99/Memory-Mechanism)

## :star_struck::star_struck::star_struck: IntelliSense-Group @ BUPT 

[![Made with ❤️ at BUPT IntelliSense](https://img.shields.io/badge/Made%20with%E2%9D%A4%EF%B8%8F-BUPT%20IntelliSense-red.svg)](https://github.com/IntelliSensing)  

👋 Welcome to the **IntelliSense-Group @ Beijing University of Posts and Telecommunications (BUPT)**. 🚀🚀  
❤  We are a research group exploring the intersection of **remote sensing, intelligent agents**. 🛰🤖  
📚 Our repositories aim to serve as knowledge bases — mixing paper lists, research projects, and hands-on demos for curious minds. 🚀

---

## 🌟 What you’ll find here
- 📚 Curated paper lists and surveys  
- 🔧 Open-source implementations  
- 🧪 Demos, benchmarks, and reproducible experiments  

## 🙌 Join us
Feel free to **star ⭐, fork 🍴** — whether you are here to learn, share, or just explore.  
We believe that **science grows when knowledge is open**. Everyone is welcome to study, tinker, and contribute!  

---

## :books: Purpose of This Repository
This repository is a collection of academic papers, surveys, and implementations about **memory mechanisms in intelligent agents**. It aims to help researchers and practitioners quickly locate resources on how agents **store, recall, and utilize memory** for reasoning and decision-making.

---

## :rocket: How to Contribute
- Add contents of new papers follow the table line by line (arXiv, conferences, journals)  
- Share open-source implementations  
- Summarize novel memory mechanisms  

---

## :memo: Citation
If you find this repository helpful, please cite it or star the repo ⭐️.

# :brain: Memory Mechanisms in Agent Field — Paper Collection

> Below is a structured collection of papers categorized by memory mechanism.

---
## :star_struck: Review Paper
| Title | Author | Organization | Time | J/C | KeyWord | Category | Link|
|----------|------|------|------|---------------|--------|------|--------|
| A Survey on the Memory Mechanism of Large Language Model based Agents  | Zeyu Zhang | Renmin University of China | 2024 | Arxiv | Memory-Augmented NN, Agentg | Parametric | [PDF](https://arxiv.org/abs/2404.13501)|
| A Survey on LLM-based Multi-Agent Systems: Workflow, Applications, and Challenges | Xinyi Li | Wuhan University, China | 2024 | Vicinagearth, Springer  | Episodic Memory, Semantic Memory, Multi-Agent |All |[PDF](https://link.springer.com/article/10.1007/s44336-024-00009-2?utm_source=chatgpt.com#auth-Xinyi-Li-Aff1)|
| From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs | Yaxiong Wu | Huawei Noah’s Ark Lab | 2025 | Arxiv | Memory Mechanisms | Memory Mechanisms in the Era of LLMs | [PDF](https://arxiv.org/abs/2504.15965)|
| On the Structural Memory of LLM Agents | Ruihong Zeng | University of Glasgow | 2024 | Arxiv | Structural Memory | Structural Memory | [PDF](https://arxiv.org/abs/2412.15266)|
| Towards the next generation of Geospatial Artificial Intelligence | Mai | USA | 2025 | JAG | RemoteSensing/LongtermMem | LongtermMem | [PDF](https://www.sciencedirect.com/science/article/pii/S1569843225000159)|

---
###  🚀Personal × Non-param × Short → **Working Memory**
Conversation/task-level context, scratchpads, explicit reasoning traces (CoT), temporary notes, planning sketches.  
**📚 Paper List**
<!-- PNS:START -->
| Year | JC | Title | Key Idea | Keywords | Links |
|---|---|---|---|---|---|
| 2024 | arXiv | ChatGLM: A Family of Large Language Models from GLM-130B to GLM-4 All Tools | GLM model family evolution; tool-augmented capabilities | LLM, tools, Chinese | [PDF](https://arxiv.org/abs/2406.12793) |
| 2024 | arXiv | DeepSeek-V3 Technical Report | Large-scale MoE LLM with training/serving optimizations | LLM, MoE, training-opt, inference-opt | [PDF](https://arxiv.org/abs/2412.19437) |
| 2023 | arXiv | Gemini: A Family of Highly Capable Multimodal Models | Unified multimodal LLM family; strong parametric capabilities | LLM, multimodal | [PDF](https://arxiv.org/abs/2312.11805) |
| 2023 | Anthropic Blog | Introducing Claude | Production deployment of Claude; safety/alignment emphasis | LLM, alignment | [PDF](https://www.anthropic.com/index/introducing-claude) |
| 2023 | arXiv | Llama 2: Open Foundation and Fine-Tuned Chat Models | Open foundation + chat models; strong baseline parametric ability | LLM, open-source | [PDF](https://arxiv.org/abs/2307.09288) |
| 2023 | NeurIPS | OpenAssistant Conversations — Democratizing Large Language Model Alignment | Open crowdsourced alignment dataset for chat assistants | alignment, dataset | [Code](https://github.com/LAION-AI/Open-Assistant) |
| 2023 | arXiv | Qwen Technical Report | General-purpose LLM family; pretraining + alignment (SFT/RLHF) | LLM, bilingual | [PDF](https://arxiv.org/abs/2309.16609) |
| 2022 | OpenAI | Introducing ChatGPT | Large-scale parametric conversational ability; baseline context for memory discussions | LLM | [PDF](https://openai.com/blog/chatgpt) |
| 2022 | arXiv | Pangu-Bot: Efficient Generative Dialogue Pre-training from Pre-trained Language Model | Dialogue-oriented pretraining built on pretrained LMs | dialogue, pretraining | [PDF](https://arxiv.org/abs/2203.17090) |
<!-- PNS:END -->

---
### 🚀Personal × Non-param × Long → **Episodic Memory**
Cross-session experiences, task logs, reflections/summaries, “episode books.”  
**📚 Paper List**
<!-- PNL:START -->
| Year | JC | Title | Key Idea | Keywords | Links |
|---|---|---|---|---|---|
<!-- PNL:END -->

---

### 🚀Personal × Param × Short → **Inference-time Caches**
KV-cache, adapter/LoRA runtime states, short-horizon router statistics. 
**📚 Paper List**
<!-- PPS:START -->
| Year | JC | Title | Key Idea | Keywords | Links |
|---|---|---|---|---|---|
<!-- PPS:END -->

---

### 🚀Personal × Param × Long → **Semantic Memory**
Knowledge internalized in parameters: pretraining, continual fine-tuning, knowledge editing.  
**📚 Paper List**
<!-- PPL:START -->
| Year | JC | Title | Key Idea | Keywords | Links |
|---|---|---|---|---|---|
<!-- PPL:END -->

---

### 🚀System × Non-param × Short → **System-level Intermediates**
Blackboard/workspace artifacts, transient products from distributed planning/search.  
**📚 Paper List**
<!-- SNS:START -->
| Year | JC | Title | Key Idea | Keywords | Links |
|---|---|---|---|---|---|
| 2025 | arXiv | Optimus-2: Multimodal Minecraft Agent with Goal-Observation-Action Conditioned Policy | GOAP（Goal-Observation-Action Conditioned Policy）, MGOA Dataset | GOAP | [PDF](https://arxiv.org/pdf/2502.19902) |
| 2025 | arXiv | Optimus-3: Towards Generalist Multimodal Minecraft Agents with Scalable Task Experts | MoE |  | [PDF](https://arxiv.org/pdf/2506.10357) |
| 2024 | NeurIPS 2024 | Optimus-1: Hybrid Multimodal Memory-Empowered Agents Excel in Long-Horizon Tasks | Hybrid Multimodal Memory | Hybrid Multimodal Memory | [PDF](https://arxiv.org/pdf/2408.03615) |
<!-- SNS:END -->

---

### 🚀System × Non-param × Long → **Knowledge/Skill Bases**
RAG/vector stores, knowledge graphs, templates/playbooks, experience repositories & trajectory replay.  
**📚 Paper List**
<!-- SNL:START -->
| Year | JC | Title | Key Idea | Keywords | Links |
|---|---|---|---|---|---|
<!-- SNL:END -->

---

### 🚀System × Param × Short → **System-level Inference Caches**
Shared KV/index caches across agents, short-term router/gating states.  
**📚 Paper List**
<!-- SPS:START -->
| Year | JC | Title | Key Idea | Keywords | Links |
|---|---|---|---|---|---|
<!-- SPS:END -->

---

### 🚀System × Param × Long → **System-level Parametric Abilities**
MoE/routing, distilled long-term skills, system-wide capability pools.  
**📚 Paper List**
<!-- SPL:START -->
| Year | JC | Title | Key Idea | Keywords | Links |
|---|---|---|---|---|---|
<!-- SPL:END -->

---

## :spiral_calendar: Episodic Memory (Long-Term)
| Title | Author | Organization | Time | J/C | KeyWord | Category | Link|
|-------------|-----------|---------------------|------|---------------|-------------|--------|-------|
|Human-inspired Perspectives: A Survey on AI Long-term Memory| Zihong He  | X-Intelligence Labs | 2025 | Arxiv | Long-term Memory， | Long-term Memory | [PDF](https://arxiv.org/abs/2411.00489)|
|RS-RAG:Bridging Remote Sensing Imagery and  Comprehensive Knowledge with a Multi-Modal  Dataset and Retrieval-Augmented Generation Model| Congcong Wen  | University of Science and Technology of China | 2025 | Arxiv |RemoteSensing，RAG， | Non-Parametric | [PDF](https://arxiv.org/abs/2504.04988)| 

---

