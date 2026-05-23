"""
login_page.py
-------------
Page Object for the Login page at:
https://the-internet.herokuapp.com/login

Credentials that work on this site:
  Username: tomsmith
  Password: SuperSecretPassword!
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Represents the Login page.

    Contains all the locators (element IDs/selectors) and
    the actions a user can perform on this page.
    """

    # ── URL ────────────────────────────────────────
    PATH = "/login"

    # ── Locators (how we find elements on the page) ─
    # Using By.ID is the fastest and most reliable locator
    USERNAME_FIELD   = (By.ID, "username")
    PASSWORD_FIELD   = (By.ID, "password")
    LOGIN_BUTTON     = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MESSAGE  = (By.CSS_SELECTOR, "#flash.success")
    ERROR_MESSAGE    = (By.CSS_SELECTOR, "#flash.error")
    LOGOUT_BUTTON    = (By.CSS_SELECTOR, "a.button.secondary")

    # ── Actions ─────────────────────────────────────

    def open_login_page(self):
        """Navigate directly to the login page."""
        self.open(self.PATH)

    def enter_username(self, username: str):
        self.type_text(*self.USERNAME_FIELD, username)

    def enter_password(self, password: str):
        self.type_text(*self.PASSWORD_FIELD, password)

    def click_login(self):
        self.click(*self.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        """
        Full login flow: fills in credentials and submits.

        Args:
            username: The username to log in with.
            password: The password to use.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_success_message(self) -> str:
        """Returns the success flash message text after login."""
        return self.get_text(*self.SUCCESS_MESSAGE)

    def get_error_message(self) -> str:
        """Returns the error flash message text after a failed login."""
        return self.get_text(*self.ERROR_MESSAGE)

    def is_logged_in(self) -> bool:
        """Returns True if the logout button is visible (means login worked)."""
        return self.is_displayed(*self.LOGOUT_BUTTON)

    def logout(self):
        """Clicks the logout button."""
        self.click(*self.LOGOUT_BUTTON)
