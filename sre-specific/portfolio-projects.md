# 🚀 SRE Portfolio Projects

> Projects that demonstrate an SRE mindset: building for reliability, scalability, and automation.

---

## Project 1: The SLO-Driven Deployment Guardian

### Overview
Build a tool that monitors the "Error Budget" of a service and automatically blocks or reverts CI/CD deployments if the budget is burning too fast.

### Tech Stack
- **Languages**: Python or Go.
- **Tools**: Prometheus (Metrics), GitHub Actions or Jenkins (CI/CD), Slack API (Alerting).

### Key Features
- Scrapes SLIs from Prometheus.
- Calculates 7-day and 30-day Error Budgets.
- Intercepts deployment triggers based on SLO health.
- Automated rollback on SLO violation during canary phase.

### Relevance to SRE
Demonstrates understanding of **Error Budgets** and the **Release Engineering** principle of reducing risk.

---

### Project 2: Distributed Anomaly Detection & Incident Automator

### Overview
A system that detects abnormal latency spikes across multiple regions and automatically executes a "pre-defined mitigation playbook" (e.g., scaling up pods or redirecting traffic).

### Tech Stack
- **Languages**: Python (with Scikit-Learn/Pandas for anomaly detection).
- **Tools**: Cloud Pub/Sub, Cloud Functions, Grafana.

### Key Features
- Ingests telemetry data in real-time.
- Uses a simple ML model (or threshold-based logic) to detect "incidents".
- Automatically triggers a "Mitigation Webhook".
- Generates a "Draft Postmortem" in Google Docs with the relevant metrics pre-populated.

### Relevance to SRE
Demonstrates focus on **Observability**, **MTTR (Mean Time to Recovery)**, and **Incident Management**.

---

### Project 3: The "Toil-Buster" Infrastructure Generator

### Overview
An Infrastructure-as-Code (IaC) framework that allows developers to spin up a "production-ready" Google Cloud environment (GKE, Cloud SQL, Redis) with built-in SRE best practices.

### Tech Stack
- **Tools**: Terraform, Kubernetes, Helm.

### Key Features
- Pre-configured health checks and liveness probes.
- Automatic horizontal and vertical pod autoscaling.
- Integrated monitoring dashboards and alerting rules out of the box.
- Secret management and security hardening.

### Relevance to SRE
Demonstrates the principle of **Eliminating Toil** and providing a **Self-Service Platform** for developers.

---

## 🎤 How to Present These Projects

When discussing these in an interview, use the following framework:
1.  **The Toil/Problem**: "We were manually rolling back failures, which took 30 minutes..."
2.  **The Engineering Solution**: "I built an automated guardian that reduced this to 2 minutes..."
3.  **The Reliability Impact**: "This improved our overall availability from 99.5% to 99.9%."
4.  **The Scale**: "The system now handles 5,000 events per second across 3 regions."
