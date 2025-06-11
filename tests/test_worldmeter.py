from time import sleep

import pytest
from playwright.sync_api import Page, Browser

from base.playwright_core import PlaywrightCore


class TestWorldMeter:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page, browser: Browser):
        self.page = page
        self.browser = browser

    def test_page(self):
        self.play_wright = PlaywrightCore(self.page)
        self.play_wright.navigate_to("https://www.worldometers.info/coronavirus/")
        # self.play_wright.wait_till_element_attached("maincounter-wrap", "id")
        # self.play_wright.scroll_to_element("maincounter-wrap", "id")
        self.play_wright.wait_for_element("//a[text()='WEEKLY TRENDS']")
        # self.play_wright.wait_till_element_attached("nav-yesterday-tab", "id")
        # self.play_wright.scroll_to_element("nav-yesterday-tab", "id")
        # self.play_wright.click("nav-yesterday-tab", "id")
        self.play_wright.scroll_to_element("//a[text()='WEEKLY TRENDS']")
        self.play_wright.click("//a[text()='WEEKLY TRENDS']")
        sleep(10)
        print(self.play_wright.fetch_dataframes())