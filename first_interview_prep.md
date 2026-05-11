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
5.  **Log Aggregation Pipeline (Observability)**:
    *   *Concept*: Deployed a localized ELK/EFK stack (Elasticsearch, Filebeat, Kibana) using docker-compose to ingest, parse, and centralize unstructured logs from multiple microservices.
    *   *Why it matters*: Demonstrates you understand how to make complex distributed systems **debuggable** across multiple nodes.
6.  **Rate Limiting Middleware (Traffic Management)**:
    *   *Concept*: Implemented a Redis-backed sliding window rate limiter in Python to protect a mock API from being overwhelmed by burst traffic.
    *   *Why it matters*: Proves you understand **capacity planning**, overload protection, and "load shedding."
7.  **Database Connection Pooler (Performance)**:
    *   *Concept*: Set up PgBouncer in front of a PostgreSQL database to handle thousands of incoming connection requests by queuing them, preventing the DB from crashing under high concurrency.
    *   *Why it matters*: Shows you understand **bottlenecks** and how to protect stateful layers from connection exhaustion.
8.  **Automated SSL Rotation Script (Security/Automation)**:
    *   *Concept*: Wrote a bash script that integrates with Let's Encrypt (Certbot), checks certificate expiration, auto-renews, and gracefully reloads the Nginx configuration without dropping active connections.
    *   *Why it matters*: Highlights the elimination of **toil** and preventing embarrassing, human-error outages.
9.  **Infrastructure as Code Sandbox (IaC)**:
    *   *Concept*: Wrote Terraform configurations to spin up a VPC, public/private subnets, an Auto-Scaling Group, and a Load Balancer, effectively treating infrastructure as version-controlled software.
    *   *Why it matters*: Proves you manage infrastructure **programmatically and reproducibly**.
10. **Network Traffic Analyzer (Networking)**:
    *   *Concept*: Developed a Python script using `tcpdump` and `scapy` to analyze packet captures, identifying sudden bandwidth spikes or unusual TCP retransmission rates.
    *   *Why it matters*: Shows you aren't afraid of the **network layer** and can debug issues below the application stack.

---

## 🚀 Deep Dive: Scalability & Architecture

When they ask about scalability, use these specific technical hooks:

*   **Decoupling & Asynchronous Processing**: *"In my projects, I rely on message brokers (like Kafka in the ARIEN project) to decouple ingestion from processing. This prevents bottlenecks and allows for horizontal scaling of consumer nodes."*
*   **State Management & Caching**: *"Scaling is fundamentally a state problem. I've worked on externalizing state into distributed caches (like Redis) so that worker nodes remain stateless. If a node fails, another can pick up immediately."*
*   **Edge Optimization**: *"I also understand resource constraints at the lowest level. For my thesis, I optimized a Deep Learning model to run on just 257KB of memory using TFLite. Understanding physical CPU and memory limits makes me a better capacity planner."*

---

## ❓ Deep-Dive Questions & Answers (Expanded)

### Q1: "Why Google Warsaw?"
**Choose the strategy that best fits the flow of the conversation:**
1.  **The Cloud Hub Strategy**: *"Warsaw is a massive hub for Google's Cloud Technical Infrastructure. I want to be surrounded by the 'engineers' engineers' who are building and maintaining the massive, massively distributed systems that power the internet."*
2.  **The Global Scale Strategy**: *"Warsaw teams manage infrastructure that impacts billions of users. The challenge of keeping European and global systems synchronized and highly available is incredibly appealing to me."*
3.  **The Talent Density Strategy**: *"I want to work with the absolute best. Warsaw is known for its high technical bar, and I want to be in an environment that constantly pushes my limits in systems engineering."*
4.  **The Systems Focus Strategy**: *"The Warsaw office has a reputation for focusing on the hardest, lowest-level infrastructure problems, rather than just product development, which perfectly aligns with my passion for OS internals and networking."*
5.  **The Research to Production Strategy**: *"Google Warsaw is famous for turning theoretical distributed systems research into production reality, mapping exactly to my background transitioning Horizon Europe research into scalable applications."*

### Q2: "What is your favorite Google product and why?"
**Choose a product that highlights infrastructure depth:**
1.  **Borg / Kubernetes**: *"I admire the architectural foresight of Borg. As an engineer, I’m fascinated by how it manages scheduling, resource allocation, and self-healing across thousands of machines, abstracting away hardware failures brilliantly."*
2.  **Cloud Spanner**: *"The way Spanner provides global consistency while maintaining horizontal scalability using TrueTime APIs is a masterclass in distributed consensus. It solves the CAP theorem trade-offs brilliantly."*
3.  **Bigtable**: *"It pioneered how we think about NoSQL column-family stores. Managing petabytes with high throughput and low latency is the foundation of scalable SRE thinking."*
4.  **Colossus (Google File System)**: *"It fascinates me how Google handles disk failures as a normal, expected occurrence, abstracting the unreliability of cheap commodity hardware into a highly reliable storage layer."*
5.  **Google VPC/Jupiter Network**: *"The software-defined networking approach is incredible. The fact that Google built its own custom data-center network switches to achieve massive bisection bandwidth is pure engineering excellence."*

### Q3: "Why SRE specifically?"
**Choose the angle that best fits your personality:**
1.  **The Bulletproof Systems Strategy**: *"Most engineers want to push new features, but I find my greatest satisfaction in making systems bulletproof. I love the detective work of debugging complex latency spikes across the network stack."*
2.  **The Automation Obsession Strategy**: *"I despise doing the same manual task twice. SRE empowers me to treat operational toil as an engineering problem that can be permanently eliminated with code."*
3.  **The Crisis Management Strategy**: *"I actually enjoy the pressure of incident response. There's a unique satisfaction in methodically triaging a critical failure and restoring service under high pressure."*
4.  **The Cross-Functional Strategy**: *"SREs get to see the entire stack. Instead of being siloed in one microservice, SREs understand how the network, the OS, the database, and the application all interact."*
5.  **The Advocate for the User Strategy**: *"At the end of the day, reliability is the most important feature. If a system is down, the best UI/UX doesn't matter. I want to be the guardian of that reliability."*

---

## 🛡️ Handling Technical "I Don't Know"

If they hit you with a hard system design, Linux, or networking question you haven't reviewed yet:
1.  **Don't Panic**: SREs deal with the unknown every day. Google cares more about your *troubleshooting process*.
2.  **State your assumptions**: *"Assuming this is a standard TCP handshake issue..."*
3.  **Think out loud / Debug logically**: *"I haven't used that specific tool, but my first step would be to check `dmesg` or `syslog` for kernel panics, then run `strace` on the process to see where the system calls are hanging."*

---

## 🛠️ Preparation Checklist & Answers

### 1. Technical Readiness (How to mention it)
**Script**: *"I've been heavily focused on deepening my SRE fundamentals. Currently, my daily routine involves solving Advanced DSA problems to keep my algorithmic thinking sharp, while simultaneously diving deep into Linux Internals—like kernel tracing and file systems—and networking fundamentals like TCP/IP congestion control and DNS resolution at scale."*

### 2. Portfolio Walkthrough (2 STAR Stories for Troubleshooting/Scaling)

**Story 1: FNOMCeO Transactional Bottlenecks (Scalability)**
*   **Situation**: We were architecting the national registry for 460,000+ medical professionals.
*   **Task**: We needed to run heavy analytical reporting without locking up the primary transactional database during peak traffic.
*   **Action**: I assessed the "as-is" architecture and designed a decoupled "to-be" cloud architecture. I implemented a distributed cache and routed all reporting queries to a dedicated read-replica.
*   **Result**: This completely segregated analytical traffic from transactional traffic, preventing database locks and ensuring high availability and consistent low latency at a national scale.

**Story 2: ARIEN Pipeline Decoupling (Fault Tolerance)**
*   **Situation**: We were ingesting highly sensitive, high-throughput financial and security data streams for a European AI security initiative.
*   **Task**: The Python AI analytics engine occasionally experienced processing latency spikes, which risked dropping real-time data packets.
*   **Action**: I architected an asynchronous data ingestion pipeline by introducing a Kafka message broker between the raw data streams and the AI processing engine.
*   **Result**: The message queue safely buffered the data during AI processing spikes, ensuring zero data loss and allowing us to horizontally scale the Python consumer nodes independently.

### 3. Role-Specific Knowledge (SRE Definitions)
*   **SLI (Service Level Indicator)**: A quantitative measure of some aspect of the level of service provided. It's the actual metric you are measuring. *(Example: The percentage of HTTP GET requests that return a 200 OK within 100ms).*
*   **SLO (Service Level Objective)**: A target value or range of values for a service level that is measured by an SLI. It's the internal engineering goal. *(Example: 99.9% of all requests in a rolling 30-day window must meet the SLI).*
*   **SLA (Service Level Agreement)**: An explicit or implicit contract with your users that includes consequences if the SLO is missed. It's the business contract. *(Example: If uptime drops below 99.9%, we refund enterprise customers).*
*   **Error Budget**: The allowable threshold for failure (100% minus the SLO). If your SLO is 99.9%, your error budget is 0.1%. SREs use this to balance reliability with feature velocity. *(Example: If we exhaust the 0.1% error budget, all new feature pushes are frozen until reliability is restored).*

---

## 💡 Final Tip
The first call is about **Energy**, **Conviction**, and **Engineering Maturity**. You aren't just a coder; you are a systems architect who loves taking things apart to see how they work. Make them feel your passion for the SRE culture.
