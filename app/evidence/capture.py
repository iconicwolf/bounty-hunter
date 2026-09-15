import asyncio
from playwright.async_api import async_playwright
import datetime
import os
import sys

async def capture_ui_evidence(folder_name: str = "default"):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = await context.new_page()

        url = "http://localhost:8000"
        print(f"Capturing high-fidelity evidence from {url}...")

        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=60000)
            await page.wait_for_selector(".executive-glass", timeout=30000)
            await asyncio.sleep(3)

            evidence_dir = os.path.join("/app/static/evidence", folder_name)
            os.makedirs(evidence_dir, exist_ok=True)

            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{timestamp}_executive_suite.png"
            filepath = os.path.join(evidence_dir, filename)

            await page.screenshot(path=filepath, full_page=True)
            print(f"✅ High-fidelity UI evidence saved to: {filepath}")
            return filepath
        except Exception as e:
            print(f"❌ Capture failed: {e}")
            try:
                content = await page.content()
                with open("/app/static/evidence/error_source.html", "w", encoding="utf-8") as f:
                    f.write(content)
                err_path = os.path.join("/app/static/evidence", "error_state.png")
                await page.screenshot(path=err_path)
            except:
                pass
            return None
        finally:
            await browser.close()

if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "default"
    asyncio.run(capture_ui_evidence(folder))

