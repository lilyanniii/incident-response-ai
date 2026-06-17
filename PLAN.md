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
- [x] Go fundamentals
- [x] Building CLI tools in Go
- [x] HTTP client to talk to Python API

### Phase 5: v1.0 Release
- [ ] **User-submitted incidents** — let users submit their own incidents to be stored in ChromaDB via the API *(in progress)*
  - [x] Auto-generate unique incident ID on the API (`get_last_incident` in `vector_storage.py` — reads all IDs, takes max number + 1, formats as `INC-XXXX`)
  - [ ] Storage function to add a single user-submitted incident to ChromaDB
  - [ ] POST endpoint to receive a new incident (decide: reuse `Incident` model vs. a new `NewIncident` model without `id`/`created_at`)
  - [ ] Go CLI menu — let user choose between submitting a new incident or querying existing ones
- [ ] Docker containerization — containerize FastAPI + ChromaDB for consistent deployment
- [ ] Cloud deployment — host on cloud, compile Go binary per platform, publish to GitHub Releases

> Dev convenience: `run.sh` starts the API, waits for it, then launches the CLI (cleans up the server on exit).

### Phase 6: Future Releases
- [ ] Testing strategies
- [ ] Conversation history — store message history per session and pass to Claude for follow-up questions
- [ ] Improve retrieval quality — replace synthetic data with more realistic/varied incidents, or allow importing real incident data from a JSON/CSV file via the CLI
- [ ] Optional: Slack/Discord bot, web UI, Kubernetes deployment
- [ ] Optional: User-supplied Anthropic API key — CLI prompts for key on first run, shifts billing to the user