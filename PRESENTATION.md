# 🎤 Interview Presentation — Google Site Reliability Engineer (SRE)

> A structured presentation framework for positioning yourself as a strong candidate.
> Customize each section with your real experience and projects.

---

## Slide 1: Profile Summary

### [Your Name] — Software Engineer / SRE

**Headline**: Software Engineer with hands-on experience scaling distributed backends, systems programming, and building robust, resilient cloud-native applications.

**Key Facts**:
- 🎓 [Your Degree] in [Your Field] from [Your University]
- 💼 [X] years of professional software engineering experience
- 🐍 Primary languages: Python, Go, Java
- 🛡️ Focused on reliability, fault tolerance, and systems internals
- 🌐 Open-source contributor and automation builder
- ☁️ Experience with cloud platforms (GCP/AWS/Azure)

> **Customize**: Replace brackets with your real information. Keep it concise — this is the 30-second elevator pitch.

---

## Slide 2: Why This Google Role Fits Me

### The Role: Site Reliability Engineer (SRE)

This role asks for someone who can:
1. **Improve system reliability and availability** for Google services
2. **Automate operational work (toil)** by writing software pipelines and systems
3. **Troubleshoot complex systems outages** under pressure (kernel, network, storage)
4. **Design robust observability** and telemetry monitoring systems

### Why It's a Perfect Match

| Role Requirement | My Background |
|-----------------|---------------|
| Software development & automation | [Your experience building high-quality backend software and scripts] |
| Distributed systems debugging | [Your experience identifying memory leaks, network socket errors, kernel bottlenecks] |
| Cross-functional collaboration | [Examples of working with different teams/stakeholders] |
| Cloud deployment (GCP) | [Your cloud experience — GKE, VPCs, VM scaling, and Cloud Run] |
| Observability & reliability practices | [Your experience with metrics dashboards (Prometheus/Grafana), SLOs, post-mortems] |

### My Unique Angle
> "I bring a combination of backend software engineering, systems programming, and infrastructure management that directly maps to Google SRE. I understand both the systems engineering side (kernel, networking, OS internals) and the software design side (how to build clean, maintainable automation tools)."

---

## Slide 3: Relevant Experience

### Professional Experience

**Role 1: [Most Relevant Job Title]** — [Company], [Date Range]
- [Achievement that maps to SDK/tooling development]
- [Achievement that maps to AI/agent work]
- [Achievement that maps to collaboration or cloud deployment]
- **Impact**: [Quantified result — users served, performance improvement, etc.]

**Role 2: [Second Most Relevant]** — [Company], [Date Range]
- [Key achievement 1]
- [Key achievement 2]
- **Impact**: [Quantified result]

### Key Projects

**Project: [Systems/Reliability Project Name]**
- **What**: [1-sentence description — e.g. national registry supporting 460K+ users]
- **Tech Stack**: Python, Java/Spring, Kubernetes, AWS/GCP, Prometheus
- **Impact**: [What it achieved — e.g. 99.9% uptime, reduced manual deployment tasks by 60%]
- **Relevance to Role**: [Direct connection to systems reliability/automation]

> **Tip**: Order experiences by relevance to the role, not by date. The most relevant experience should come first, even if it was a side project.

---

## Slide 4: Relevant Technical Skills

### Skills Matrix

| Category | Skills | Proficiency | Relevance to Role |
|----------|--------|-------------|-------------------|
| **Languages** | Python, Go, C++, Java | ⭐⭐⭐⭐⭐ | Core — Automation & systems coding |
| **OS & Systems** | Linux Internals, Sockets, Processes, Memory | ⭐⭐⭐⭐ | Critical — debugging & performance tuning |
| **Infrastructure** | Kubernetes, Docker, Terraform | ⭐⭐⭐⭐ | Direct — managing workloads at scale |
| **Observability** | Prometheus, OpenTelemetry, Grafana, Jaeger | ⭐⭐⭐⭐ | Key — metrics, alerting, tracing |
| **Networking** | TCP/IP, HTTP/2, gRPC, DNS, Load Balancers | ⭐⭐⭐⭐ | Core — troubleshooting connections |
| **System Design** | Distributed systems, Consensus (Raft), Replication | ⭐⭐⭐⭐ | Important — architecture design |

### Technical Depth: SRE & Systems Reliability Stack

```
┌─────────────────────────────────────────────────┐
│                Application Layer                │
│       Microservices, APIs, Business Logic       │
├─────────────────────────────────────────────────┤
│               Orchestration Layer               │
│       Kubernetes, Docker, Cloud Run, GKE        │
├─────────────────────────────────────────────────┤
│              Observability Layer                │
│       Prometheus, OpenTelemetry, Grafana        │
├─────────────────────────────────────────────────┤
│               Infrastructure Layer              │
│        Linux OS, Sockets, Compute, Storage      │
└─────────────────────────────────────────────────┘
```

> I have experience across all layers, with deepest expertise in the orchestration and infrastructure layers.

---

## Slide 5: Projects Aligned with Site Reliability Engineering

### Project 1: [National-Scale Registry Reliability (FNOMCeO)]
- **Description**: Spearheaded reliability improvements for a national registry supporting 460K+ users.
- **Architecture**: Microservices on Spring Boot / Angular, deployed with high availability configurations, auto-scaling, and health check alerts.
- **Technologies**: Java, Spring, AWS, Docker, Kubernetes, Prometheus, Grafana
- **Key Challenges Solved**:
  - Eliminated high latency during morning peak hours by introducing intelligent database indexing and a Redis caching layer.
  - Automated deployment rollbacks when new releases failed health checks.
- **Relevance**: Directly demonstrates the ability to manage reliability and scale for real-world national services.

### Project 2: [SRE Automation / Cleanup Operator]
- **Description**: Built an automated toil-reduction tool that continuously inspects and cleans up orphaned cloud assets, temporary logs, and idle Docker containers.
- **Architecture**: A Python-based CLI / Cron operator that connects to GCP/Kubernetes API, checks resource usage, runs diagnostic tests, and performs safe, alert-triggered purges.
- **Technologies**: Python, Kubernetes API, Docker, GCP, CI/CD
- **Relevance**: Highlights automation first mindset and coding skills to reduce operational toil.

### Project 3: [Distributed Metrics Exporter & Alert Engine]
- **Description**: Developed a custom monitoring pipeline that scrapes application metrics, aggregates request counts/latencies, and fires alerts based on dynamic error budgets.
- **Technologies**: Go, Prometheus, Alertmanager, Docker, Slack API
- **Relevance**: Demonstrates hands-on capabilities in building observability tools, defining SLIs/SLOs, and designing effective symptom-based alerting.

> **Tip**: If you don't have all 3 projects yet, use Week 5 to build a strong ADK-based project. Having a real, deployed project to discuss in the interview is a massive advantage.

---

## Slide 6: Gaps and Improvement Areas

### Honest Self-Assessment

| Gap | Current Level | Target Level | Mitigation Plan |
|-----|--------------|-------------|-----------------|
| Google SRE production models | Beginner | Intermediate | Week 5 SRE Book deep dive + practice |
| Distributed systems design | Intermediate | Strong | Week 4 practice + 5 mock designs |
| Linux kernel & tracing tools | Intermediate | Strong | System monitoring projects, study strace/lsof |
| Hard LeetCode problems | ~30% success | ~50% success | Daily practice, focus on DP and graphs |
| GKE & GCP infrastructure | Intermediate | Strong | Hands-on with GKE, configure custom ingress |

### How I'm Addressing Each Gap

1. **SRE Models**: Studying the official Google SRE books and workbook, focusing on SLIs/SLOs and post-mortem best practices
2. **System Design**: Following the 7-day system design plan in this repo, focusing on high availability, rate limiting, and metrics systems
3. **Linux Tracing**: Practicing tracing application system calls (`strace`) and listing network connection sockets (`lsof`) under load
4. **DSA**: Solving 15+ LeetCode problems per week, focusing on graphs, heaps, and tree traversals
5. **GKE/GCP**: Deploying GKE test workloads, setting up Prometheus metric scraping and autoscalers (HPA)

> **Why this section matters**: Google values self-awareness and growth mindset. Showing you know your gaps AND have a plan to close them is a strong signal.

> **Why this section matters**: Google values self-awareness and growth mindset. Showing you know your gaps AND have a plan to close them is a strong signal.

---

## Slide 7: Preparation Roadmap

### 6-Week Plan

```
Week 1: DSA Foundations
├── Arrays, HashMaps, Two Pointers, Sliding Window
├── Stacks, Queues, Linked Lists
└── 30+ LeetCode problems

Week 2: Intermediate DSA
├── Binary Search, Trees, Heaps
├── Recursion, Backtracking, Sorting
└── 30+ LeetCode problems

Week 3: Advanced DSA
├── Graphs (BFS, DFS, Dijkstra)
├── Dynamic Programming (1D + 2D)
├── Tries, Greedy Algorithms
└── 25+ LeetCode problems (including Hards)

Week 4: System Design
├── Distributed Systems, Databases
├── Global Rate Limiter, Distributed Tracing
├── Metrics & Alerting, Cloud Resiliency
└── 6 system design practice sessions

Week 5: SRE & Systems Engineering (Role-Specific)
├── Linux Internals, Systems Debugging
├── SLOs, SLAs, Error Budgets, Toil Reduction
├── Infrastructure Automation, Incident Management
└── Observability & Alert Rules, SRE Mock Project

Week 6: Behavioral & Final
├── STAR Stories, Googleyness prep
├── Mock Interviews (Coding + SD + Behavioral)
├── Portfolio finalization
└── Application submission
```

### Daily Commitment: 3-4 hours focused study

---

## Slide 8: Interview Strategy

### Coding Interview
- **Approach**: Clarify → Brute Force → Optimize → Code → Test
- **Communication**: Think out loud, explain trade-offs, invite feedback
- **Time Management**: 5 min clarify, 5 min approach, 20 min code, 5 min test
- **Strengths to Leverage**: [Your strongest patterns — e.g., "Strong at graph and tree problems"]
- **Risk Areas**: [Your weakest — e.g., "Need more practice on DP"] → mitigation plan in place

### System Design Interview
- **Approach**: Requirements → Estimation → High-Level → Deep Dive → Trade-offs
- **Communication**: Draw diagrams, discuss alternatives, quantify decisions
- **Edge**: Focus on non-functional requirements (fault tolerance, high availability, load shedding)
- **Preparation**: Practiced 10+ system designs, 3 SRE-specific

### Behavioral Interview
- **Approach**: STAR method with quantified impact
- **Stories Ready**: 10 stories covering: leadership, collaboration, conflict, failure, growth, impact
- **Googleyness**: Prepared for "doing the right thing", navigating ambiguity, and blamelessness
- **Questions for Interviewer**: 5+ specific questions about SRE practices, tooling, and post-mortems

### Interview Day Plan
1. ✅ Arrive/connect 15 minutes early
2. ✅ Have water, notepad, and this cheat sheet ready
3. ✅ Start every problem by clarifying constraints
4. ✅ Think out loud — silence is your enemy
5. ✅ Ask if the interviewer has questions → show engagement
6. ✅ End with thoughtful questions about SRE culture

---

## Slide 9: Final Positioning

### Why Hire Me?

**The Short Version**:
> "I'm a software engineer who combines strong CS fundamentals in data structures and algorithms with hands-on experience designing and operating national-scale backends. I've built automation to reduce toil, I understand system behavior from the application level down to the Linux kernel, and I'm deeply motivated by SRE principles of engineering reliability into large-scale systems."

### Three Things That Set Me Apart

1. **Systems & Software Balance**: I don't just write scripts — I write clean, structured software to automate infrastructure and resolve complex failure modes.
2. **National-Scale Uptime**: I have experience keeping systems up for nearly half a million active users (FNOMCeO), meaning I know what it means when downtime is not an option.
3. **Stamina & Autonomy**: Balancing full-time engineering and research roles with academic success proves I can learn fast and execute under high-pressure scenarios.

### My Ask
> "I want to be part of the team that ensures Google's global scale services remain highly available and reliable. I want to contribute my software engineering background to automate toil and build next-generation SRE tooling."

---

## 📝 Presentation Tips

1. **Be Specific**: Replace every placeholder with your real data. Generic answers fail.
2. **Tell Stories**: Each slide should have a concrete example or story behind it.
3. **Show Passion**: Your excitement about agents and developer tooling should be visible.
4. **Be Honest About Gaps**: Google values self-awareness. Don't pretend to know everything.
5. **Practice**: Run through this presentation 3 times before your interview.
6. **Adapt**: You won't present all slides — use them as mental frameworks for answering questions.

---

## 🎯 Key Messages to Weave In

Throughout any interview, consistently reinforce these messages:

- ✅ "I automate toil" → Highlight automation scripts and toil-reduction tools
- ✅ "I understand system reliability" → Mention SLIs, SLOs, and Error Budgets
- ✅ "I debug systematically" → Describe tracing process down the network stack and OS internals
- ✅ "I understand enterprise scale" → Mention microservice HA patterns, VPCs, GKE, rate limiters
- ✅ "I'm a strong collaborator" → Reference cross-functional projects and blameless culture
- ✅ "I'm ready for Google SRE" → Preparation plan demonstrates commitment and systems depth
