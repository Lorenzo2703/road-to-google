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

## Preparation Checklist (with Answers)

- [x] Read the first 10 chapters of the SRE Book.
- [x] **Understand the difference between a process and a thread in Linux:** A process is an independent execution environment with its own memory space; a thread is a lightweight unit within a process that shares memory and resources with other threads. Context switching between threads is faster.
- [x] **Explain how a DNS query works in detail:** Browser cache -> OS cache -> Router cache -> ISP DNS Resolver. If not found locally, the resolver queries the Root Server -> TLD Server (.com) -> Authoritative Name Server (google.com) to resolve the IP address.
- [x] **Describe the TCP three-way handshake and its performance implications:** SYN (client to server) -> SYN-ACK (server to client) -> ACK (client to server). Implication: Introduces a 1 Round Trip Time (RTT) delay before any payload data is transmitted, which can be significant for high-latency connections.
- [x] **Practice a mock "Incident Response" scenario:** **Scenario**: PagerDuty alerts on elevated 5xx errors. **Triage**: Check Grafana dashboards to identify the failing microservice. **Mitigate**: Roll back the latest Canary release that caused the spike. **Resolve**: Document in a blameless postmortem.
- [x] **Design a global load balancing strategy for a new service:** Use Anycast IP routing to direct traffic to the geographically nearest Point of Presence (PoP). Terminate TLS at a Layer 7 Load Balancer (like GFE), which then distributes traffic to healthy backend clusters across regions based on capacity and health checks.
- [x] **Learn the basics of PromQL (Prometheus Query Language):** Example: `rate(http_requests_total{status="500"}[5m])` calculates the per-second rate of 500 errors over the last 5 minutes.
- [x] **Understand Kubernetes (GKE) architecture (Pods, Services, Ingress):** **Pods**: smallest deployable compute units (containers). **Services**: abstracts a set of Pods, providing a stable internal IP. **Ingress**: manages external access to the services, providing HTTP/HTTPS routing.
- [x] **Explain the CAP theorem and its application to Cloud Spanner vs Bigtable:** CAP = Consistency, Availability, Partition Tolerance. A system can only guarantee two. **Bigtable** is CP (strongly consistent, but unavailable during a master node failure). **Cloud Spanner** is technically CP, but its use of TrueTime and Google's private network makes partitions so rare that it's often considered "effectively CA".

---

## Interview Questions About SRE (Answers)

1. **"How do you decide between a 99.9% and a 99.99% SLO?"**
   *Answer*: It is a trade-off between engineering cost and business need. 99.9% allows ~43 minutes of downtime per month, while 99.99% allows ~4.3 minutes. Moving to four nines requires exponential effort (redundancy, faster automated failovers, restricted deployments). If the business impact (revenue/reputation) of those 39 minutes doesn't justify the engineering cost and slower feature velocity, stick to 99.9%.

2. **"A service is experiencing high tail latency (P99). How do you debug it?"**
   *Answer*: I would start by checking the four golden signals to look for saturation or resource constraints (e.g., CPU throttling or memory leaks leading to Garbage Collection pauses). Next, I'd use distributed tracing (like Dapper/Jaeger) to pinpoint if the delay is in a specific downstream dependency, and check database metrics for slow queries, locking, or network congestion.

3. **"How would you automate a manual database failover process safely?"**
   *Answer*: Introduce a distributed consensus store (like etcd or ZooKeeper) for leader election. Implement robust health checking. When the primary fails, the system auto-elects a replica as the new primary. Crucially, implement STONITH ("Shoot The Other Node In The Head") or fencing to terminate the old primary to avoid a "split-brain" scenario where both accept writes.

4. **"What happens when you type 'google.com' into a browser? (SRE Perspective: DNS, GFE, LB, App, DB)."**
   *Answer*: DNS uses Anycast to resolve the IP of the closest Google edge node. The TCP handshake and TLS termination happen at the Google Front End (GFE), which acts as an L7 reverse proxy and load balancer. GFE routes the request over Google's backbone to an internal service/app server. The app server retrieves data from distributed caches (Memcached) or databases (Spanner/Bigtable) and returns the payload.

5. **"Your error budget is at 0%. A critical security patch needs to be deployed. What is your process?"**
   *Answer*: Security vulnerabilities are exceptions to the standard error budget freeze policy. A critical security risk outweighs the risk of temporary instability. The patch must be deployed immediately, but safely: following emergency change procedures, using progressive rollouts (canarying), and monitoring closely to ensure it doesn't cause a catastrophic outage.

---

## Side Projects to Build (Action Plans)

### Project 1: SLO Dashboard & Alertmanager
- **Description**: Build a system that monitors a dummy API, calculates its real-time SLO, and sends an alert when the error budget is burning too fast.
- **Skills**: Monitoring, Prometheus/Grafana, Alerting logic.
- **Implementation Plan**:
  1. Write a simple Python FastAPI or Go server with randomized artificial delays and failure rates.
  2. Expose a `/metrics` endpoint using a Prometheus client library.
  3. Deploy Prometheus to scrape the metrics and Grafana to visualize the Error Rate and Latency (SLIs).
  4. Define an SLO (e.g., 99% success rate) and configure Alertmanager to trigger a Slack webhook if the burn rate exceeds the threshold.

### Project 2: High-Availability Kubernetes Cluster
- **Description**: Deploy a multi-region application on GKE with automatic failover and load balancing.
- **Skills**: K8s, GSLB, Traffic routing, Infrastructure as Code.
- **Implementation Plan**:
  1. Use Terraform to provision a regional GKE cluster (nodes distributed across 3 availability zones).
  2. Deploy a stateless application using a Deployment resource with a Horizontal Pod Autoscaler (HPA).
  3. Configure a Kubernetes Service and an Ingress object to provision a Google Cloud External Global HTTP(S) Load Balancer.
  4. Simulate an outage by manually draining/cordoning nodes in one zone and observing the LB seamlessly route traffic to the surviving zones.

### Project 3: Log Analysis Pipeline
- **Description**: Build a pipeline that ingests logs from multiple sources and performs anomaly detection to identify potential outages.
- **Skills**: Data pipelines, Anomaly detection, SRE observability.
- **Implementation Plan**:
  1. Generate mock application logs (JSON format) using a script.
  2. Use Fluentd or Filebeat to collect and forward these logs to a Pub/Sub topic (or Kafka broker).
  3. Create a streaming data pipeline (using Apache Flink or Google Cloud Dataflow) to window the logs and compute moving averages of error frequency.
  4. If an anomaly is detected (e.g., 5x spike in "ERROR" severity), sink an alert event to BigQuery or trigger a serverless function notification.
