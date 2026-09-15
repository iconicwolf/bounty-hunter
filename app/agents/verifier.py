import os
from typing import List, Dict, Any
from sqlalchemy.orm import Session

class VerifierAgent:
    """
    The Verifier Agent acts as the final quality gate in the Loop Engineering process.
    Its purpose is to be an adversarial critic, identifying hallucinations,
    theme violations, and functional gaps before the user sees the result.
    """

    def __init__(self):
        self.project_manifest = {
            "theme": {
                "forbidden": ["blue", "#0A192F", "#020C1B", "#112240", "rgba(17, 34, 64"],
                "required": ["dark grey", "slate", "gold"]
            },
            "vision": "Career OS - Autonomous Job Application System",
            "governance": "No change is complete without evidence and verification."
        }

    async def audit_change(self, change_description: str, diff_content: str, gate_results: Dict[str, Any], evidence_folder: str = None, test_results: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Audits the ACTUAL state of the project files, the delivery process, and functional test results.
        """
        findings = []
        verdict = "PASSED"

        # 1. REAL-FILE Theme Audit
        ui_path = "/app/frontend/index.html"
        try:
            with open(ui_path, "r", encoding="utf-8") as f:
                content = f.read().lower()
                for pattern in self.project_manifest["theme"]["forbidden"]:
                    if pattern.lower() in content:
                        findings.append(f"Theme Violation: Found forbidden color/pattern '{pattern}' in index.html.")
                        verdict = "REJECTED"

                if "blue-" in content:
                    findings.append("Theme Violation: Found Tailwind 'blue-' classes in index.html.")
                    verdict = "REJECTED"
        except Exception as e:
            findings.append(f"Audit Error: Could not read UI file: {e}")
            verdict = "REJECTED"

        # 2. Evidence Audit
        if not evidence_folder:
            findings.append("Governance Violation: No evidence folder provided.")
            verdict = "REJECTED"
        else:
            evidence_path = f"/app/static/evidence/{evidence_folder}"
            try:
                if not os.path.exists(evidence_path) or not os.listdir(evidence_path):
                    findings.append(f"Evidence Violation: Folder '{evidence_folder}' is missing or empty.")
                    verdict = "REJECTED"
            except Exception as e:
                findings.append(f"Evidence Audit Error: {e}")
                verdict = "REJECTED"

        # 3. Functional Audit (Gate results)
        if not gate_results.get("api_online", True):
            findings.append("Stability Violation: The API is offline or unstable.")
            verdict = "REJECTED"

        if not gate_results.get("theme_compliant", True):
            findings.append("Theme Violation: The automated gate detected blue tones.")
            verdict = "REJECTED"

        # 4. Feature Test Audit
        if test_results:
            for test_name, passed in test_results.items():
                if not passed:
                    findings.append(f"Feature Failure: Test '{test_name}' failed. Functionality is broken.")
                    verdict = "REJECTED"

        # 5. Logic Audit
        if "TODO" in diff_content or "FIXME" in diff_content:
            findings.append("Quality Violation: Found 'TODO' or 'FIXME' markers in submitted code.")
            verdict = "REJECTED"

        return {
            "verdict": verdict,
            "findings": findings,
            "rationale": "All criteria met." if verdict == "PASSED" else "Governance or Project manifest violations found."
        }
