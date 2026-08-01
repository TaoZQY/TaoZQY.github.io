---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
- Ph.D. Candidate, University of Science and Technology of China, Institute of Advanced Technology and Future Network Laboratory, 2023.09 - Present
- Bachelor's Degree, Chongqing University of Posts and Telecommunications, School of Communication and Information Engineering, 2019.09 - 2023.06

Research interests
======
- Efficient LLM inference serving and deployment
- AI infrastructure for heterogeneous GPU clusters
- Disaggregated serving, scheduling, and resource orchestration
- Multi-agent systems and communication-efficient collaboration
- Multimodal model efficiency and visual token pruning

Work experience
======
**Research Intern, Huawei 2012 Laboratories**
- Work on PTO optimization, focusing on dynamic and static graph construction on the Simpler side.
- Improve efficient computational graph construction and solving for system-level optimization workflows.
- Explore scheduling strategies for graph construction, graph solving, and high-throughput execution.

Research experience
======
**DisHelis: Serving Disaggregated Large Language Models over Heterogeneous Environments via Hierarchical Max-Flow**
- Studied resource allocation and model deployment for disaggregated LLM serving on heterogeneous GPU clusters.
- Modeled heterogeneous GPU compute, network bandwidth, and stage-level heterogeneity in disaggregated inference.
- Proposed a hierarchical max-flow-graph-based deployment algorithm and a lightweight redeployment mechanism for fluctuating online conditions.
- Evaluated against DistServe, HexGen2, Helix, and vLLM-style baselines.

**FAESR: Fine-Grained Rate Adaptation for Energy-Aware Super Resolution in Mobile Panoramic Video Streaming**
- Proposed a fine-grained bitrate adaptation method for neural-network-enhanced panoramic video streaming.
- Built a super-resolution power model from real-world measurements and formulated a joint QoE and energy-aware optimization problem.
- Developed a branch-sequence deep reinforcement learning algorithm for tile-level bitrate allocation.
- Publication: IEEE Transactions on Cognitive Communications and Networking, Early Access 2025, first author.

Honors
======
- National Scholarship, University of Science and Technology of China, 2025
- Graduate Academic First-Class Scholarship, University of Science and Technology of China, 2023 and 2024
- MathorCup National Undergraduate Mathematical Modeling Competition, National First Prize, 2022
- Outstanding Graduate of Chongqing Municipality, 2023
- Minister of Mobile Development Department, Hongyan Online School Workstation; Class Monitor, Excellent Engineer Class, 2020 - 2023
  
Skills
======
- Research: literature search with CNKI, IEEE Xplore, Google Scholar, GitHub, and related research resources
- Systems: LLM inference serving, scheduling, distributed databases, backend systems, traffic data processing
- Development: Web frontend/backend development and Android mobile application development
- Language: English reading and writing for professional literature; CET-4 and CET-6

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
