# 🎓 BountyHunter: The Complete Technical Learning Guide

Welcome to the technical deep-dive of BountyHunter. This document is designed for someone learning software engineering and agentic systems. It explains the "How" and "Why" behind every architectural decision.

---

## 🗺️ 1. The Big Picture: What is an "Agentic OS"?

Most applications are **Passive**. You click a button $\rightarrow$ the app does one thing $\rightarrow$ it stops.
**BountyHunter is Active**. It uses **Agents**. An agent is a piece of code that has:
1. **A Goal**: (e.g., "Find me a job").
2. **Tools**: (e.g., Google Search, Browser, Database).
3. **A Loop**: It perceives the environment $\rightarrow$ thinks $\rightarrow$ acts $\rightarrow$ evaluates the result $\rightarrow$ repeats.

### The BountyHunter Loop:
`Hunter (Search)` $\rightarrow$ `Refiner (Filter)` $\rightarrow$ `Adversary (Stress Test)` $\rightarrow$ `Refiner (Fix)`.

---

## 🏗️ 2. The Architecture: MVC Explained

We use the **Model-View-Controller (MVC)** pattern. This separates the data, the logic, and the presentation.

### 📦 The Model (Data Layer)
*   **Files**: `app/models/`
*   **Concept**: This is the "Source of Truth." We use **SQLAlchemy** (an ORM) to talk to **PostgreSQL**.
*   **Why?** Instead of writing raw SQL (`SELECT * FROM...`), we use Python classes. This makes the code cleaner and prevents SQL Injection attacks.

### 🖼️ The View/Schema (Data Validation Layer)
*   **Files**: `app/schemas/`
*   **Concept**: We use **Pydantic**.
*   **Why?** Pydantic ensures that if the API expects an `Integer` for salary, it doesn't get a `String`. It acts as a "filter" that catches errors before they reach the database.

### 🎮 The Controller (API Layer)
*   **Files**: `app/api/endpoints/`
*   **Concept**: **FastAPI**.
*   **Why?** FastAPI is asynchronous (`async`). It can handle thousands of requests simultaneously without blocking, which is critical when agents are scraping the web in the background.

---

## 🛠️ 3. The Infrastructure: Docker & Environment

### 🐳 Docker
Imagine you build an app that works on your computer but crashes on mine because I have a different version of Python. **Docker solves this**.
*   **Image**: A snapshot of the entire computer (OS, Python, Libs).
*   **Container**: A running instance of that image.
*   **Docker Compose**: A script that launches multiple containers (API + DB) and connects them in a private network.

### 🔑 Environment Variables (`.env`)
We never put passwords in the code. We put them in a `.env` file. The app reads these at startup. This is a critical security standard in professional software.

---

## 🤖 4. The Agent Brains

### The Hunter Agent
Uses **SerpApi** to query Google. It uses a "Matching Algorithm" to compare keywords in a job description with your professional profile. It also uses **Playwright** to capture visual evidence (screenshots) of the jobs it finds, ensuring you have a record of the original posting.

### The Adversary Agent
This is a **Chaos Agent**. It uses a technique called "Fuzzing"—sending random or malicious data to the API to see if it crashes.

### The Refiner Agent
This is the **Architect**. It reads the logs of the Adversary. If the Adversary finds a bug, the Refiner suggests a pattern to fix it.

---

## 🚀 5. Step-by-Step Flow of a Request

When you click "Search for Jobs" in the UI:
1. **Frontend**: Sends a `POST` request to `/agents/hunter/search`.
2. **FastAPI**: Receives the request and triggers a `BackgroundTasks` (so you don't have to wait for the page to load).
3. **Hunter Agent**: 
   - Pulls your `UserProfile` from the DB.
   - Pulls your `JobFilter` from the DB.
   - Calls SerpApi $\rightarrow$ gets a list of jobs.
   - Matches jobs $\rightarrow$ saves matches to `Applications` table.
4. **User**: Refreshes the `/applications` page and sees new jobs appearing in real-time.

---

## 📚 Official Learning Resources
If you want to master these, study these in order:
1. [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/) - Learn how to build APIs.
2. [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/index.html) - Learn how databases work.
3. [Docker Curriculum](https://docker-curriculum.com/) - Learn containerization.
4. [Pydantic Documentation](https://docs.pydantic.dev/) - Learn data validation.
