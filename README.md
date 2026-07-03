# 🐍 Python for AI Engineering

A structured 2-week Python learning sprint focused exclusively on the skills needed to build **production-grade AI applications** — LLM pipelines, agentic systems, and AI APIs.

This is not a general Python course. Every topic here has a direct line to real-world AI engineering with **LangChain**, **LangGraph**, **LangSmith**, and the broader LLM ecosystem.

---

## 👤 About This Repository

This repo documents a personal learning journey from **Engineering Manager → AI Engineer**, built by someone with 15+ years of software development experience who wanted to close the gap between general Python knowledge and AI-specific engineering patterns.

Progress is committed daily, one folder per day, with working code examples and exercises.

---

## 🎯 Who Can Benefit From This

This repo is for you if:

- You're an **experienced software engineer** (any language) transitioning into AI engineering
- You're a **Python developer** who wants to level up specifically for LLM application development
- You're a **tech lead or engineering manager** moving hands-on into the AI space
- You understand programming fundamentals and want to **skip the basics** and go straight to patterns that matter in production AI systems

This is **not** for absolute beginners. If you're new to programming, start with a general Python course first.

---

## 🗺️ The 2-Week Curriculum

### Week 1 — Core Python for AI Systems

| Day | Topic | Key Concepts |
|-----|-------|-------------|
| **Day 01** | Python Environment & Tooling | pyenv, Poetry, pyproject.toml, VS Code setup, Ruff, pre-commit |
| **Day 02** | Type System & Pydantic v2 | Type hints, TypedDict, BaseModel, validators, serialization, LLM I/O schemas |
| **Day 03** | Async Python | asyncio, async/await, gather, queues, streaming responses, httpx |
| **Day 04** | Generators & Iterators | yield, async generators, itertools, lazy evaluation, token streaming |
| **Day 05** | Decorators & Context Managers | Stacking decorators, functools, contextlib, retry wrappers, tracing |
| **Weekend** | Review & Reinforce | Revisit async project, read LangChain source, Pydantic challenges |

### Week 2 — Advanced Patterns for AI Application Dev

| Day | Topic | Key Concepts |
|-----|-------|-------------|
| **Day 08** | OOP Patterns in AI Frameworks | ABCs, Protocols, Mixins, Factory pattern, LangChain class hierarchy |
| **Day 09** | Concurrency & Performance | GIL, ThreadPoolExecutor, parallel LLM calls, semaphores, profiling |
| **Day 10** | Data Handling & Parsing | JSON encoders, LLM output parsing, regex extraction, orjson, YAML |
| **Day 11** | Testing & Observability | pytest, mocking LLM calls, structlog, OpenTelemetry, snapshot testing |
| **Day 12** | Production FastAPI | Async endpoints, WebSocket streaming, dependency injection, Docker |
| **Weekend** | Capstone Project | Full LLM pipeline app — async + streaming + Pydantic + FastAPI + tests |

---

## 🏗️ Repository Structure

```
python-ai-engineering/
│
├── week1/
│   ├── day01_tooling/
│   │   └── notes.md
│   ├── day02_types_pydantic/
│   │   ├── type_system.py
│   │   ├── pydantic_basics.py
│   │   └── llm_schemas.py
│   ├── day03_async/
│   ├── day04_generators/
│   └── day05_decorators/
│
├── week2/
│   ├── day08_oop_patterns/
│   ├── day09_concurrency/
│   ├── day10_data_parsing/
│   ├── day11_testing/
│   └── day12_fastapi/
│
├── capstone/
│   └── llm_pipeline_app/
│
├── pyproject.toml
├── poetry.lock
├── .env.example
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| **Runtime** | Python 3.11+, pyenv |
| **Dependency Management** | Poetry, pyproject.toml |
| **Type Safety** | Pydantic v2, typing, mypy |
| **Async & HTTP** | asyncio, httpx |
| **API Framework** | FastAPI |
| **LLM SDKs** | openai, anthropic |
| **AI Frameworks** | LangChain, LangGraph *(coming next)* |
| **Testing** | pytest, pytest-asyncio, pytest-mock |
| **Observability** | structlog, OpenTelemetry |
| **Linting & Formatting** | Ruff, Black |
| **Environment** | VS Code, Jupyter Notebooks, Docker |

---

## 🚀 Getting Started

### Prerequisites

- macOS / Linux / Windows (WSL2)
- Python 3.11+ via [pyenv](https://github.com/pyenv/pyenv)
- [Poetry](https://python-poetry.org/) for dependency management
- VS Code with Python + Pylance + Ruff extensions

### Setup

```bash
# Clone the repo
git clone https://github.com/yourusername/python-ai-engineering.git
cd python-ai-engineering

# Install dependencies
poetry install

# Copy environment variables
cp .env.example .env
# Add your API keys to .env

# Activate the environment
poetry shell
```

### Environment Variables

```bash
# .env.example
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
```

---

## 📈 Learning Outcomes

By the end of this sprint, you will be able to:

- ✅ Write fully typed, async Python with confidence
- ✅ Design Pydantic schemas for LLM inputs and outputs
- ✅ Handle streaming token output from any LLM provider
- ✅ Build retry and rate-limit wrappers for LLM APIs
- ✅ Run parallel LLM calls without exceeding rate limits
- ✅ Parse and validate unstructured LLM responses robustly
- ✅ Write tests for AI code including mocking LLM calls
- ✅ Expose AI logic via a production-ready FastAPI server
- ✅ Read and understand LangChain and LangGraph source code
- ✅ Architect a Python AI application from scratch

---

## 🔭 What Comes Next

This repo is **Phase 1** of a longer AI engineering journey:

| Phase | Focus |
|-------|-------|
| **Phase 1** *(this repo)* | Python foundations for AI engineering |
| **Phase 2** | LangChain — chains, prompts, retrievers, memory |
| **Phase 3** | LangGraph — stateful agents, multi-agent systems |
| **Phase 4** | LangSmith — tracing, evaluation, observability |
| **Phase 5** | Production deployment — RAG systems, agent APIs |

---

## 📝 Commit Convention

Daily progress follows this commit style:

```
day02: add Pydantic v2 fundamentals and LLM I/O schemas
day03: implement async streaming client with httpx
capstone: complete LLM pipeline with FastAPI streaming endpoint
```

---

## 📄 License

MIT — use anything here freely for your own learning.

---

<div align="center">
  <sub>Built with focus and coffee · AI Engineering Sprint · 2025</sub>
</div>
