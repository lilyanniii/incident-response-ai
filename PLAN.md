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
- [ ] Build RAG (Retrieval Augmented Generation) system
- [ ] Prompt engineering for incident analysis
- [ ] Root cause suggestion logic

### Phase 4: Go CLI
- [ ] Go fundamentals
- [ ] Building CLI tools in Go
- [ ] HTTP client to talk to Python API

### Phase 5: Polish & Extend
- [ ] Docker containerization
- [ ] Testing strategies
- [ ] Optional: Slack/Discord bot, web UI, Kubernetes deployment

## Progress Log

### Session 1 - 2026-01-21
- Defined project scope and architecture
- Chose tech stack: Python + FastAPI + ChromaDB + Go
- Decided on synthetic data approach for training/testing
- Created project folder and CLAUDE.md

### Session 2 - 2026-01-21
- Verified Python 3.12.6 installation
- Created virtual environment (`venv/`)
- Learned about virtual environments: isolation, reproducibility, why not to touch venv folder
- Discussed core dependencies: FastAPI, Uvicorn, ChromaDB, Anthropic/OpenAI
- Deep dive into vector databases and embeddings (how semantic search works, cosine similarity, RAG)

### Session 3 - 2026-01-31
- Created `requirements.txt` and installed dependencies (FastAPI, Uvicorn, ChromaDB, Anthropic)
- Built first FastAPI app with "Hello World" endpoint
- Learned FastAPI concepts: path parameters, query parameters, request body, response models
- Deep dive into API security vulnerabilities (SQL injection, DoS, info disclosure, unauthorized access, mass assignment)
- Created `LEARNINGS.md` to document key concepts
- Decided to use Anthropic (Claude Opus 4.5) for LLM integration

### Session 4 - 2026-05-15
- Learned how LLM APIs work: messages, system prompts, tokens, temperature, max_tokens
- Discussed how ChromaDB vector search scales (speed vs accuracy at large datasets)
- Discussed automated alert webhook flow (future Phase 5 feature)
- Designed incident data schema and created `models.py` with Pydantic model
- Learned about Python imports: BaseModel, Optional, datetime
- Built `data_generator.py` - generates realistic fake incidents using templates + randomization
- Learned difference between semantic search (documents) vs exact filtering (metadatas) in ChromaDB
- Decided which incident fields go into documents vs metadatas vs ids
- Started building `vector_storage.py` - connects ChromaDB, stores and searches incidents
- Fixed duplicate `service` field in `models.py`
- Discussed open sourcing: .gitignore setup, secrets management, README, licensing
- Changed learning approach: Gianni struggles first, asks specific questions when stuck

### Session 5 - 2026-05-22
- Completed `vector_storage.py` using struggle-first approach
- Built `store_incidents_in_db()` - generates 200 incidents and stores them in ChromaDB
- Built `get_similar_incidents(user_query)` - queries ChromaDB by semantic meaning, returns top 10 matches
- Learned why tags should be joined as a string (`', '.join(tags)`) rather than passed as a list for cleaner embeddings
- Confirmed ChromaDB field mapping:
  - `ids` → `incident.id`
  - `documents` → combined string of title, description, root_cause, resolution, tags (joined)
  - `metadatas` → `severity` (int), `status` (str), `service` (str)
- Phase 2 complete

## Current Status
**Working on:** Phase 3 - AI Core (RAG system)
**Next up:**
- Build RAG system: wire ChromaDB results into Claude prompt
- Prompt engineering for incident analysis
- Root cause suggestion logic

## Key Decisions
1. Using synthetic data for incidents (no real production data needed)
2. Python for AI core, Go for CLI (learning both languages)
3. Starting simple, adding complexity incrementally
4. Using Anthropic (Claude Opus 4.5) as the LLM provider

## Notes
- Gianni is a junior SRE focused on DevOps, wants to sharpen programming skills
- This is a learning project - focus on understanding concepts, not rushing through
- Gianni writes the code, Claude guides and explains