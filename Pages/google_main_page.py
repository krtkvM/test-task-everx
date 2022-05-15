from Pages.base_page import BasePage
from locators import Locator

class GoogleMainPage(BasePage):

    def fill_searching_field(self, text):
        self.page.fill(Locator.searching_field, text)

    def keyboard_navigation(self, text):
        self.page.keyboard.press(text)
        #F1 - F12, Digit0- Digit9, KeyA- KeyZ, Backquote, Minus, Equal, Backslash,
        # Backspace, Tab, Delete, Escape, ArrowDown, End, Enter, Home, Insert,
        # PageDown, PageUp, ArrowRight, ArrowUp, etc.

    def closing_web_socket(self):
        self.web_socket.on("close")

