import os
import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page") or item.funcargs.get("logged_in_page")

        if page:
            os.makedirs("reports/screenshots", exist_ok=True)

            screenshot_path = os.path.join(
                "reports",
                "screenshots",
                f"{item.name}.png"
            )

            page.screenshot(
                path=screenshot_path,
                full_page=True
            )

            print(f"\nScreenshot saved: {screenshot_path}")

            