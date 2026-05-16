# 🏗️ SRE Engineering Fundamentals - Checklist Answers

This document provides detailed answers and implementations for the SRE Engineering checklist found in `sre-engineering.md`.

---

## 1. Can you implement a Token Bucket rate limiter from scratch?

**Concept:** A token bucket algorithm manages a bucket with a maximum capacity of tokens. Tokens are added to the bucket at a fixed rate. When a request comes in, it must take a token from the bucket to be processed. If the bucket is empty, the request is rejected or queued. This is highly effective for rate-limiting APIs.

**Implementation (Python):**
```python
import time
import threading

class TokenBucket:
    def __init__(self, capacity, fill_rate):
        """
        :param capacity: Maximum number of tokens the bucket can hold.
        :param fill_rate: Number of tokens added to the bucket per second.
        """
        self.capacity = float(capacity)
        self.fill_rate = float(fill_rate)
        self.tokens = float(capacity)
        self.last_fill_time = time.time()
        self.lock = threading.Lock()

    def allow_request(self, tokens_needed=1):
        with self.lock:
            now = time.time()
            # Calculate how many tokens to add since the last check
            time_elapsed = now - self.last_fill_time
            tokens_to_add = time_elapsed * self.fill_rate
            
            # Update token count, bounded by the maximum capacity
            self.tokens = min(self.capacity, self.tokens + tokens_to_add)
            self.last_fill_time = now
            
            # Check if we have enough tokens to allow the request
            if self.tokens >= tokens_needed:
                self.tokens -= tokens_needed
                return True
            return False
```

---

## 2. Do you know how to write a Thread-Safe producer-consumer queue?

**Concept:** A producer-consumer queue requires synchronization so that producers can safely add items and consumers can safely remove them without race conditions or data corruption. We achieve this using a mutex lock and condition variables.

**Implementation (Python):**
```python
import threading
from collections import deque

class ThreadSafeQueue:
    def __init__(self, max_size):
        self.queue = deque()
        self.max_size = max_size
        self.lock = threading.Lock()
        
        # Condition variable for consumers to wait when the queue is empty
        self.not_empty = threading.Condition(self.lock)
        # Condition variable for producers to wait when the queue is full
        self.not_full = threading.Condition(self.lock)

    def put(self, item):
        with self.not_full:
            while len(self.queue) >= self.max_size:
                self.not_full.wait()  # Wait until there is space
            
            self.queue.append(item)
            self.not_empty.notify()   # Notify a waiting consumer

    def get(self):
        with self.not_empty:
            while len(self.queue) == 0:
                self.not_empty.wait() # Wait until there is an item
            
            item = self.queue.popleft()
            self.not_full.notify()    # Notify a waiting producer
            return item
```

---

## 3. Can you explain the difference between TCP and UDP for various system types?

- **TCP (Transmission Control Protocol)**: 
  - **Characteristics:** Connection-oriented, reliable, ordered, and error-checked delivery of a stream of bytes. It includes built-in flow control and congestion control mechanisms.
  - **Use Cases (System Types):** Web traffic (HTTP/HTTPS), file transfer (FTP), email (SMTP), remote administration (SSH), and database connections. Any system where data integrity and guaranteed delivery are more important than raw speed.

- **UDP (User Datagram Protocol)**:
  - **Characteristics:** Connectionless, best-effort delivery, no ordering guarantees, and no built-in error recovery (no retransmissions). It has much lower overhead and latency.
  - **Use Cases (System Types):** Real-time streaming (video/audio, WebRTC), online multiplayer gaming, DNS queries, VoIP, and telemetry/metrics collection (e.g., StatsD). Any system where dropping a few packets is acceptable compared to the latency introduced by waiting for retransmissions.

---

## 4. Do you understand Database Sharding and how to handle cross-shard transactions?

**Database Sharding** is a horizontal scaling technique where a large database is divided into smaller, faster, and more manageable pieces called *shards*. Each shard runs on a separate database server. A "shard key" determines which shard holds a specific piece of data.

**Handling Cross-Shard Transactions:**
Transactions that span multiple shards are inherently complex because they require distributed coordination to maintain ACID properties.
1. **Two-Phase Commit (2PC):** A distributed algorithm that coordinates all participating shards. Phase 1 prepares the transaction (locking resources), and Phase 2 commits or aborts based on unanimous agreement. **Drawback:** It is synchronous, blocking, and scales poorly, leading to high latency and potential deadlocks.
2. **Saga Pattern:** Breaks the distributed transaction into a sequence of local transactions. Each local transaction updates its database and publishes an event to trigger the next step. If a step fails, "compensating transactions" are triggered to undo previous steps. **Drawback:** Provides eventual consistency rather than strict ACID compliance, and logic can become highly complex.
3. **Avoidance (Best Practice):** The most common SRE/Architectural approach is to design the schema and choose shard keys specifically to *avoid* cross-shard transactions. For example, co-locating all data for a specific user or tenant on the same shard.

---

## 5. Can you design an Auto-scaling algorithm based on custom metrics?

**Concept:** While basic auto-scaling uses CPU or memory, advanced systems scale on custom business metrics (e.g., queue length, concurrent requests, latency percentiles).

**Design Algorithm (The Controller Pattern):**
1. **Metric Emitting:** Applications expose a custom metric endpoint (e.g., `/metrics` for Prometheus) exposing a metric like `job_queue_depth`.
2. **Collection:** A monitoring system (like Prometheus) scrapes and stores these metrics time-series data.
3. **Evaluation Loop:** An autoscaler controller (e.g., Kubernetes HPA with Custom Metrics API) evaluates the metric at a fixed interval (e.g., every 15 seconds).
4. **Target Tracking Logic:**
   ```text
   Desired Replicas = ceil(Current Replicas * (Current Metric Value / Target Metric Value))
   ```
   *Example:* If the target `queue_depth_per_worker` is 10, current depth is 50, and we have 2 workers: `2 * (50 / 10) = 10` workers required.
5. **Hysteresis (Cooldowns):** Implement scale-up and scale-down cooldown periods (e.g., do not scale down if a scale-up happened in the last 3 minutes) to prevent "thrashing" (rapidly destroying and creating instances).

---

## 6. Do you know how to use Protobuf for efficient cross-service communication?

**Protocol Buffers (Protobuf)** is Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data.

**How to use it:**
1. Define the data structure and service interfaces in a `.proto` file.
   ```protobuf
   syntax = "proto3";
   message UserRequest {
     string user_id = 1;
   }
   message UserResponse {
     string name = 1;
     int32 age = 2;
   }
   service UserService {
     rpc GetUser (UserRequest) returns (UserResponse);
   }
   ```
2. Run the `protoc` compiler to generate native classes/structs for your target language (Go, Python, Java, etc.).
3. Implement the client and server using a framework like **gRPC**, which uses Protobuf as its default Interface Definition Language (IDL) and underlying message interchange format.

**Why it's efficient:** 
- It serializes to a highly compressed binary format, heavily reducing network bandwidth usage compared to JSON or XML.
- Parsing binary is significantly faster than parsing text formats.
- It relies on numbered fields rather than repeating string keys in the payload, further saving bytes.

---

## 7. Are you comfortable with Linux Debugging Tools like `strace`, `lsof`, `tcpdump`, and `perf`?

SREs rely on these tools when high-level metrics and logs don't provide the answer.

- **`strace` (System Call Tracer):** Intercepts and records the system calls which are called by a process and the signals which are received.
  - *Use Case:* Discovering why a process is hanging, what files it's failing to open (e.g., `ENOENT`), or diagnosing permission issues (`EACCES`).
  - *Command:* `strace -p <pid>`
- **`lsof` (List Open Files):** Lists all open files and the processes that opened them. In Linux, "everything is a file," including network sockets and directories.
  - *Use Case:* Finding which process is listening on port 8080 (`lsof -i :8080`), or seeing if a deleted file is still being held open by a process (causing disk space issues).
- **`tcpdump`:** A powerful command-line packet analyzer.
  - *Use Case:* Capturing live network traffic to debug dropped packets, routing issues, or inspecting unencrypted payload headers to verify load balancer behavior.
  - *Command:* `tcpdump -i eth0 port 443`
- **`perf` (Performance Counters):** A performance analyzing tool in Linux.
  - *Use Case:* Profiling CPU usage, generating flame graphs to see exactly which functions in the code are consuming CPU cycles, and identifying hardware cache misses.
  - *Command:* `perf record -p <pid> -g` followed by `perf report`
