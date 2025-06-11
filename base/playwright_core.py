import pandas
from playwright.sync_api import Page
from io import StringIO


class PBy:
    CSS = "CSS"
    ID = "ID"
    XPATH = "XPATH"
    TEXT = "TEXT"
    ROLE = "ROLE"
    PLACEHOLDER = "PLACEHOLDER"
    LABEL = "LABEL"
    ALTTEXT = "ALTTEXT"
    TITLE = "TITLE"
    TESTID = "TESTID"


class PlaywrightCore:

    def __init__(self, page: Page):
        self.page = page

    def get_element(self, locator: str, by_type: str):
        __all_locator_functions = {
            PBy.CSS: self.page.locator,
            PBy.ID: self.page.locator,
            PBy.XPATH: self.page.locator,
            PBy.TEXT: self.page.get_by_text,
            PBy.ROLE: self.page.get_by_role,
            PBy.PLACEHOLDER: self.page.get_by_placeholder,
            PBy.LABEL: self.page.get_by_label,
            PBy.ALTTEXT: self.page.get_by_alt_text,
            PBy.TITLE: self.page.get_by_title,
            PBy.TESTID: self.page.get_by_test_id
        }
        if by_type == PBy.ID:
            locator = f"#{locator}"
        return __all_locator_functions.get(by_type, self.page.locator)(locator).first

    def navigate_to(self, url: str):
        self.page.goto(url)

    def click(self, locator: str, by_type: str = PBy.XPATH):
        self.get_element(locator=locator, by_type=by_type).click()

    def fill(self, locator: str, by_type: str = PBy.XPATH, value: str = None):
        self.get_element(locator=locator, by_type=by_type).fill(value)

    def scroll_to_element(self, locator: str, by_type: str = PBy.XPATH):
        self.get_element(locator=locator, by_type=by_type).scroll_into_view_if_needed()

    def get_text(self, locator: str, by_type: str = PBy.XPATH) -> str:
        return self.get_element(locator=locator, by_type=by_type).inner_text()

    def is_visible(self, locator: str, by_type: str = PBy.XPATH) -> bool:
        return self.get_element(locator=locator, by_type=by_type).is_visible()

    def get_attribute(self, locator: str, by_type: str = PBy.XPATH, attribute: str = None) -> str:
        return self.get_element(locator=locator, by_type=by_type).get_attribute(attribute)

    def press_key(self, locator: str, by_type: str = PBy.XPATH, key: str = None):
        self.get_element(locator=locator, by_type=by_type).press(key)

    def wait_for_element(self, locator: str, by_type: str = PBy.XPATH):
        self.get_element(locator=locator, by_type=by_type).wait_for()

    def wait_till_element_visible(self, locator: str, by_type: str = PBy.XPATH):
        self.get_element(locator=locator, by_type=by_type).wait_for(state="visible")

    def wait_till_element_attached(self, locator: str, by_type: str = PBy.XPATH):
        self.get_element(locator=locator, by_type=by_type).wait_for(state="attached")

    def take_screenshot(self, path: str = "screenshot.png"):
        self.page.screenshot(path=path)
        return path

    def fetch_dataframes(self):
        return pandas.read_html(StringIO(self.page.content()))
