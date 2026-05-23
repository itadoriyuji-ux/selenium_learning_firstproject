"""
test_forms.py
-------------
Tests for the Dropdown and Inputs pages.
Sites:
  https://the-internet.herokuapp.com/dropdown
  https://the-internet.herokuapp.com/inputs
"""

import pytest
from pages.form_page import DropdownPage, InputsPage


class TestDropdown:
    """Tests for the Dropdown page."""

    def test_default_option_is_please_select(self, driver):
        """
        GIVEN I open the dropdown page
        THEN  the default selected option should be 'Please select an option'
        """
        page = DropdownPage(driver)
        page.open_dropdown_page()

        assert page.get_selected_option() == "Please select an option"

    def test_select_option_1(self, driver):
        """
        GIVEN I'm on the dropdown page
        WHEN  I select 'Option 1'
        THEN  the selected value should be 'Option 1'
        """
        page = DropdownPage(driver)
        page.open_dropdown_page()

        page.select_option_by_text("Option 1")

        assert page.get_selected_option() == "Option 1"

    def test_select_option_2(self, driver):
        """
        GIVEN I'm on the dropdown page
        WHEN  I select 'Option 2' by its value
        THEN  the selected value should be 'Option 2'
        """
        page = DropdownPage(driver)
        page.open_dropdown_page()

        page.select_option_by_value("2")

        assert page.get_selected_option() == "Option 2"

    def test_dropdown_has_three_options(self, driver):
        """
        GIVEN I'm on the dropdown page
        THEN  the dropdown should have exactly 3 options
        """
        page = DropdownPage(driver)
        page.open_dropdown_page()

        options = page.get_all_options()

        # Expect: ['Please select an option', 'Option 1', 'Option 2']
        assert len(options) == 3

    @pytest.mark.parametrize("option_text", ["Option 1", "Option 2"])
    def test_can_select_any_option(self, driver, option_text):
        """Parametrized test: verifies both options can be selected."""
        page = DropdownPage(driver)
        page.open_dropdown_page()

        page.select_option_by_text(option_text)

        assert page.get_selected_option() == option_text


class TestInputs:
    """Tests for the Number Inputs page."""

    def test_enter_a_number(self, driver):
        """
        GIVEN I'm on the inputs page
        WHEN  I type a number into the field
        THEN  the field should show that number
        """
        page = InputsPage(driver)
        page.open_inputs_page()

        page.enter_number(42)

        assert page.get_input_value() == "42"

    def test_clear_input(self, driver):
        """
        GIVEN I've entered a number
        WHEN  I clear the field
        THEN  the field should be empty
        """
        page = InputsPage(driver)
        page.open_inputs_page()

        page.enter_number(99)
        page.clear_input()

        assert page.get_input_value() == ""

    def test_replace_number(self, driver):
        """
        GIVEN I've entered a number
        WHEN  I enter a different number
        THEN  the field should show the new number
        """
        page = InputsPage(driver)
        page.open_inputs_page()

        page.enter_number(10)
        page.enter_number(20)  # enter_number clears first, then types

        assert page.get_input_value() == "20"
