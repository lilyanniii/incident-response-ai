# Incident Response AI

An AI-powered tool that helps SREs and DevOps engineers respond to incidents faster by searching past incidents semantically and generating root cause suggestions using an LLM.

## What it does

When an incident occurs, engineers typically spend 15-30+ minutes manually searching through past incidents, runbooks, and documentation to form a hypothesis. This tool cuts that down to seconds by:

- Searching historical incidents by **meaning**, not just keywords (e.g. "database not connecting" finds "MySQL connection pool exhausted")
- Passing the most relevant past incidents to Claude as context
- Generating root cause suggestions and troubleshooting steps based on what worked before

## Tech Stack

- **Python + FastAPI** — API layer
- **ChromaDB** — Vector database for semantic search over past incidents
- **Anthropic API (Claude)** — LLM for analysis and suggestions
- **Go** — CLI tool for interacting with the system

## Project Goals

This is a learning project built to develop hands-on experience with:

- Python and FastAPI
- Vector databases and semantic search
- RAG (Retrieval Augmented Generation) systems
- LLM API integration
- Go CLI development
- Docker and containerization

## Status

Under active development. See `PLAN.md` for architecture notes.
