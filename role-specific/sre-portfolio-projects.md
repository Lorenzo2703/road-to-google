# 🛠️ SRE Portfolio Projects Guide

> Suggested systems engineering and automation projects to strengthen your candidacy for Google Site Reliability Engineering (SRE).

---

## Priority Projects

### Project 1: Distributed Load Generator & Rate Limiter
**Priority**: ⭐⭐⭐⭐⭐ | **Time**: 2-3 days | **Difficulty**: Medium
- **Description**: Build a high-throughput microservice in Go or Python. Implement a distributed token bucket rate-limiting algorithm using Redis. Load-test the system using a tool like Locust or k6 to show it successfully enforces quotas and sheds load during spikes.
- **What it demonstrates**:
  - Understanding of rate-limiting algorithms
  - Handling of network latency and Redis locks
  - Capacity testing and performance evaluation
- **Bonus**: Implement adaptive rate limiting based on downstream CPU usage.

---

### Project 2: Kubernetes Toil-Reduction Cleanup Operator
**Priority**: ⭐⭐⭐⭐⭐ | **Time**: 2-3 days | **Difficulty**: Medium-Hard
- **Description**: Develop a custom Kubernetes controller (using Python `kopf` or Go `operator-sdk`) that automatically scans GKE/local clusters for orphaned volumes, crashlooping pods, and unused resources. The operator should compile stack traces, publish reports, alert Slack, and execute a safe garbage collection.
- **What it demonstrates**:
  - Deep understanding of Kubernetes API and controllers
  - Active toil reduction mindset
  - Security and safe automation patterns

---

### Project 3: Prometheus Exporter & Alert Dashboard
**Priority**: ⭐⭐⭐⭐ | **Time**: 2 days | **Difficulty**: Medium
- **Description**: Write a custom daemon that hooks into standard Linux resource files (like `/proc/meminfo` or `/proc/net/dev`) to extract low-level network/socket telemetry. Expose the data as a Prometheus metrics endpoint. Configure Prometheus scraping, set up Alertmanager triggers, and visualize system health in Grafana.
- **What it demonstrates**:
  - Linux internals `/proc` filesystem knowledge
  - Practical observability, metrics collection, and dashboard configuration
  - Defining clear, non-noisy alerting rules

---

### Project 4: Automated Failover & Disaster Recovery Simulation
**Priority**: ⭐⭐⭐⭐⭐ | **Time**: 3 days | **Difficulty**: Hard
- **Description**: Set up a multi-zone application on Google Cloud (using Terraform). Use a script (or a tool like Chaos Mesh) to simulate node termination, zone outage, and database replication lag. Programmatically capture failover times, database consistency states, and measure the Mean Time to Recovery (MTTR).
- **What it demonstrates**:
  - Infrastructure as Code (IaC) with Terraform
  - Chaos engineering and testing distributed failure modes
  - High availability and disaster recovery design

---

## GitHub Profile Tips for SRE
- [ ] Pin projects that contain real software (Go, Python, C++ code), not just Terraform templates or YAML configs
- [ ] Include clear installation instructions and a `docker-compose.yml` for local execution
- [ ] Document design trade-offs, architecture diagrams, and back-of-the-envelope calculations in the README
- [ ] Demonstrate testing: include unit tests, integration tests, and mock systems checks
