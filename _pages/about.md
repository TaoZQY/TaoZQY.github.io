---
layout: splash
permalink: /
title: "Tao Zhang"
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

<div class="minimal-scholar-home minimal-scholar-home--wide">
  <section class="scholar-hero" aria-labelledby="scholar-home-title">
    <div class="scholar-hero-copy">
      <p class="scholar-kicker">Ph.D. Candidate · Future Network Laboratory · USTC</p>
      <h1 id="scholar-home-title">Tao Zhang</h1>
      <p class="scholar-role">Efficient LLM Serving · AI Infrastructure · Multi-Agent Systems</p>
      <p class="scholar-lede">
        I study how modern AI systems can serve large language models faster and more efficiently across
        heterogeneous GPU clusters, disaggregated inference pipelines, networked workloads, and collaborative agents.
      </p>

      <div class="scholar-pills" aria-label="Research areas">
        <span>LLM Serving</span>
        <span>AI Infrastructure</span>
        <span>Disaggregated Systems</span>
        <span>KV Cache Reuse</span>
        <span>Multi-Agent Communication</span>
        <span>Multimodal Efficiency</span>
      </div>

      <div class="scholar-hero-actions" aria-label="Profile links">
        <a class="scholar-button scholar-button--primary" href="mailto:zhangtaolqy@mail.ustc.edu.cn">
          <i class="fas fa-envelope" aria-hidden="true"></i>
          <span>Email</span>
        </a>
        <a class="scholar-button" href="/publications/">
          <i class="fas fa-book-open" aria-hidden="true"></i>
          <span>Publications</span>
        </a>
        <a class="scholar-button" href="/cv/">
          <i class="fas fa-file-lines" aria-hidden="true"></i>
          <span>CV</span>
        </a>
        <a class="scholar-button" href="https://github.com/TaoZQY" target="_blank" rel="noopener">
          <i class="fab fa-github" aria-hidden="true"></i>
          <span>GitHub</span>
        </a>
      </div>
    </div>

    <aside class="scholar-identity-card" aria-label="Profile summary">
      <img class="scholar-portrait" src="/images/tao-zhang.jpg" alt="Tao Zhang portrait">
      <div class="scholar-card-body">
        <p class="scholar-card-name">Tao Zhang</p>
        <p>University of Science and Technology of China</p>
        <p>Future Network Laboratory · Hefei, China</p>
      </div>
    </aside>
  </section>

  <nav class="scholar-anchor-nav" aria-label="Homepage sections">
    <a href="#news">News</a>
    <a href="#experience">Experience</a>
    <a href="#publications">Publications</a>
    <a href="#skills">Skills</a>
    <a href="#interests">Interests</a>
    <a href="#education">Education</a>
    <a href="#honors">Honors</a>
  </nav>

  <section class="scholar-stats" aria-label="Publication highlights">
    <div>
      <strong>8</strong>
      <span>First/co-first papers</span>
    </div>
    <div>
      <strong>1</strong>
      <span>Oral paper</span>
    </div>
    <div>
      <strong>2</strong>
      <span>SCI Q1 journal papers</span>
    </div>
    <div>
      <strong>2026</strong>
      <span>CVPR · ACL · EMNLP · MM</span>
    </div>
  </section>

  <section class="scholar-section scholar-brief-grid" id="news">
    <div>
      <p class="section-label">About</p>
      <h2>Building systems for faster AI inference</h2>
      <p>
        I am a Ph.D. candidate at USTC Future Network Laboratory. My work connects
        AI infrastructure, distributed systems, and model-serving algorithms, with an emphasis on practical
        serving efficiency for LLM and multimodal workloads.
      </p>
    </div>
    <div>
      <p class="section-label">News</p>
      <ul class="news-list">
        <li><time>2026</time><span>Joined <strong>Huawei 2012 Laboratories</strong> as a research intern working on PTO optimization.</span></li>
        <li><time>2026</time><span><strong>SpecCache</strong> accepted by ACL 2026 as an oral paper.</span></li>
        <li><time>2026</time><span><strong>HAWK</strong>, <strong>SAVP</strong>, <strong>GSTEP</strong>, and <strong>LatCom</strong> accepted by CVPR, EMNLP, ACM Multimedia, and EMNLP.</span></li>
      </ul>
    </div>
  </section>

  <section class="scholar-section scholar-focus-section" id="research">
    <div class="scholar-section-heading">
      <p class="section-label">Research Focus</p>
      <h2>Serving systems for modern AI workloads</h2>
    </div>
    <div class="research-grid">
      <p>
        My research centers on efficient inference serving and AI infrastructure: resource scheduling for
        disaggregated LLM serving, KV-cache optimization for RAG, MoE training systems, multimodal token pruning,
        and communication-efficient multi-agent collaboration.
      </p>
      <ul class="research-list">
        <li><strong>DisHelis</strong><span>Deployment and resource allocation for heterogeneous disaggregated LLM serving.</span></li>
        <li><strong>SpecCache</strong><span>Speculative KV cache reuse for efficient RAG serving.</span></li>
        <li><strong>LatCom</strong><span>Latent compression for efficient multi-agent collaboration.</span></li>
      </ul>
    </div>
  </section>

  <section class="scholar-section" id="experience">
    <div class="scholar-section-heading">
      <p class="section-label">Internship Experience</p>
      <h2>Industry systems work</h2>
    </div>
    <div class="experience-card">
      <div class="experience-period">Current</div>
      <div class="experience-body">
        <h3>Research Intern, Huawei 2012 Laboratories</h3>
        <p class="experience-meta">PTO optimization · AI infrastructure systems</p>
        <ul>
          <li>Work on PTO optimization, focusing on dynamic and static graph construction on the Simpler side.</li>
          <li>Improve efficient computational graph construction and solving for system-level optimization workflows.</li>
          <li>Explore scheduling strategies for graph construction, graph solving, and high-throughput execution.</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="scholar-section" id="publications">
    <div class="scholar-section-heading">
      <p class="section-label">Selected Publications</p>
      <h2>First-author and co-first-author work</h2>
    </div>
    <div class="home-publications">
      <a href="/publication/dishelis">
        <span class="paper-index">01</span>
        <strong>DisHelis</strong>
        <span>IEEE TCCN · 2026 · First author · SCI 一区</span>
      </a>
      <a href="/publication/speccache">
        <span class="paper-index">02</span>
        <strong>SpecCache</strong>
        <span>ACL 2026 · 2026 · Co-first author · Oral</span>
      </a>
      <a href="/publication/hawk">
        <span class="paper-index">03</span>
        <strong>HAWK</strong>
        <span>CVPR 2026 · 2026 · Co-first author · Poster</span>
      </a>
      <a href="/publication/savp">
        <span class="paper-index">04</span>
        <strong>SAVP</strong>
        <span>EMNLP 2026 · 2026 · Co-first author · Poster</span>
      </a>
      <a href="/publication/gstep">
        <span class="paper-index">05</span>
        <strong>GSTEP</strong>
        <span>ACM Multimedia 2026 · 2026 · Co-first author · Poster</span>
      </a>
      <a href="/publication/latcom">
        <span class="paper-index">06</span>
        <strong>LatCom</strong>
        <span>EMNLP 2026 · 2026 · Co-first author · Poster</span>
      </a>
      <a href="/publication/multi-timescale-llm-serving">
        <span class="paper-index">07</span>
        <strong>Multi-Timescale Joint Optimization for Disaggregated LLM Serving</strong>
        <span>IEEE TCCN · 2026 · First author · SCI 二区</span>
      </a>
      <a href="/publication/faesr">
        <span class="paper-index">08</span>
        <strong>FAESR</strong>
        <span>IEEE TCCN · 2025 · First author · SCI 一区</span>
      </a>
    </div>
  </section>

  <section class="scholar-section scholar-two-column" id="skills">
    <div>
      <p class="section-label">Skills</p>
      <div class="skill-cloud" aria-label="Technical skills">
        <span>LLM serving</span>
        <span>AI infrastructure</span>
        <span>Disaggregated inference</span>
        <span>PTO optimization</span>
        <span>Computational graph construction</span>
        <span>Graph solving</span>
        <span>Scheduling</span>
        <span>Multimodal efficiency</span>
      </div>
    </div>
    <div id="interests">
      <p class="section-label">Research Interests</p>
      <div class="interest-matrix">
        <div>
          <strong>Serving Efficiency</strong>
          <span>Resource allocation, KV-cache reuse, and online scheduling for LLM serving.</span>
        </div>
        <div>
          <strong>AI Infra</strong>
          <span>Systems support for heterogeneous GPU clusters, graph optimization, and high-throughput execution.</span>
        </div>
        <div>
          <strong>Agents and Multimodal Models</strong>
          <span>Communication-efficient collaboration and visual-token pruning for efficient AI workloads.</span>
        </div>
      </div>
    </div>
  </section>

  <section class="scholar-section scholar-two-column">
    <div id="education">
      <p class="section-label">Education</p>
      <ul class="clean-list">
        <li><strong>Ph.D. Candidate</strong><span>University of Science and Technology of China, Institute of Advanced Technology and Future Network Laboratory, 2023.09 - Present</span></li>
        <li><strong>B.Eng.</strong><span>Chongqing University of Posts and Telecommunications, School of Communication and Information Engineering, 2019.09 - 2023.06</span></li>
      </ul>
    </div>
    <div id="honors">
      <p class="section-label">Recent Honors</p>
      <ul class="clean-list">
        <li><strong>National Scholarship</strong><span>University of Science and Technology of China, 2025</span></li>
        <li><strong>Graduate Academic First-Class Scholarship</strong><span>University of Science and Technology of China, 2023 and 2024</span></li>
        <li><strong>Outstanding Graduate</strong><span>Chongqing Municipality, 2023</span></li>
      </ul>
    </div>
  </section>
</div>
