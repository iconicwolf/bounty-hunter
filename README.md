# 🎯 BountyHunter: Agentic Career OS

BountyHunter is a high-performance, agentic career automation system. It transforms the job search from a manual chore into a targeted operation, using a **Council of Agents** to source, match, and track job opportunities.

![BountyHunter Logo](static/logo.svg)

## 🌟 Core Capabilities

### 1. Live Agentic Sourcing (The Hunter)
The **Hunter Agent** doesn't just search; it hunts.
- **Real-time Sourcing**: Integrated with SerpApi (Google Jobs) to find the latest postings across the entire web.
- **Intelligent Matching**: Uses your professional persona to calculate a "Match Score" for every job found.
- **Visual Evidence**: Uses **Playwright** to take real-time screenshots of job postings, providing a visual "paper trail" for every lead.
- **Auto-Tracking**: Automatically populates your application tracker with high-match roles.

### 2. Chaos-Driven Rigor (The Adversary & Refiner)
BountyHunter is built to be unbreakable through "Chaos Engineering."
- **Continuous Breaking**: The **Adversary Agent** constantly attacks the API with SQL injections and malformed data to find vulnerabilities.
- **Self-Healing**: The **Refiner Agent** analyzes these attacks and implements architectural improvements to harden the system.

### 3. Professional Identity Management
- **Persona-Based Search**: The agent acts on behalf of your unique professional identity (skills, achievements, target roles).
- **Granular Filtering**: Control exactly what the agent hunts for (Salary, Location, Remote/On-site).

---

## 🛠️ Technology Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend** | React/Vue + Tailwind CSS | World-class a-grade professional dashboard. |
| **Backend** | [FastAPI](https://fastapi.tiangolo.com/) | High-performance asynchronous API. |
| **Database** | [PostgreSQL](https://www.postgresql.org/) | Persistent, ACID-compliant data storage. |
| **ORM** | [SQLAlchemy](https://www.sqlalchemy.org/) | Object-relational mapping for clean data logic. |
| **Agents** | [Playwright](https://playwright.dev/) | Browser automation for sourcing and evidence capture. |
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
1. **Open Dashboard**: Open `frontend/index.html` in your browser.
2. **Set Your Persona**: Go to **Professional Persona** and enter your skills and achievements.
3. **Configure Filters**: Go to **Hunting Parameters** to define your ideal role.
4. **Deploy the Hunter**: Click **Deploy Hunter Agent** to begin the sourcing cycle.
5. **Review Bounties**: View matched jobs and their visual evidence in the **Dashboard**.

---

## 🎓 Learning Center
This project is a masterclass in modern AI engineering. Explore the `docs/` folder for:
- **TECHNICAL_GUIDE.md**: A ground-up explanation of MVC, Agentic Loops, and Docker for beginners.
- **skills.md**: A detailed matrix of agent capabilities.
