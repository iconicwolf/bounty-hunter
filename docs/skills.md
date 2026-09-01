# 🛠️ BountyHunter Agent Skill Matrix

This document defines the specific capabilities and tools available to the agents within the BountyHunter ecosystem. Each agent's "Mission" is supported by these technical skills.

## 🏹 The Hunter (Sourcing Agent)
**Mission**: Find and track high-match job opportunities.

| Skill | Tool/Technology | Description |
| :--- | :--- | :--- |
| `live_search` | SerpApi (Google Jobs) | Performs real-time queries across Google Jobs and other aggregators. |
| `profile_matching` | Pydantic / Logic | Compares job descriptions against `UserProfile` skills to calculate a match score. |
| `web_scraping` | Playwright / BeautifulSoup | Extracts detailed job requirements and application links from target pages. |
| `app_tracking` | SQLAlchemy | Automatically injects found roles into the `Applications` table. |

## 👹 The Adversary (Chaos Agent)
**Mission**: Stress-test the application to find vulnerabilities.

| Skill | Tool/Technology | Description |
| :--- | :--- | :--- |
| `fuzzing` | HTTPX | Sends malformed JSON and unexpected payloads to API endpoints. |
| `injection_testing` | SQL Payloads | Attempts basic SQL injection strings to verify database security. |
| `state_breaking` | API Sequence | Tries to trigger crashes by calling endpoints in an invalid order (e.g., accessing data before profile setup). |
| `latency_simulation` | Timeout triggers | Tests how the app handles slow database responses. |

## 💎 The Refiner (Optimization Agent)
**Mission**: Analyze failures and evolve the codebase.

| Skill | Tool/Technology | Description |
| :--- | :--- | :--- |
| `failure_analysis` | Log Parser | Analyzes Tracebacks and error codes from the Adversary's runs. |
| `pattern_recognition` | Logic | Identifies if a bug is a one-off or a systemic architectural flaw. |
| `code_evolution` | AST / Refactoring | Proposes and implements structural changes to prevent recurring bugs. |
| `rigor_audit` | Testing Suite | Verifies that the "fix" actually resolves the vulnerability without introducing regressions. |

---

## 🔄 Skill Interaction Loop
1. **Hunter** sources $\rightarrow$ **Refiner** ensures the sourcing logic is efficient.
2. **Adversary** breaks $\rightarrow$ **Refiner** implements the fix.
3. **Hunter** applies $\rightarrow$ **Adversary** checks if the application flow is robust.
