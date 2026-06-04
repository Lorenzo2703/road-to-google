# 🛠️ SRE-Specific System Design

> Designing distributed systems with a focus on high availability, observability, scalability, and fault tolerance.

---

## Design Challenge 1: Global Rate Limiter

### Requirements
- Process 100K+ requests/sec across a globally distributed application
- Enforce rate limits per API key/IP address (e.g. 100 req/min)
- Latency added to HTTP requests must be < 5ms
- System must fail-open (if rate limiter goes down, traffic is allowed through)

### Architecture
```
┌──────────────┐      ┌───────────────┐      ┌──────────────┐
│   Client     │─────▶│   API Gateway │─────▶│ Backend      │
└──────────────┘      └───────┬───────┘      │ Services     │
                              │              └──────────────┘
                     (Check Rate / Fail-Open)
                              ▼
                      ┌───────────────┐
                      │ Local Cache   │
                      │ (Memory/LRU)  │
                      └───────┬───────┘
                              │ (Async sync / Batching)
                              ▼
                      ┌───────────────┐
                      │ Redis Cluster │
                      │ (Global Sync) │
                      └───────────────┘
```

### Key Design Decisions
1. **Local vs Global Counters**: Gateway instances check a fast local cache first. Local statistics are asynchronously synchronized with a shared Redis cluster to minimize network latency.
2. **Fail-Open Policy**: Gateway uses a timeout (e.g. 2ms) when querying the rate limiter. If a timeout occurs, a metric is logged, and the request is permitted.
3. **Token Bucket Algorithm**: Standard sliding window algorithm is resource-intensive; token bucket represented as a timestamp and a float count in Redis is highly efficient.

---

## Design Challenge 2: Distributed Tracing System (Google Dapper Clone)

### Requirements
- Trace requests across thousands of services
- Capture span start/end times, metadata, and cross-service dependencies
- Low overhead: trace collection must consume < 1% of host CPU/memory
- Support petabytes of trace data per day with search capabilities

### Architecture
```
┌─────────────────┐       ┌─────────────────┐
│ Service A       │       │ Service B       │
│ (Inject Context)│──gRPC▶│ (Extract Context)
│ [Agent Daemon]  │       │ [Agent Daemon]  │
└────────┬────────┘       └────────┬────────┘
         │ (Udp / Unix Socket)     │
         ▼                         ▼
┌───────────────────────────────────────────┐
│ Host Agent (Local collector daemon)      │
└────────────────────┬──────────────────────┘
                     │ (Batch TCP / Async)
                     ▼
┌───────────────────────────────────────────┐
│ Streaming Ingestion Pipeline (Kafka)     │
└────────────────────┬──────────────────────┘
                     ▼
┌───────────────────────────────────────────┐
│ Collector Workers & Storage (Bigtable)    │
└───────────────────────────────────────────┘
```

### Key Design Decisions
1. **Adaptive Sampling**: Tracing 100% of calls is expensive. The system uses head-based sampling (e.g. sample 1 in 1000 requests) or adaptive tail-based sampling (sample if request exhibits latency > 95th percentile or encounters an error).
2. **Out-of-Band Collection**: Trace data is written to a local collector daemon via a fast Unix domain socket or UDP, decoupling tracing from the main application thread.
3. **No-SQL Storage**: Use a wide-column store like Bigtable or Cassandra, which handles massive write volume efficiently.

---

## Design Challenge 3: Metrics Collection & Alerting Pipeline (Prometheus-like)

### Requirements
- Monitor 10K+ instances, scraping metrics every 10 seconds
- Support complex query metrics (e.g. rate, percentile computations)
- System reliability: alerting must remain operational even when parts of the cloud are down
- Alert deduplication and grouping to prevent alert storms

### Key Components
1. **Scraper Workers**: Periodically poll `/metrics` HTTP endpoints from target servers (Pull model).
2. **Time-Series Database (TSDB)**: Writes metrics to disk using memory-mapped files and delta-of-delta compression.
3. **Rules Engine**: Periodically runs query expressions (e.g. `rate(http_errors[5m]) > threshold`) to evaluate alert triggers.
4. **Alertmanager**: Receives triggers, groups alerts by service and environment, deduplicates alerts, and routes them to on-call paging tools.
