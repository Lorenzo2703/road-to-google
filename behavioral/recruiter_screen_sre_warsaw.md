# 📞 Recruiter Screen & Interview Prep: Google SRE Warsaw

This document prepares you for the initial recruiter screening and early interview stages for the **Site Reliability Engineering** position at **Google Warsaw**. It covers the specifics of the role, your personalized pitch, and strategic questions to ask.

---

## 1. The Role, Responsibilities, and Hiring Process

### The Role
Site Reliability Engineering (SRE) at Google is what happens when you ask a software engineer to design an operations team. The **Google Warsaw** office is one of the largest and most important engineering hubs for **Google Cloud** in Europe. As an SRE in Warsaw, you will likely be working on massive, globally distributed systems like Borg, Compute Engine, or core data platforms. The core mission is to ensure Google's services are fast, highly available, and scalable.

### Key Responsibilities
*   **Engineering Reliability**: Writing code (Go, Python, C++, Java) to automate operations, eliminate toil, and build resilient infrastructure.
*   **Incident Management**: Participating in on-call rotations, triaging complex production issues across the network, OS, and application layers, and leading blameless postmortems.
*   **Capacity & Performance**: Designing systems to handle hyper-growth, load balancing, and minimizing tail latency.
*   **SLOs & Error Budgets**: Working closely with product development teams to define Service Level Objectives (SLOs) and using error budgets to balance feature velocity with reliability.

### The Hiring Process
1.  **Recruiter Screen (30-45 mins)**: Focuses on your background, career goals, Googleyness, and high-level technical fit. They will test your communication and passion for SRE.
2.  **Technical Phone Screen (45-60 mins)**: Usually a coding interview (DSA) or a systems engineering/Linux internals interview. Conducted via Google Docs or a simple coding platform.
3.  **Onsite Loop (4-5 interviews, 45 mins each)**:
    *   **Coding / Algorithms**: Standard software engineering algorithmic problem-solving.
    *   **Systems Design (NALSD)**: Non-Abstract Large System Design. Designing a scalable, reliable system and analyzing failure modes.
    *   **Systems Troubleshooting / Linux Internals**: Deep dive into OS concepts, networking (TCP/IP), and debugging production issues.
    *   **Leadership & Googleyness (Behavioral)**: STAR-method questions focusing on collaboration, handling ambiguity, and the blameless SRE culture.

---

## 2. My Relevant Experience, Qualifications, and Career Goals

### Relevant Experience & Qualifications
*   **Massive Scale Architectures**: I spearheaded the cloud architecture for the national institution registry (**FNOMCeO**), which supports over **460,000+ users**. This required deep knowledge of high-availability, fault-tolerance, and consistent performance under load.
*   **Full-Stack Systems Expertise**: I have hands-on experience across the entire lifecycle. From backend services (Java, Python) to infrastructure automation (Docker, Kubernetes, AWS) and deep Linux internals. I don't just write application code; I understand how it interacts with the OS and network.
*   **Research to Production**: As a Researcher in Horizon Europe Projects (e.g., ARIEN), I developed highly available data ingestion pipelines for real-time tracking of complex flows. I know how to translate theoretical performance optimizations (like edge inference) into robust production systems.
*   **Grit and Time Management**: I successfully balanced full-time, high-level engineering roles while completing my Master's and Bachelor's degrees. I am accustomed to high-pressure environments, making me well-prepared for the incident-response rigor of Google SRE.

### Career Goals
*   **Short-Term**: I want to transition from building national-scale enterprise architectures to operating and scaling the foundational infrastructure of the internet at Google Warsaw. I want to deeply master Google's internal stack (Borg, Spanner) and immediately contribute to reducing toil through automation.
*   **Long-Term**: I aim to become a domain expert in distributed systems reliability and Non-Abstract Large System Design (NALSD). My goal is to lead architectural reviews for new Google Cloud products, ensuring they are designed for failure and extreme scale from Day 1.

---

## 3. Strategic Questions You Might Have (To Ask the Interviewer)

*Always have questions prepared. It demonstrates deep interest and system-level thinking.*

### For the Recruiter:
1.  *"I know Warsaw is a massive hub for Google Cloud. Is the SRE team I am being considered for focused more on core infrastructure (like Borg/network) or specific customer-facing GCP products?"*
2.  *"What does the typical onboarding process (often called 'SRE Bootcamp') look like for someone joining the Warsaw office?"*
3.  *"Are there specific technical gaps the Warsaw SRE teams are currently trying to fill (e.g., more networking expertise vs. more software development expertise)?"*

### For an SRE / Engineering Manager:
1.  *"Can you walk me through a recent complex incident your team handled, and how the subsequent blameless postmortem led to a systemic improvement in your architecture?"*
2.  *"How does your specific team balance feature velocity with strict error budgets? Is there ever pushback from product teams, and how is that resolved?"*
3.  *"Google SRE famously aims to cap operational toil at 50%. How is your team currently tracking against that metric, and what kind of automation are you building to reduce it further?"*
4.  *"What is the most unexpected failure mode you've encountered while scaling systems in your current domain?"*
