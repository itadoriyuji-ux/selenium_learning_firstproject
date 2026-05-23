"""
test_navigation.py
------------------
Tests for basic page navigation and browser behaviour.
Site: https://the-internet.herokuapp.com
"""

from pages.base_page import BasePage
from pages.login_page import LoginPage


class TestNavigation:
    """Tests for general navigation around the site."""

    def test_homepage_title(self, driver):
        """
        GIVEN I open the homepage
        THEN  the page title should be 'The Internet'
        """
        page = BasePage(driver)
        page.open()  # opens the base URL

        assert page.get_title() == "The Internet"

    def test_homepage_url(self, driver):
        """
        GIVEN I open the homepage
        THEN  the URL should contain 'the-internet.herokuapp.com'
        """
        page = BasePage(driver)
        page.open()

        assert "the-internet.herokuapp.com" in page.get_current_url()

    def test_navigate_to_login_page(self, driver):
        """
        GIVEN I'm on the homepage
        WHEN  I navigate to /login
        THEN  the URL should end with /login
        """
        page = BasePage(driver)
        page.open("/login")

        assert page.get_current_url().endswith("/login")

    def test_login_page_title(self, driver):
        """
        GIVEN I navigate to the login page
        THEN  the page title should be 'The Internet'
        """
        page = LoginPage(driver)
        page.open_login_page()

        assert page.get_title() == "The Internet"

    def test_browser_back_button(self, driver):
        """
        GIVEN I've navigated from homepage to login page
        WHEN  I click back
        THEN  I should return to the homepage URL
        """
        page = BasePage(driver)
        page.open()                         # Go to homepage
        page.open("/login")                 # Navigate to login
        page.go_back()                      # Click back

        # Should be back at the root URL
        assert page.get_current_url().rstrip("/").endswith("herokuapp.com")

    def test_navigate_to_dropdown_page(self, driver):
        """
        GIVEN I navigate to /dropdown
        THEN  the URL should contain 'dropdown'
        """
        page = BasePage(driver)
        page.open("/dropdown")

        assert "dropdown" in page.get_current_url()
