"""
helpers.py
----------
Reusable helper functions used across multiple tests.
"""

import os
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# ──────────────────────────────────────────────
# Screenshot helpers
# ──────────────────────────────────────────────

def take_screenshot(driver, test_name: str) -> str:
    """
    Saves a screenshot to the /screenshots folder.

    Args:
        driver:    The active WebDriver instance.
        test_name: A label used in the filename.

    Returns:
        The file path of the saved screenshot.
    """
    # Make sure the screenshots folder exists
    screenshots_dir = os.path.join(os.path.dirname(__file__), "..", "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)

    # Build a timestamped filename so screenshots don't overwrite each other
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{test_name}_{timestamp}.png"
    filepath = os.path.join(screenshots_dir, filename)

    driver.save_screenshot(filepath)
    print(f"\n📸 Screenshot saved: {filepath}")
    return filepath


# ──────────────────────────────────────────────
# Wait helpers
# ──────────────────────────────────────────────

def wait_for_element(driver, by: By, value: str, timeout: int = 10):
    """
    Explicitly waits for an element to be visible on the page.

    Prefer this over time.sleep() — it's faster and more reliable.

    Args:
        driver:  The active WebDriver instance.
        by:      The locator strategy (e.g. By.ID, By.CSS_SELECTOR).
        value:   The locator value (e.g. "username", ".submit-btn").
        timeout: Max seconds to wait before raising an error.

    Returns:
        The WebElement once it's visible.
    """
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, value))
    )


def wait_for_text(driver, by: By, value: str, text: str, timeout: int = 10):
    """
    Waits until a specific element contains the expected text.

    Args:
        driver:  The active WebDriver instance.
        by:      Locator strategy.
        value:   Locator value.
        text:    The text to wait for.
        timeout: Max seconds to wait.

    Returns:
        True once the text is present.
    """
    return WebDriverWait(driver, timeout).until(
        EC.text_to_be_present_in_element((by, value), text)
    )
