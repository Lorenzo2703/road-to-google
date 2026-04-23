# 🧠 Agent Engineering Fundamentals

> Core knowledge for AI agent development — essential for the Google role.

---

## LLM Fundamentals

### Key Concepts
- **Transformer Architecture**: Self-attention, multi-head attention, positional encoding
- **Tokenization**: BPE, SentencePiece, token limits
- **Inference**: Temperature, top-p, top-k, frequency/presence penalties
- **Context Window**: Managing limited context, chunking strategies
- **Fine-tuning vs Prompting**: When to use each, cost-benefit analysis

### Prompting Techniques
| Technique | Description | When to Use |
|-----------|-------------|-------------|
| Zero-shot | No examples, just instruction | Simple tasks |
| Few-shot | Provide examples in prompt | Format-specific outputs |
| Chain-of-thought | "Think step by step" | Reasoning tasks |
| Self-consistency | Multiple reasoning paths | Complex reasoning |
| ReAct | Reasoning + Acting in loops | Tool-using agents |

---

## Agent Architecture Patterns

### 1. ReAct (Reason + Act)
```
Thought → Action → Observation → Thought → Action → ... → Final Answer
```
- Most common pattern for tool-using agents
- Used by ADK, LangChain, and most frameworks

### 2. Plan-and-Execute
```
Plan (decompose into steps) → Execute each step → Synthesize results
```
- Good for complex, multi-step tasks
- Requires upfront planning capability

### 3. Multi-Agent
```
Orchestrator → Specialist Agent 1
             → Specialist Agent 2
             → Specialist Agent 3
             → Aggregator
```
- Each agent has specialized capabilities
- Orchestrator routes and coordinates

### 4. Reflexion
```
Act → Evaluate → Reflect → Act (improved) → ...
```
- Agent evaluates its own output and improves
- Useful for iterative refinement tasks

---

## Tool Use & Function Calling

### Tool Definition Best Practices
1. **Clear descriptions**: LLMs need to understand when to use each tool
2. **Strict schemas**: Use Pydantic models for input validation
3. **Error handling**: Return structured errors, not exceptions
4. **Idempotency**: Tools should be safe to retry
5. **Timeouts**: Always set timeouts for external calls

### Common Tool Types
- Search/retrieval tools
- Code execution tools
- API integration tools
- Database query tools
- File manipulation tools

---

## Testing Non-Deterministic Systems

### Challenges
- LLM outputs vary between runs
- Tool call sequences may differ
- Edge cases are hard to enumerate

### Strategies
1. **Mock the LLM**: Fixed responses for unit tests
2. **Assertion on structure**: Check format, not exact content
3. **Evaluation metrics**: BLEU, ROUGE, custom rubrics
4. **Property-based testing**: Verify invariants (e.g., "always calls auth before data access")
5. **Snapshot testing**: Compare against baseline, allow fuzzy matching

---

## Enterprise Considerations

### AI Safety
- Output filtering and content moderation
- PII detection and redaction
- Prompt injection defense
- Jailbreak prevention

### Data Residency
- Where data is stored and processed
- Compliance with GDPR, HIPAA, SOC 2
- Data sovereignty requirements

### Integration
- Connecting to existing enterprise systems (CRM, ERP, ITSM)
- Authentication and authorization (OAuth, SAML, API keys)
- Rate limiting and quotas

### Observability
- Token usage tracking and cost attribution
- Latency monitoring per component
- Error classification and alerting
- Audit logging for compliance
