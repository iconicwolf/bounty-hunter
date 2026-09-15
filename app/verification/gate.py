import requests
import os
import sys

def verify_api():
    print("Checking API Health...")
    import time
    for i in range(5):
        try:
            res = requests.get("http://127.0.0.1:8000/", timeout=5)
            if res.status_code == 200:
                print("✅ API is Online")
                return True
        except Exception:
            print(f"Waiting for API... (Attempt {i+1}/5)")
            time.sleep(2)
    print("❌ API Offline after 5 attempts")
    return False

def verify_ui_theme():
    print("Auditing UI Theme for Blue Tones...")
    forbidden_patterns = ["blue", "#0A192F", "#020C1B", "#112240", "rgba(17, 34, 64"]
    ui_path = "/app/frontend/index.html"

    if not os.path.exists(ui_path):
        print(f"❌ UI file not found at {ui_path}")
        return False

    with open(ui_path, "r", encoding="utf-8") as f:
        content = f.read().lower()
        for pattern in forbidden_patterns:
            if pattern.lower() in content:
                print(f"❌ Theme Violation Found: '{pattern}' is still in the UI.")
                return False

    print("✅ UI Theme is Neutral (No Blue)")
    return True

def run_gate():
    all_pass = True

    if not verify_api(): all_pass = False
    if not verify_ui_theme(): all_pass = False

    if all_pass:
        print("\n🌟 UNIVERSAL GATE PASSED: System is stable and theme-compliant.")
        sys.exit(0)
    else:
        print("\n🚨 UNIVERSAL GATE FAILED: Fix violations before delivery.")
        sys.exit(1)

if __name__ == "__main__":
    run_gate()
