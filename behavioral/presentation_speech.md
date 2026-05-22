# Natural Presentation Speech (10 Minutes) - SRE Focused

> **Estimated Length**: ~1,300 words (Speech only).
> **Tone**: Natural, conversational, and direct. Addressed to a single interviewer.
> **Focus**: Site Reliability Engineering (SRE), systems, scale, and performance.

---

Hi, thanks for taking the time to talk today. I wanted to give you a direct walkthrough of my background, the projects I’ve worked on over the past five years, and the engineering choices I’ve had to make along the way.

To give you some context, I’ve spent the last five years working full-time as a software engineer while completing both my Bachelor’s in Computer Engineering at Politecnico di Milano—where I also covered networking protocols through the CCNA curriculum—and my Master’s in Computer Science at Sapienza. Balancing both was demanding, but it was highly practical. Everything I learned in my courses about databases, distributed systems, or machine learning, I immediately applied to the systems I was building at work. And when I ran into production bugs or performance issues, I had the theoretical depth to understand exactly why they were happening.

### Backend Development and Automation

I started my career doing core backend development. In my role at NTT DATA, I worked with Java, Spring, and JavaEE. Most of my work was focused on integration. We had to integrate an enterprise software system called Zarathustra into our existing infrastructure. This involved architecting data pipelines, designing REST APIs, and implementing secure JWT authentication. 

While working there, I noticed we were wasting a lot of time on manual resume screening, so I built a CV scraping tool to automate the workflow. The tool used simple NLP to parse raw resume text and extract key information like contact details and skills, then scored each candidate by matching their skills against a set of predefined keyword points. It was a simple utility, but it saved the team hours of manual data entry and taught me the value of automation early on.

### Designing for Scale: The FNOMCeO Registry

After NTT DATA, I worked on a registry project for FNOMCeO, the National Federation of Doctors and Dentists in Italy. This was my first time dealing with real scale. The goal was to build a new national registry that could reliably support about 460,000 users. 

I started by conducting a detailed assessment of their legacy architecture, which was monolithic, slow, and prone to failures. I spearheaded the plan to transition them to a decoupled, cloud-based microservices architecture on AWS. The design used Docker containers managed by Amazon ECS, with an API Gateway routing traffic to the microservices. To handle concurrent traffic spikes without locking the database, I set up Amazon RDS with read-replicas and implemented an ElastiCache Redis layer for fast data retrieval. This project really shifted my mindset from just writing code to thinking about system design, cloud reliability, and how infrastructure behaves under heavy load.

### Horizon Europe: UI State Machines and On-Device Models

Next, I transitioned into working on European research projects under the Horizon Europe program. These projects allowed me to merge my systems engineering background with machine learning, focusing on taking theoretical AI models and building the production systems around them.

For the PREVENT-PCP project, which focused on security in public transport systems across Europe, I developed a Python-based evaluation framework to benchmark different security prototypes. We had to ingest data from various third-party security systems, normalize it, and calculate performance metrics. I built an interactive dashboard using Streamlit to visualize these KPIs, allowing public procurement teams to make evidence-based decisions when choosing security technologies.

I also worked on the ARIEN project, which aimed to help law enforcement track drug trafficking and analyze financial flows. I built the frontend using Angular to visualize massive, interconnected graphs of transactions. The challenge was rendering complex, real-time data in a way that investigators could easily use to make quick decisions.

Another key project was SmartSense, which focused on secure urban environments. I engineered a cross-platform mobile application using Ionic, alongside a companion smartwatch app built in Java. The smartwatch app ran an on-device gesture recognition CNN model to detect emergency movements and send an SOS signal. The main challenge here was synchronization and state management; we had to translate complex BPMN workflow diagrams into functional, reactive state machines inside the mobile app to ensure the watch and phone stayed in sync in real time.

### Master’s Thesis: Optimizing AI for the Edge

This experience with hardware and resource constraints led directly to my Master’s thesis at Sapienza. My research focused on driving activity detection using smartwatch inertial sensors. The goal was to classify driving movements, turns, and steering actions in real time to monitor driver behavior.

The main challenge was the physical hardware constraints. Running a deep neural network continuously on a smartwatch processor will quickly drain the battery and overheat the device. I had to optimize a multi-head 1D-CNN model for edge inference. 

Using TensorFlow Lite, I quantized the model weights from 32-bit floats to 8-bit integers and pruned unnecessary connections in the network. This reduced the final memory footprint of the model to just 257.6 KB. Despite this tiny size, we achieved a 96% classification accuracy. I also designed the on-device pre-processing pipeline, using median filtering to clean up accelerometer and gyroscope sensor noise, and window segmentation to analyze the movements in real time with minimal latency. It was a great exercise in writing highly optimized code under tight hardware constraints.

### Why Google SRE?

When I look at the Site Reliability Engineering role at Google, it aligns perfectly with the engineering challenges I enjoy solving. SRE is about scaling distributed systems, automating away toil, and ensuring services remain highly available and reliable under heavy load.

I’ve spent the last five years building scalable backend services, designing decoupled cloud architectures, and writing optimized code for highly constrained environments. Additionally, I am actively studying for the LPIC Linux certification and have built a strong foundation in network protocols and administration. This gives me a deep understanding of core OS internals, process management, and network troubleshooting, which are essential for diagnosing low-level infrastructure issues. 

I enjoy digging into system failures, understanding bottlenecks, and building automated guardrails to prevent incidents before they affect users. My background in both hands-on systems engineering and ML optimization has taught me how to approach problems systematically, which is exactly the mindset needed to keep Google's infrastructure running reliably.

That’s a quick summary of my background. I’d love to answer any questions you have or dive deeper into any of these projects.

---

## ❓ Potential Interviewer Questions & Answers

### Q1: How did you approach planning the high-level cloud architecture for the FNOMCeO registry to support 460k users?
**Answer:** "Since this was an abstract design phase to modernize a legacy monolith, my goal was to propose a highly decoupled, scalable architecture that would eliminate their database locking problems. I proposed containerizing their services using Docker and deploying them on AWS ECS for easy scaling. To handle read-heavy traffic spikes, I structured a model where the primary write database offloaded read operations to AWS RDS read-replicas. Additionally, I planned an ElastiCache Redis layer to cache registry data, ensuring fast retrieval times and protecting the database from concurrent read spikes."

### Q2: How did you build the CV scraping automation tool to handle resume parsing?
**Answer:** "I built the tool in Java, using open-source libraries like Apache POI to parse Word documents and Apache PDFBox to read PDFs. Resumes vary widely in layout, so instead of relying on structural document position, I focused on extracting the raw text and using key-phrase indexing and pattern matching to pull out critical blocks like contact information, work history, and core skills. The tool scored candidates by matching their skills against predefined keyword profiles, which helped streamline our initial screening process."

### Q3: Why did you choose a 1D-CNN instead of an LSTM or GRU for the driving activity detection thesis?
**Answer:** "While LSTMs and GRUs are great for sequential data, they are highly sequential in their computation, which makes them slow and computationally expensive to run on a low-power smartwatch CPU. A 1D-CNN, on the other hand, performs convolutions across the time dimension using sliding windows, which can be heavily parallelized. This resulted in significantly faster inference times and a much smaller memory footprint, which was critical for squeezing the model down to 257 KB using TensorFlow Lite without draining the watch battery."

### Q4: On the Horizon Europe projects, how did you manage the transition from research models to production-ready software?
**Answer:** "Since I was responsible for both the research algorithms and the software engineering, I had to ensure that our AI logic didn't just stay in a prototype phase. I designed the code from day one with clear boundaries—separating the data ingestion pipelines, the model inference logic, and the user interface. I used strict input-output validation and standardized API contracts, which allowed me to update and retrain the tracking or benchmarking models without having to rebuild the surrounding application infrastructure."

---

## 📝 CV-Based STAR Stories

### Story 1: Designing the Cloud Registry Migration (FNOMCeO)
* **Tags**: `system-design` `scalability` `sre`
* **Situation:** The existing national registry for FNOMCeO was built on a monolithic legacy architecture that suffered from frequent database locks and sluggish queries, threatening its reliability for ~460,000 users.
* **Task:** I was tasked with analyzing their legacy setup and designing an abstract cloud-based architecture to resolve these bottlenecks and modernize the system.
* **Action:** 
  - Analyzed database queries and legacy system behaviors to pinpoint locking bottlenecks.
  - Designed a high-level AWS-based microservices architecture using containerized services on Amazon ECS.
  - Proposed an API Gateway for routing and service isolation.
  - Planned a database strategy using RDS read-replicas to separate write and read loads, alongside a Redis caching layer (ElastiCache) to serve frequent reads without touching the persistent DB.
* **Result:** The proposed architecture was approved by stakeholders, and the cloud transition is currently in progress. Once fully rolled out, the design is expected to eliminate database locking issues and scale to support the 460k users reliably.

### Story 2: Squeezing a CNN onto a Smartwatch (Master's Thesis)
* **Tags**: `optimization` `edge-computing` `problem-solving`
* **Situation:** Running a deep learning model for real-time driving activity detection on a smartwatch was draining the battery in less than two hours and causing the processor to overheat.
* **Task:** My goal was to optimize a multi-head 1D-CNN model so it could run continuous on-device inference within the tight memory and power constraints of a wearable device.
* **Action:**
  - Used TensorFlow Lite to convert the model from a floating-point representation to a quantized 8-bit integer format.
  - Pruned unnecessary neural connections that didn't contribute to accuracy.
  - Re-engineered the signal pre-processing pipeline in Java, implementing lightweight median filtering and time-window segmentation to process accelerometer and gyroscope data efficiently before feeding it to the model.
* **Result:** Reduced the model's memory footprint down to 257.6 KB and kept power consumption low enough for all-day execution, while maintaining a 96% classification accuracy.

### Story 3: Unifying Unstable Prototypes (PREVENT-PCP / Horizon Europe)
* **Tags**: `collaboration` `automation` `reliability`
* **Situation:** During the PREVENT-PCP project, different research consortia delivered security prototypes that were highly inconsistent, using different data structures and running on unstable local setups, making objective benchmarking impossible.
* **Task:** I was tasked with creating a unified evaluation framework to benchmark these security systems against strict European public transport safety KPIs.
* **Action:**
  - Defined a standard JSON data schema that all prototypes had to implement to send data.
  - Built a Python-based evaluation framework that ingested, validated, and normalized data from all systems.
  - Integrated automated metric calculation algorithms.
  - Engineered an interactive Streamlit dashboard to display performance comparisons dynamically.
* **Result:** Successfully evaluated all prototypes under identical conditions. The dashboard provided transparent, data-driven comparisons that directly facilitated evidence-based procurement decisions for European public transit authorities.
