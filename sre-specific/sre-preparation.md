# 🛠️ SRE Preparation Guide

> Deep dive into Google Site Reliability Engineering for interview preparation.

---

## What is Google SRE?

Site Reliability Engineering (SRE) is what happens when you ask a software engineer to design an operations function. At Google, SREs are responsible for the availability, latency, performance, efficiency, change management, monitoring, emergency response, and capacity planning of Google's services.

### Core Pillars
1.  **Embracing Risk**: Managing reliability through Error Budgets.
2.  **Service Level Objectives (SLOs)**: Defining and measuring reliability.
3.  **Eliminating Toil**: Automating repetitive, manual tasks.
4.  **Monitoring Distributed Systems**: Identifying and alerting on failures.
5.  **The Evolution of Automation**: Moving from scripts to self-healing systems.
6.  **Release Engineering**: Consistent and reliable deployments.
7.  **Simplicity**: Reducing systemic complexity.

---

## Must-Read Resources
- **The SRE Book**: [sre.google/sre-book/table-of-contents](https://sre.google/sre-book/table-of-contents/)
- **The SRE Workbook**: [sre.google/workbook/table-of-contents](https://sre.google/workbook/table-of-contents/)
- **Building Secure & Reliable Systems**: [sre.google/static/pdf/building_secure_and_reliable_systems.pdf](https://sre.google/static/pdf/building_secure_and_reliable_systems.pdf)

---

## Key SRE Concepts to Master

### 1. The Error Budget
- $Error\ Budget = 100\% - SLO$
- If the SLO is 99.9%, the error budget is 0.1%.
- When the budget is exhausted, releases are halted until reliability is restored.

### 2. The Four Golden Signals
- **Latency**: The time it takes to service a request.
- **Traffic**: A measure of how much demand is being placed on your system.
- **Errors**: The rate of requests that fail.
- **Saturation**: How "full" your service is.

### 3. Incident Management
- **The On-Call Loop**: Triage, Mitigate, Resolve.
- **Blameless Postmortems**: Focus on system failures, not human error.
- **MTTR (Mean Time To Repair)**: The critical metric for SRE success.

### 4. NALSD (Non-Abstract Large System Design)
- Designing for specific scale (e.g., 1 billion users).
- Back-of-envelope calculations for storage, CPU, and network.
- Identifying bottlenecks and single points of failure.

---

## Preparation Checklist

- [ ] Read the first 10 chapters of the SRE Book.
- [ ] Understand the difference between a process and a thread in Linux.
- [ ] Explain how a DNS query works in detail.
- [ ] Describe the TCP three-way handshake and its performance implications.
- [ ] Practice a mock "Incident Response" scenario.
- [ ] Design a global load balancing strategy for a new service.
- [ ] Learn the basics of PromQL (Prometheus Query Language).
- [ ] Understand Kubernetes (GKE) architecture (Pods, Services, Ingress).
- [ ] Explain the CAP theorem and its application to Cloud Spanner vs Bigtable.

---

## Interview Questions About SRE

1. "How do you decide between a 99.9% and a 99.99% SLO?"
2. "A service is experiencing high tail latency (P99). How do you debug it?"
3. "How would you automate a manual database failover process safely?"
4. "What happens when you type 'google.com' into a browser? (SRE Perspective: DNS, GFE, LB, App, DB)."
5. "Your error budget is at 0%. A critical security patch needs to be deployed. What is your process?"

---

## Side Projects to Build

### Project 1: SLO Dashboard & Alertmanager
- **Description**: Build a system that monitors a dummy API, calculates its real-time SLO, and sends an alert when the error budget is burning too fast.
- **Skills**: Monitoring, Prometheus/Grafana, Alerting logic.

### Project 2: High-Availability Kubernetes Cluster
- **Description**: Deploy a multi-region application on GKE with automatic failover and load balancing.
- **Skills**: K8s, GSLB, Traffic routing, Infrastructure as Code.

### Project 3: Log Analysis Pipeline
- **Description**: Build a pipeline that ingests logs from multiple sources and performs anomaly detection to identify potential outages.
- **Skills**: Data pipelines, Anomaly detection, SRE observability.
