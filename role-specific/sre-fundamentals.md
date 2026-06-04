# ⚙️ SRE Fundamentals Guide

> Deep dive into Google's Site Reliability Engineering philosophy and models for interview preparation.

---

## What is SRE?

Site Reliability Engineering (SRE) is what happens when you ask a software engineer to design an operations function. SREs apply software engineering principles to solve infrastructure and operational problems, with a strong focus on automation, scalability, and system reliability.

**Key Books**: 
- [SRE Book](https://sre.google/sre-book/table-of-contents/)
- [SRE Workbook](https://sre.google/workbook/table-of-contents/)
- [Class SRE Workbook](https://sre.google/class-sre-book/table-of-contents/)

---

## Key SRE Principles to Master

### 1. Service Level Terminology (SLI, SLO, SLA)
- **Service Level Indicator (SLI)**: A quantifiable measure of the service performance.
  - *Example*: Latency of successful HTTP GET requests is < 200ms measured over a 1-minute window.
  - *Formula*: `(number of good events / total events) * 100`
- **Service Level Objective (SLO)**: A target reliability level for a service, specified as a percentage over a rolling window.
  - *Example*: 99.9% of HTTP requests must have a latency < 200ms over a rolling 30-day window.
- **Service Level Agreement (SLA)**: A legal contract specifying the SLO targets and the business consequences (refunds, penalties) if they are missed. SREs focus on SLOs, not SLAs.

### 2. Error Budgets
- **Definition**: The allowable unreliability of a service, defined as `100% - SLO%`.
  - *Example*: For a 99.9% SLO, the error budget is 0.1%.
- **Use Case**: Error budgets balance feature velocity (innovation) against stability. If the error budget is exhausted, releases are halted, and engineering efforts focus solely on reliability improvements.

### 3. Eliminating Toil
- **Toil Definition**: Repetitive, manual, automatable, tactical, and non-creative work that scales linearly with service size.
- **SRE Target**: Google caps SRE operational work (including toil and on-call) at **50%** of their time. The remaining 50% must be spent on software engineering projects to automate operations and improve system design.

### 4. Blameless Post-Mortems
- **Definition**: A post-mortem reviews a system outage to identify root causes and assign action items to prevent recurrence.
- **Blamelessness**: It assumes that engineers act with good intentions based on the information they had. It focuses on identifying system flaws rather than human mistakes.

---

## SRE Interview Questions to Expect

1. "How would you design a set of SLIs and SLOs for a new global multi-tier web application?"
2. "Your team's error budget is exhausted, but the product manager wants to push a critical feature. How do you handle this?"
3. "Walk me through how you would run a post-mortem for a cascading database outage caused by a routine deployment."
4. "What is the difference between a symptom-based alert and a cause-based alert? Which one should wake you up at 3 AM?"
5. "How do you distinguish between 'toil' and 'operational work' that cannot be automated?"

---

## Practical Checklist

- [ ] Read Chapters 1-5, 10, and 21-22 of the Google SRE Book
- [ ] Calculate the allowed downtime in minutes for 99.9%, 99.99%, and 99.999% availability over a 30-day window
- [ ] Draft an SLI/SLO document for a public microservice
- [ ] Review a sample blameless post-mortem and identify structural shortcomings
- [ ] Outline how you would automate a manual task you did recently (e.g. database schema migrations or backups)
