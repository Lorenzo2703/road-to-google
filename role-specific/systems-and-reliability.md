# 🐧 Linux Internals & Systems Reliability

> Essential systems knowledge for Google SRE interviews covering OS primitives, tracing tools, and distributed failure modes.

---

## Linux System Internals

### 1. Processes and CPU Scheduling
- **Process States**: Running (`R`), Interruptible Sleep (`S`), Uninterruptible Sleep (`D` - usually waiting on I/O), Zombie (`Z` - terminated but parent hasn't read exit status).
- **Process Lifecycle**:
  - `fork()`: Clones the calling process.
  - `execve()`: Replaces the process image with a new program binary.
  - `wait()`: Parent waits for child exit.
- **CPU Load Average**: Represents the average number of processes in the CPU run queue (either running or waiting to run) + processes in uninterruptible sleep (`D`). A load average of 4.0 on a 4-core machine means the CPU is fully saturated.

### 2. Virtual Memory & OOM Killer
- **Virtual Memory**: Maps process address space to physical memory (RAM + swap).
- **Page Faults**:
  - *Minor*: Virtual page mapped to a physical page already in RAM (shared library).
  - *Major*: Page must be read from disk (swap or file-backed mapping).
- **OOM (Out Of Memory) Killer**: When RAM+Swap is exhausted, the Linux kernel terminates processes to free memory. It computes an `oom_score` based on memory usage percentages and the configuration `/proc/[pid]/oom_score_adj`.

### 3. Sockets & Networking
- **TCP States**: `LISTEN`, `SYN_SENT`, `SYN_RECV`, `ESTABLISHED`, `FIN_WAIT_1`, `CLOSE_WAIT`, `LAST_ACK`, `TIME_WAIT`.
- **TIME_WAIT**: Occurs on the side that initiates the active close. It ensures any lingering packets in the network are discarded before a new connection uses the same socket (lasts 2 * MSL - Maximum Segment Lifetime, typically 1-4 mins).

---

## Systems Tracing & Debugging Toolkit

| Tool | Purpose | Key Flag / Example |
|------|---------|-------------------|
| `strace` | Trace system calls and signals executed by a process | `strace -p [PID] -c` (Summary of syscall counts and times) |
| `lsof` | List open files, file descriptors, and network connections | `lsof -i :8080` (Check what process is bound to port 8080) |
| `tcpdump` | Network packet analyzer | `tcpdump -i eth0 port 80 -nn` (Capture traffic on port 80) |
| `top` / `htop` | Interactive process and resource monitor | Highlights CPU/memory usage, load average, and thread count |
| `ss` / `netstat` | Investigate socket statistics and connection states | `ss -tulpn` (List listening sockets with PID/program name) |
| `iostat` / `vmstat` | Monitor CPU, disk I/O, and virtual memory statistics | `vmstat 1 5` (Show system activity statistics every second) |

---

## Distributed Systems Failure Modes

### 1. Cascading Failures
- **Definition**: A positive feedback loop of failures that propagates through a distributed system.
- **Cause**: If one server fails, its traffic is redistributed to the remaining healthy servers, overloading them and triggering further failures.
- **Mitigation**:
  - **Load Shedding**: Reject excess requests when overloaded.
  - **Rate Limiting**: Restrict incoming traffic at the edge.
  - **Circuit Breakers**: Fail fast on downstream calls without wasting resources.

### 2. Network Partitions & Split-Brain
- **Partition**: A communication failure where nodes are divided into disjoint groups.
- **Split-Brain**: When two partitioned subsets of a cluster both assume they are the active coordinator and modify database state independently, leading to data corruption.
- **Mitigation**: Use consensus algorithms (Paxos, Raft) that require a strict majority quorum (`N/2 + 1`) to elect a leader and commit logs.

### 3. Thundering Herd
- **Definition**: Many client processes waiting for an event are awakened simultaneously when the event occurs, overloading the system resources.
- **Mitigation**: Add randomized delay (**jitter**) to client retry intervals, and use caching with randomized TTL expiration.
