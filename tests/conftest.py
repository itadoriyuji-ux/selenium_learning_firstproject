"""
conftest.py
-----------
pytest's special configuration file.

Fixtures defined here are automatically available to ALL test files
without needing to import them. Think of fixtures as setup/teardown
helpers that pytest manages for you.
"""

import pytest
from utils.driver_factory import get_driver
from utils.helpers import take_screenshot


# ──────────────────────────────────────────────────────────────
# Browser fixture
# ──────────────────────────────────────────────────────────────

@pytest.fixture(scope="function")
def driver():
    """
    Starts a browser before each test and closes it afterward.

    scope="function" means a fresh browser is created for every
    single test function. This prevents tests from affecting
    each other (known as test isolation).

    Yields the driver to the test, then quits when done.
    """
    # ── SETUP: runs before the test ────────────────
    browser = get_driver(browser="chrome", headless=False)

    yield browser  # <-- the test runs here

    # ── TEARDOWN: always runs after the test ───────
    browser.quit()


# ──────────────────────────────────────────────────────────────
# Screenshot on failure hook
# ──────────────────────────────────────────────────────────────

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    After each test, if it FAILED, automatically take a screenshot.

    This is a pytest hook — a special function pytest calls at
    specific points during a test run.
    """
    outcome = yield
    report = outcome.get_result()

    # Only act on the actual test call (not setup/teardown)
    if report.when == "call" and report.failed:
        # Get the driver from the test's fixtures if it exists
        driver = item.funcargs.get("driver")
        if driver:
            test_name = item.name.replace(" ", "_")
            take_screenshot(driver, f"FAILED_{test_name}")
