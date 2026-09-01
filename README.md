# 🎯 BountyHunter: Agentic Career OS

BountyHunter is a high-performance, agentic career automation system. Unlike a simple job tracker, BountyHunter uses a **Council of Agents** to source, match, and track job opportunities while utilizing "Chaos Engineering" to ensure the system is rigorous and production-ready.

![BountyHunter Logo](https://via.placeholder.com/800x400?text=BountyHunter+Logo+-+Crosshair+and+Briefcase)

## 🌟 Core Capabilities

### 1. Live Agentic Sourcing (The Hunter)
The **Hunter Agent** doesn't just search; it hunts.
- **Live Sourcing**: Integrates with the Google Jobs API to find the latest postings across the entire web.
- **Intelligent Matching**: Uses your professional profile to calculate a "Match Score" for every job found.
- **Auto-Tracking**: Automatically adds high-match roles to your application tracker.

### 2. Chaos-Driven Rigor (The Adversary & Refiner)
BountyHunter is built to be unbreakable.
- **Continuous Breaking**: The **Adversary Agent** constantly attacks the API with SQL injections and malformed data.
- **Self-Healing**: The **Refiner Agent** analyzes these attacks and implements architectural improvements to harden the system.

### 3. Professional Identity Management
- **Persona-Based Search**: The agent acts on behalf of your unique professional identity (skills, achievements, target roles).
- **Granular Filtering**: Control exactly what the agent hunts for (Salary, Location, Remote/On-site).

---

## 🛠️ Technology Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend** | [FastAPI](https://fastapi.tiangolo.com/) | High-performance asynchronous API. |
| **Database** | [PostgreSQL](https://www.postgresql.org/) | Persistent, ACID-compliant data storage. |
| **ORM** | [SQLAlchemy](https://www.sqlalchemy.org/) | Object-relational mapping for clean data logic. |
| **Agents** | [Playwright](https://playwright.dev/) | Browser automation for job sourcing and evidence capture. |
| **Search** | [SerpApi](https://serpapi.com/) | Real-time Google Jobs data access. |
| **Infrastructure** | [Docker](https://www.docker.com/) | Containerized, environment-agnostic deployment. |

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- Docker & Docker Compose installed.
- A [SerpApi Key](https://serpapi.com/).

### 2. Setup & Launch
```bash
# Clone the repository
git clone https://github.com/iconicwolf/bounty-hunter.git
cd bounty-hunter

# Configure environment
cp .env.example .env
# Edit .env and add your SERPAPI_KEY

# Launch the system
docker-compose up --build -d
```

### 3. Using the Application
1. **Set Your Profile**: Go to `http://localhost:8001/docs` $\rightarrow$ `POST /profile`.
2. **Configure Filters**: Go to `POST /filters` to define your ideal job.
3. **Deploy the Hunter**: Call `POST /agents/hunter/search` to begin the sourcing cycle.
4. **Track Results**: View your matched jobs at `GET /applications`.

---

## 🎓 Learning Center (Concepts Used)

For beginners wanting to learn how this was built, here are the key concepts:

### 🏗️ MVC Architecture
We use **Model-View-Controller**. 
- **Models**: Define how data is stored (SQLAlchemy).
- **Views/Schemas**: Define how data is sent/received (Pydantic).
- **Controllers**: Handle the logic and routes (FastAPI endpoints).

### 🤖 Agentic Loops
Unlike a standard script, an agentic loop consists of:
`Perception (Sourcing)` $\rightarrow$ `Analysis (Matching)` $\rightarrow$ `Action (Tracking)` $\rightarrow$ `Critique (Refining)`.

### 🐳 Containerization
Docker ensures the app runs the same on your machine as it does on mine by packaging the OS, Python version, and database together.

---

## 📸 Screenshots & Evidence
*(Screenshots will be automatically captured by the Playwright agent during the Application phase)*

- **API Dashboard**: `[Screenshot: /docs]`
- **Agent Logs**: `[Screenshot: Hunter Agent Console]`
- **Database State**: `[Screenshot: pgAdmin Tables]`
