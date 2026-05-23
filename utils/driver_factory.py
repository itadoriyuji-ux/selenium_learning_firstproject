"""
driver_factory.py
-----------------
Responsible for creating and configuring the Selenium WebDriver.
Using webdriver-manager means you never need to manually download ChromeDriver.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def get_driver(browser: str = "chrome", headless: bool = False):
    """
    Creates and returns a WebDriver instance.

    Args:
        browser:  "chrome" or "firefox"
        headless: If True, runs the browser in the background (no window)
                  Useful for CI/CD pipelines.

    Returns:
        A configured WebDriver instance.
    """
    browser = browser.lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()

        if headless:
            # Run without opening a visible browser window
            options.add_argument("--headless=new")

        # These options make Chrome more stable in various environments
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        # webdriver-manager auto-downloads the correct ChromeDriver version
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()

        if headless:
            options.add_argument("--headless")

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )

    else:
        raise ValueError(f"Unsupported browser: '{browser}'. Use 'chrome' or 'firefox'.")

    # Wait up to 10s for elements to appear before throwing an error
    driver.implicitly_wait(10)

    # Open the browser maximized
    driver.maximize_window()

    return driver
