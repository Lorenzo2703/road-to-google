# 🏢 Enterprise AI Considerations

> Understanding enterprise needs — a preferred qualification for the Google role.

---

## Why Enterprise Matters for This Role

From the job description:
> "Experience building applications for enterprise needs, which includes AI safety, data residency, integration with existing systems."
> "Understanding of the needs of the Cloud customers."

---

## Key Enterprise AI Topics

### 1. AI Safety & Responsible AI
- Content filtering (harmful, biased, or inappropriate outputs)
- Prompt injection attacks and defenses
- Model hallucination detection and mitigation
- Fairness and bias evaluation
- Human-in-the-loop for high-stakes decisions

### 2. Data Residency & Compliance
- GDPR (EU data protection)
- HIPAA (US healthcare data)
- SOC 2 (security controls)
- Data sovereignty: processing data in specific regions
- Audit trails and logging requirements

### 3. Security
- Authentication: OAuth 2.0, SAML, API keys
- Authorization: RBAC, ABAC, IAM policies
- Encryption: At rest (AES-256) and in transit (TLS 1.3)
- Secrets management: No hardcoded keys
- Network security: VPCs, firewalls, private endpoints

### 4. Integration with Existing Systems
- Common enterprise systems: Salesforce, SAP, ServiceNow, Jira
- API patterns: REST, gRPC, GraphQL
- Event-driven integration: Webhooks, message queues
- Legacy system wrappers

### 5. Scale & Reliability
- High availability: 99.9%+ uptime SLAs
- Disaster recovery: Multi-region deployment
- Load handling: Burst traffic, auto-scaling
- Cost management: Budget alerts, usage caps

---

## Interview Angle

When discussing enterprise in interviews, demonstrate:
1. **Awareness**: You know these constraints exist
2. **Empathy**: You understand why enterprises care about them
3. **Practical solutions**: You can design systems that address them
4. **Trade-offs**: You can articulate the cost of compliance vs. the risk of ignoring it
