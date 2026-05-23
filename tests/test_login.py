"""
test_login.py
-------------
Tests for the Login page.
Site: https://the-internet.herokuapp.com/login

Valid credentials:
  username: tomsmith
  password: SuperSecretPassword!
"""

import pytest
from pages.login_page import LoginPage


class TestLogin:
    """Groups all login-related tests together."""

    # ── Test 1: Successful login ─────────────────────────────

    def test_valid_login(self, driver):
        """
        GIVEN I'm on the login page
        WHEN  I enter correct credentials and click Login
        THEN  I should see a success message and be logged in
        """
        page = LoginPage(driver)
        page.open_login_page()

        page.login(username="tomsmith", password="SuperSecretPassword!")

        # Assert the success message contains the expected text
        assert "You logged into a secure area!" in page.get_success_message()

        # Also confirm the logout button is visible
        assert page.is_logged_in(), "Expected to be logged in but logout button not found"

    # ── Test 2: Wrong password ───────────────────────────────

    def test_invalid_password(self, driver):
        """
        GIVEN I'm on the login page
        WHEN  I enter a wrong password
        THEN  I should see an error message
        """
        page = LoginPage(driver)
        page.open_login_page()

        page.login(username="tomsmith", password="wrongpassword")

        error_msg = page.get_error_message()
        assert "Your password is invalid!" in error_msg

    # ── Test 3: Wrong username ───────────────────────────────

    def test_invalid_username(self, driver):
        """
        GIVEN I'm on the login page
        WHEN  I enter a username that doesn't exist
        THEN  I should see an error message
        """
        page = LoginPage(driver)
        page.open_login_page()

        page.login(username="notauser", password="SuperSecretPassword!")

        error_msg = page.get_error_message()
        assert "Your username is invalid!" in error_msg

    # ── Test 4: Login then logout ────────────────────────────

    def test_login_then_logout(self, driver):
        """
        GIVEN I've successfully logged in
        WHEN  I click the logout button
        THEN  I should be redirected back to the login page
        """
        page = LoginPage(driver)
        page.open_login_page()

        page.login(username="tomsmith", password="SuperSecretPassword!")
        assert page.is_logged_in()

        page.logout()

        # After logout we should be back on the login page
        assert "/login" in page.get_current_url()

    # ── Test 5: Parametrized invalid logins ─────────────────

    @pytest.mark.parametrize("username, password, expected_error", [
        ("",         "SuperSecretPassword!", "Your username is invalid!"),
        ("tomsmith", "",                     "Your password is invalid!"),
        ("",         "",                     "Your username is invalid!"),
    ])
    def test_empty_fields(self, driver, username, password, expected_error):
        """
        Tests multiple bad-credential combinations in one go.
        pytest.mark.parametrize runs this test once per row above.
        """
        page = LoginPage(driver)
        page.open_login_page()

        page.login(username=username, password=password)

        assert expected_error in page.get_error_message()
