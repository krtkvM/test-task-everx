from Pages.google_main_page import GoogleMainPage
from data_for_tests import Data
from Pages.search_result_page import SearchResultPage


def test_searching(page):
    page.goto("https://www.google.com/")

    main_page = GoogleMainPage(page)
    main_page.fill_searching_field("Egils saga")
    main_page.keyboard_navigation("Enter")

    search_result_page = SearchResultPage(page)
    search_result_page.assert_searching_result_field()

def test_using_suggested_item(page):
    page.goto("https://www.google.com/")

    main_page = GoogleMainPage(page)
    main_page.fill_searching_field(Data.TEXT_FOR_SEARCHING)
    #select proposed result
    main_page.keyboard_navigation("ArrowDown")
    main_page.keyboard_navigation("Enter")

    search_result_page = SearchResultPage(page)
    search_result_page.assert_searching_result_field()
    search_result_page.assert_right_text_in_searching_field()

def test_unsuccessful_searching(page):
    page.goto("https://www.google.com/")

    main_page = GoogleMainPage(page)
    main_page.fill_searching_field(Data.NEGATIVE_TEXT_FOR_SEARCHING)
    main_page.keyboard_navigation("Enter")

    search_result_page = SearchResultPage(page)
    search_result_page.assert_searching_result_not_found()
