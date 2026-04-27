# 🏗️ System Design Fundamentals

> Core concepts for Google system design interviews.

---

## System Design Interview Framework

**Step 1: Clarify Requirements (5 min)**
- Functional requirements (what the system does)
- Non-functional requirements (scale, latency, availability)
- Constraints and assumptions

**Step 2: Back-of-Envelope Estimation (3 min)**
- Users/requests per day → per second
- Storage needs
- Bandwidth needs

**Step 3: High-Level Design (10 min)**
- Major components and their interactions
- API design
- Data model

**Step 4: Deep Dive (15 min)**
- Scale the bottlenecks
- Discuss trade-offs for each decision
- Handle failure scenarios

**Step 5: Trade-offs & Wrap-up (5 min)**
- Summarize key decisions
- Discuss alternatives you considered
- Mention monitoring and operational concerns

---

## Core Concepts Quick Reference

### Load Balancing
- **Round Robin**: Simple, equal distribution
- **Least Connections**: Routes to least-loaded server
- **Consistent Hashing**: Minimizes redistribution when servers change

### Caching
- **Cache-aside**: App checks cache first, loads from DB on miss
- **Write-through**: Write to cache and DB simultaneously
- **Write-behind**: Write to cache, async write to DB
- **CDN**: Cache static content at edge locations

### Databases
| Type | Use Case | Examples |
|------|----------|---------|
| Relational | ACID, complex queries | PostgreSQL, MySQL, Cloud SQL |
| Document | Flexible schema, nested data | MongoDB, Firestore |
| Key-Value | High throughput, simple lookups | Redis, Memcached, Bigtable |
| Graph | Relationships, traversals | Neo4j, Dgraph |
| Time-Series | Metrics, events | InfluxDB, Cloud Monitoring |

### CAP Theorem
- **C**onsistency: Every read gets the latest write
- **A**vailability: Every request gets a response
- **P**artition tolerance: System works despite network failures
- In practice: Choose CP (banking) or AP (social media)

### Message Queues
- **When**: Decouple producers/consumers, handle spikes, async processing
- **Options**: Pub/Sub, Kafka, RabbitMQ, Cloud Tasks
- **Patterns**: Point-to-point, publish-subscribe, fan-out

### Scaling
- **Vertical**: Bigger machine (limited, expensive)
- **Horizontal**: More machines (preferred, with complexity)
- **Sharding**: Partition data across databases
- **Replication**: Copy data for reads and fault tolerance

---

## GCP Services to Know

| Service | Purpose | When to Use |
|---------|---------|-------------|
| Cloud Run | Serverless containers | Stateless APIs, Microservices |
| GKE | Kubernetes | Complex workloads, microservices |
| Cloud Functions | Serverless functions | Simple event handlers |
| Pub/Sub | Message queue | Async communication |
| Cloud SQL | Managed PostgreSQL/MySQL | Relational data |
| Firestore | NoSQL document DB | Flexible schemas |
| Bigtable | Wide-column store | High throughput |
| BigQuery | Analytics warehouse | Large-scale analytics |
| Cloud Storage | Object storage | Files, models, artifacts |
| Vertex AI | ML platform | Model serving, training |
| Cloud Trace | Distributed tracing | Debugging latency |
| Cloud Monitoring | Metrics & alerting | Operational health |

---

## Estimation Cheat Sheet

| Quantity | Approximation |
|----------|--------------|
| 1 day | ~86,400 seconds ≈ 10^5 |
| 1 month | ~2.5 million seconds ≈ 2.5 × 10^6 |
| 1 year | ~31 million seconds ≈ 3 × 10^7 |
| 1 KB | 1,000 bytes |
| 1 MB | 1,000,000 bytes |
| 1 GB | 10^9 bytes |
| 1 TB | 10^12 bytes |
| 1 million QPS → | ~12 requests/ms |
| 100M users, 10% DAU → | 10M DAU |
| Average read latency (SSD) | ~100 μs |
| Network round trip (same DC) | ~500 μs |
| Network round trip (cross-region) | ~50-150 ms |
