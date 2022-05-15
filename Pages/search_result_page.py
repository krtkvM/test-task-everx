from Pages.base_page import BasePage
from data_for_tests import Data
from locators import Locator

class SearchResultPage(BasePage):

    def assert_searching_result_field(self):
        assert self.page.inner_html(Locator.searching_results_field)
        # expect(Locator.searching_results_field).to_be_visible()
    def assert_right_text_in_searching_field(self):
        assert self.page.get_attribute(Locator.searching_field, "value") == Data.TEXT_FOR_SEARCHING

    def assert_searching_result_not_found(self):
        assert self.page.inner_html(Locator.button_element_for_unsuccessful_search)
