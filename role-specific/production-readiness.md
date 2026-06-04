# 🏢 Production Readiness Checklist

> Best practices for evaluating and onboarding services to ensure high availability and reliability in production.

---

## What is Production Readiness?

A **Production Readiness Review (PRR)** is a structural audit conducted to ensure a service can be operated reliably and efficiently in production. It identifies architectural, operational, and monitoring gaps before they trigger critical incidents.

---

## Core PRR Categories

### 1. Architecture and Fault Tolerance
- [ ] **No Single Point of Failure (SPOF)**: Ensure all components (load balancers, web instances, databases) are deployed across multiple zones/regions.
- [ ] **Graceful Degradation**: Can the service continue running with reduced functionality if a dependency goes down?
- [ ] **Timeout and Retry Policies**: All external calls have explicit timeouts. Retries use exponential backoff with random jitter.
- [ ] **Circuit Breakers**: Implemented on all critical downstream APIs to prevent cascading overload.
- [ ] **Load Shedding**: The service can actively reject lower-priority traffic when resources are saturated.

### 2. Observability and Alerting
- [ ] **Symptom-Based Alerting**: Alerts are tied to SLO violations (e.g. latency, error rates) rather than resource utilization (CPU/Memory) to avoid alert fatigue.
- [ ] **Metrics Dashboard**: A central dashboard (Grafana/Cloud Monitoring) visualizes the Golden Signals: Latency, Traffic, Errors, and Saturation.
- [ ] **Distributed Tracing**: Trace context is propagated across network boundaries (via OpenTelemetry) for cross-service diagnostics.
- [ ] **Audit Logging**: Structured logs (JSON format) with distinct correlation IDs (`trace_id`) are forwarded to a central log store.

### 3. Change Management and Deployments
- [ ] **CI/CD Pipeline**: Deployments are fully automated, avoiding manual shell interactions.
- [ ] **Canary Rollouts**: Updates are slowly rolled out to a small percentage of traffic (e.g., 1%, 5%, 10%) before full promotion.
- [ ] **Automated Rollback**: The deployment system automatically rolls back changes if error rates or error budgets spike.
- [ ] **Infrastructure as Code (IaC)**: All infrastructure is defined in version-controlled config files (Terraform).

### 4. Backup and Disaster Recovery
- [ ] **Automated Backups**: Backups are run, encrypted, and stored off-site.
- [ ] **Recovery Drills**: Backup restoration and failover drills are performed periodically to verify recovery times (RTO/RPO).
- [ ] **Drain Procedures**: Documented scripts exist to redirect all traffic away from a failing zone or region.

### 5. Security & Isolation
- [ ] **Secrets Management**: No credentials are hardcoded. Use Cloud Secret Manager or HashiCorp Vault.
- [ ] **Least Privilege**: IAM policies restrict system permissions to the minimum required.
- [ ] **Network Isolation**: Backend databases and queues run on private subnets behind firewalls.
