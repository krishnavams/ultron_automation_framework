import time
import logging
from playwright.sync_api import Page, TimeoutError

logging.basicConfig(level=logging.INFO)


class WaitUtils:
    def __init__(self, page: Page, time_out=5):
        self.time_out = 1000 * time_out
        self.page = page

    def wait_for_element_visible(self, locator: str, by_type):
        logging.info(f"Waiting for element visible: {locator}")
        self.page.locator(locator).wait_for(state="visible", timeout=self.time_out)

    def wait_for_element_hidden(self, locator: str):
        logging.info(f"Waiting for element hidden: {locator}")
        self.page.locator(locator).wait_for(state="hidden", timeout=self.time_out)

    def wait_for_text(self, locator: str, text: str):
        logging.info(f"Waiting for text '{text}' in {locator}")
        end_time = time.time() + (self.time_out / 1000)
        while time.time() < end_time:
            try:
                if self.page.locator(locator).inner_text().strip() == text:
                    return
            except Exception:
                pass
            time.sleep(0.5)
        raise TimeoutError(f"Text '{text}' not found in {locator} within {self.time_out} ms")

    def wait_for_attribute(self, locator: str, attribute: str, value: str):
        logging.info(f"Waiting for attribute '{attribute}' = '{value}' in {locator}")
        end_time = time.time() + (self.time_out / 1000)
        while time.time() < end_time:
            try:
                attr = self.page.locator(locator).get_attribute(attribute)
                if attr == value:
                    return
            except Exception:
                pass
            time.sleep(0.5)
        raise TimeoutError(f"Attribute '{attribute}' did not become '{value}' in {locator}")

    def wait_for_url(self, url_part: str):
        logging.info(f"Waiting for URL to contain: {url_part}")
        end_time = time.time() + (self.time_out / 1000)
        while time.time() < end_time:
            if url_part in self.page.url:
                return
            time.sleep(0.5)
        raise TimeoutError(f"URL did not contain '{url_part}' within {self.time_out} ms")

    def wait_for_element_count(self, locator: str, expected_count: int):
        logging.info(f"Waiting for {expected_count} elements at {locator}")
        end_time = time.time() + (self.time_out / 1000)
        while time.time() < end_time:
            try:
                count = self.page.locator(locator).count()
                if count == expected_count:
                    return
            except Exception:
                pass
            time.sleep(0.5)
        raise TimeoutError(f"Element count was not {expected_count} at {locator}")
