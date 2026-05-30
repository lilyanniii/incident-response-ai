# AI-Powered Incident Response Assistant

## Project Overview
An AI-powered tool that helps SREs and DevOps engineers respond to incidents faster by:
- Analyzing logs/metrics to detect anomalies
- Suggesting root causes based on historical incidents
- Auto-generating runbooks or troubleshooting steps
- Learning from past incidents to improve over time

## Tech Stack
- **Python** - Core AI/ML logic and API
- **FastAPI** - Modern async web framework for the API
- **ChromaDB** - Vector database for semantic search over incidents
- **Anthropic API** - Claude Opus 4.5 for LLM integration
- **Go** - CLI tool for interacting with the system
- **Docker** - Containerization

## Architecture
```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Go CLI Tool   │────▶│  Python API     │────▶│  Vector DB      │
│   (incident     │     │  (FastAPI +     │     │  (ChromaDB)     │
│    reporting)   │◀────│   LLM logic)    │◀────│                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                               │
                               ▼
                        ┌─────────────────┐
                        │  LLM Provider   │
                        │  (Anthropic/    │
                        │   OpenAI API)   │
                        └─────────────────┘
```

## Learning Path

### Phase 1: Foundations
- [x] Set up Python project structure (virtual environments, dependencies)
- [x] Learn FastAPI basics by building a simple API
- [x] Understand how LLM APIs work (prompts, tokens, responses)

### Phase 2: Data & Storage
- [x] Design incident data schema
- [x] Build synthetic data generator
- [x] Learn about embeddings and vector databases
- [x] Store and retrieve incidents semantically

### Phase 3: AI Core
- [x] Build RAG (Retrieval Augmented Generation) system
- [x] Prompt engineering for incident analysis
- [x] Root cause suggestion logic

### Phase 4: Go CLI
- [ ] Go fundamentals
- [ ] Building CLI tools in Go
- [ ] HTTP client to talk to Python API

### Phase 5: Polish & Extend
- [ ] Docker containerization
- [ ] Testing strategies
- [ ] Optional: Slack/Discord bot, web UI, Kubernetes deployment