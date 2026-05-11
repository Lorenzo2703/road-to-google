# 📞 First Interview Call: Strategy & Script

This document is your high-level strategy for the initial recruiter/hiring manager screening. The goal is to establish **authority**, **technical depth**, and **role-specific passion** right from the start for the Google Warsaw SRE position.

---

## 🎯 Core Objectives
1. **Convince them of Technical Excellence**: Show that your coding and Linux fundamentals are rock-solid.
2. **Demonstrate an "Engineer's Engineer" Mindset**: Prove you treat operations as a software problem and love "voiding warranties" to see how things work.
3. **Showcase Drive & Infrastructure PoCs**: Highlight your ability to build automation tools from 0 to 1 to reduce toil.
4. **Highlight Grit**: Managing a full-time job while graduating proves you can handle the intensity and pressure of Google SRE incident response.

---

## 🗣️ Key Talking Points

### 1. The "Engineer's Engineer" Narrative
*"I don't just want to build features; I want to understand what happens to the code when it hits the metal. My background blends deep software engineering with complex cloud architectures (like FNOMCeO). I treat operations and reliability as software optimization problems, striving to eliminate manual toil through code."*

### 2. The Infrastructure PoC Track Record
*"To constantly sharpen my skills, I build small, focused Proof of Concepts (PoCs). This has taught me how to design for **scalability and resilience** from Day 1. Instead of just reading about observability or orchestration, I build local Kubernetes clusters, write custom metric exporters, and script self-healing daemons. It proves I have a hands-on, builder's approach to infrastructure."*

### 3. The "Grit" Factor
*"I have a high capacity for work and rapid learning. I balanced full-time software engineering roles while finishing my degrees. This forced me to master time management, technical focus under pressure, and prioritizing impact over busy-work—traits that are essential during critical, high-stakes incident responses."*

---

## 🛠️ Simple but Effective SRE PoCs to Discuss

Be ready to describe these simple PoCs as evidence of your hands-on SRE skills:

1.  **Automated Self-Healing Daemon (Linux/Python)**: 
    *   *Concept*: Wrote a lightweight Python daemon that monitors specific systemd services (or Docker containers). If memory spikes above 90% or the process hangs, the script automatically captures a stack trace (for blameless postmortems) and safely restarts the service.
    *   *Why it matters*: Shows you understand **toil reduction** and **automated remediation**.
2.  **Custom Prometheus Exporter (Observability)**:
    *   *Concept*: Built a custom `/metrics` endpoint in Python/Flask that exposes custom business logic metrics (e.g., "active financial flows tracking" for the ARIEN project) so it could be scraped by Prometheus and visualized in Grafana.
    *   *Why it matters*: Proves you know how to build **telemetry** and create actionable alerts (SLIs/SLOs) rather than just reading generic CPU/RAM graphs.
3.  **Local Chaos Engineering Script (Resilience)**:
    *   *Concept*: A bash script running on a cron job that randomly kills one of three redundant web-server containers to test if the load balancer correctly reroutes traffic without dropping user requests.
    *   *Why it matters*: Demonstrates a proactive approach to **fault tolerance** and "designing for failure."
4.  **Zero-Downtime Deployment Pipeline (CI/CD)**:
    *   *Concept*: Set up a GitHub Action that builds a Docker image and performs a Rolling Update on a local cluster, ensuring there is never a moment where the service is completely down during a rollout.
    *   *Why it matters*: Shows you prioritize **uptime appropriate to customer needs**.

---

## 🚀 Deep Dive: Scalability & Architecture

When they ask about scalability, use these specific technical hooks:

*   **Decoupling & Asynchronous Processing**: *"In my projects, I rely on message brokers (like Kafka in the ARIEN project) to decouple ingestion from processing. This prevents bottlenecks and allows for horizontal scaling of consumer nodes."*
*   **State Management & Caching**: *"Scaling is fundamentally a state problem. I've worked on externalizing state into distributed caches (like Redis) so that worker nodes remain stateless. If a node fails, another can pick up immediately."*
*   **Edge Optimization**: *"I also understand resource constraints at the lowest level. For my thesis, I optimized a Deep Learning model to run on just 257KB of memory using TFLite. Understanding physical CPU and memory limits makes me a better capacity planner."*

---

## ❓ Deep-Dive Questions & Answers (Expanded)

### Q1: "Why Google Warsaw?"
**The Strategy**: Connect the specific office culture with your goals.
*   *"Warsaw is a massive hub for Google's Cloud Technical Infrastructure. I want to be surrounded by the 'engineers' engineers' who are building and maintaining the massive, massively distributed systems that power the internet. The focus on deep technical problems and a blameless postmortem culture is exactly where I thrive."*

### Q2: "What is your favorite Google product and why?"
**The Strategy**: Go deeper into the infrastructure.
*   **Example**: *Borg / Kubernetes*. *"I admire the architectural foresight of Borg (and subsequently Kubernetes). As an engineer, I’m fascinated by how it manages scheduling, resource allocation, and self-healing across thousands of machines. It fundamentally changed how we think about deploying software and abstracts away hardware failures brilliantly."*

### Q3: "Why SRE specifically?"
**The Strategy**: Position yourself as passionate about reliability.
*   *"Most engineers want to push new features, but I find my greatest satisfaction in making systems bulletproof. I love the detective work of debugging complex latency spikes across the network stack, and the satisfaction of writing automation that eliminates a recurring problem forever. I want to build systems that don't just work, but work reliably at massive scale."*

---

## 🛡️ Handling Technical "I Don't Know"

If they hit you with a hard system design, Linux, or networking question you haven't reviewed yet:
1.  **Don't Panic**: SREs deal with the unknown every day. Google cares more about your *troubleshooting process*.
2.  **State your assumptions**: *"Assuming this is a standard TCP handshake issue..."*
3.  **Think out loud / Debug logically**: *"I haven't used that specific tool, but my first step would be to check `dmesg` or `syslog` for kernel panics, then run `strace` on the process to see where the system calls are hanging."*

---

## 🛠️ Preparation Checklist
- [ ] **Technical Readiness**: Mention you've been reviewing Advanced DSA, Linux Internals, and Networking (TCP/IP, DNS).
- [ ] **Portfolio Walkthrough**: Have 2 specific stories ready for the "Tell me about a time you troubleshooted a complex distributed issue" question.
- [ ] **Role-Specific Knowledge**: Be able to explicitly define SLIs, SLOs, SLAs, and Error Budgets.

---

## 💡 Final Tip
The first call is about **Energy**, **Conviction**, and **Engineering Maturity**. You aren't just a coder; you are a systems architect who loves taking things apart to see how they work. Make them feel your passion for the SRE culture.
