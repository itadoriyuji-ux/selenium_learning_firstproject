"""
base_page.py
------------
The BasePage class contains actions that every page can perform.
All other page classes will inherit from this one.

This is the foundation of the Page Object Model (POM) pattern.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Base class for all page objects.

    Every page class (LoginPage, FormPage, etc.) inherits these
    common browser actions so we don't repeat ourselves.
    """

    # Base URL of the site we're testing
    BASE_URL = "https://the-internet.herokuapp.com"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

    # ──────────────────────────────────────────────
    # Navigation
    # ──────────────────────────────────────────────

    def open(self, path: str = ""):
        """Navigate to a URL. If path is given, appends it to the base URL."""
        self.driver.get(self.BASE_URL + path)

    def get_title(self) -> str:
        """Returns the current page title."""
        return self.driver.title

    def get_current_url(self) -> str:
        """Returns the current URL."""
        return self.driver.current_url

    def go_back(self):
        """Clicks the browser back button."""
        self.driver.back()

    # ──────────────────────────────────────────────
    # Finding elements
    # ──────────────────────────────────────────────

    def find(self, by: By, value: str):
        """Finds and returns a single element. Waits until it's visible."""
        return self.wait.until(
            EC.visibility_of_element_located((by, value))
        )

    def find_all(self, by: By, value: str):
        """Finds and returns all matching elements."""
        return self.driver.find_elements(by, value)

    # ──────────────────────────────────────────────
    # Interacting with elements
    # ──────────────────────────────────────────────

    def click(self, by: By, value: str):
        """Waits for an element to be clickable, then clicks it."""
        element = self.wait.until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()

    def type_text(self, by: By, value: str, text: str):
        """Clears a field and types text into it."""
        field = self.find(by, value)
        field.clear()
        field.send_keys(text)

    def get_text(self, by: By, value: str) -> str:
        """Returns the visible text content of an element."""
        return self.find(by, value).text

    def is_displayed(self, by: By, value: str) -> bool:
        """Returns True if the element is visible on the page, False otherwise."""
        try:
            return self.find(by, value).is_displayed()
        except Exception:
            return False
