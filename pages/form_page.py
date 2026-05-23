"""
form_page.py
------------
Page Object for the Dropdown and Inputs pages at:
  https://the-internet.herokuapp.com/dropdown
  https://the-internet.herokuapp.com/inputs
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class DropdownPage(BasePage):
    """
    Represents the Dropdown page.
    Demonstrates how to interact with <select> elements.
    """

    PATH = "/dropdown"

    # Locators
    DROPDOWN = (By.ID, "dropdown")

    def open_dropdown_page(self):
        self.open(self.PATH)

    def select_option_by_text(self, visible_text: str):
        """
        Selects a dropdown option by its visible label.

        Example: select_option_by_text("Option 1")
        """
        dropdown_element = self.find(*self.DROPDOWN)
        select = Select(dropdown_element)  # Selenium's built-in Select helper
        select.select_by_visible_text(visible_text)

    def select_option_by_value(self, value: str):
        """Selects a dropdown option by its HTML value attribute."""
        dropdown_element = self.find(*self.DROPDOWN)
        select = Select(dropdown_element)
        select.select_by_value(value)

    def get_selected_option(self) -> str:
        """Returns the text of the currently selected option."""
        dropdown_element = self.find(*self.DROPDOWN)
        select = Select(dropdown_element)
        return select.first_selected_option.text

    def get_all_options(self) -> list[str]:
        """Returns all dropdown option texts as a list."""
        dropdown_element = self.find(*self.DROPDOWN)
        select = Select(dropdown_element)
        return [option.text for option in select.options]


class InputsPage(BasePage):
    """
    Represents the Inputs page (a number input field).
    Demonstrates typing into form fields and reading values.
    """

    PATH = "/inputs"

    # Locators
    NUMBER_INPUT = (By.CSS_SELECTOR, "input[type='number']")

    def open_inputs_page(self):
        self.open(self.PATH)

    def enter_number(self, number):
        """Types a number into the input field."""
        self.type_text(*self.NUMBER_INPUT, str(number))

    def get_input_value(self) -> str:
        """Returns the current value in the input field."""
        return self.find(*self.NUMBER_INPUT).get_attribute("value")

    def clear_input(self):
        """Clears the input field."""
        self.find(*self.NUMBER_INPUT).clear()
