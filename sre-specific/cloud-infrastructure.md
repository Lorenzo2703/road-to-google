# ☁️ Google Cloud Infrastructure for SREs

> Understanding Google Cloud Platform (GCP) services through the lens of reliability and systems engineering.

---

## 1. Compute & Orchestration

### Google Kubernetes Engine (GKE)
- **SRE Focus**: Node auto-provisioning, horizontal/vertical pod autoscaling, and multi-cluster management (Anthos).
- **Reliability**: Regional clusters for high availability across zones.

### Cloud Run
- **SRE Focus**: Serverless scaling, request-based autoscaling, and concurrency management.
- **Reliability**: Built-in health checks and automatic traffic splitting for canaries.

---

## 2. Storage & Databases

### Cloud Spanner
- **SRE Focus**: Globally consistent, horizontally scalable relational database.
- **Reliability**: Synchronous replication and 99.999% SLA. Understanding Paxos-based consensus.

### Bigtable
- **SRE Focus**: High-throughput NoSQL for sub-10ms latency.
- **Reliability**: Replication for regional failover and data isolation.

### Cloud Storage (GCS)
- **SRE Focus**: Object storage with multiple classes (Standard, Nearline, Coldline, Archive).
- **Reliability**: Geo-redundant storage and versioning.

---

## 3. Networking

### Cloud Load Balancing
- **SRE Focus**: Global Anycast IP, L7 vs L4 balancing, and Cloud Armor for DDoS protection.
- **Reliability**: Automatic failover to the next closest region.

### Cloud DNS
- **SRE Focus**: 100% uptime SLA, programmable DNS.
- **Reliability**: Global distribution and low-latency resolution.

---

## 4. Observability (The Google Operations Suite)

### Cloud Monitoring (Stackdriver)
- **SRE Focus**: SLI monitoring, Dashboarding, and Alerting.
- **Reliability**: Uptime checks and custom metrics.

### Cloud Trace & Logging
- **SRE Focus**: Distributed tracing to identify latency bottlenecks and log-based metrics.
- **Reliability**: Ingesting and querying massive log volumes.

---

## 🏗️ SRE Infrastructure Patterns on GCP

| Pattern | GCP Service | Benefit |
|---------|-------------|---------|
| **Multi-Region Failover** | GSLB + Regional GKE | Surivability during region outages |
| **Global Consistency** | Cloud Spanner | ACID transactions at global scale |
| **Edge Caching** | Cloud CDN | Lower latency and origin protection |
| **Async Processing** | Cloud Pub/Sub | Decoupling and burst handling |
| **Safe Deployments** | Cloud Build + Canary | Reduced Blast Radius of changes |
