# 🏗️ System Architecture: The Executive Suite

BountyHunter is engineered as a **Reference Implementation** of an Agentic Career OS. It moves beyond a simple application to create a governed pipeline for professional growth.

## 🎯 Design Philosophy: "The Executive Suite"
The system is designed to evoke the feeling of a high-end corporate command center. This is not just a visual choice, but a functional one: the UI is built to present high-density, high-fidelity data that allows a user to make "Executive Decisions" quickly.

### 1. The Source of Truth (DesignerAgent)
Unlike traditional apps where CSS is static, BountyHunter treats its aesthetics as a managed asset.
- **Dynamic Branding**: The `DesignerAgent` maintains the brand palette and typography.
- **Runtime Injection**: The frontend fetches these specifications via API on load and injects them as CSS variables.
- **Brand Audit**: The system can self-audit; the `DesignerAgent` reads the rendered HTML to ensure brand integrity.

## ⚙️ Technical Stack
The architecture follows a strict separation of concerns to ensure scalability and rigor.

### Layer 1: The Interface (Frontend)
- **Framework**: Vue.js (Composition API)
- **Styling**: Tailwind CSS + Glassmorphism
- **State**: Reactive bindings to the FastAPI backend via Axios.

### Layer 2: The Orchestration (Backend API)
- **Framework**: FastAPI (Asynchronous)
- **Data Layer**: PostgreSQL + SQLAlchemy (ACID compliant)
- **Validation**: Pydantic schemas for all request/response cycles.

### Layer 3: The Intelligence (Council of Agents)
The system's core logic is distributed across specialized agents:
- **Sourcing**: `HunterAgent` $\rightarrow$ SerpApi $\rightarrow$ Playwright (Evidence).
- **Governance**: `ExecutiveAgent` $\rightarrow$ Requirements $\rightarrow$ Quality Gates.
- **Hardening**: `AdversaryAgent` $\rightarrow$ `RefinerAgent` (Chaos Loop).
- **Aesthetics**: `DesignerAgent` $\rightarrow$ Brand Specs.

## 🔄 The Autonomous Pipeline
The most critical architectural feature is the **Auto-Apply Pipeline**:
1. **Sourcing**: Hunter finds a role.
2. **Scoring**: Hunter calculates a `match_score` based on the user's professional persona.
3. **Decision**: If `auto_apply` is enabled and `match_score` $\ge 70\%$, the system automatically transitions the record to `Applied`.
4. **Evidence**: A real-time screenshot is captured via Playwright to provide a permanent record of the job as it existed at the time of application.

## 🛡️ Security & Rigor
To prevent the "AI Hallucination" problem, BountyHunter implements:
- **Adversarial Testing**: The `AdversaryAgent` constantly attempts to break the API.
- **Human-in-the-loop**: While sourcing is autonomous, the "Executive" role ensures a human can audit and override any action.
