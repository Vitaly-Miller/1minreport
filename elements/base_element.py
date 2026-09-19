"""
Base check of element
"""
import allure
from playwright.sync_api import Locator, expect

from tools.logger import get_logger

#=======================================================================================================================
class BaseElement:
    logger = get_logger('ELEMENT ', True)

    def __init__(self, locator: Locator, path: str, name: str):
        """
        Initialize base element

        :param locator: Element locator
        :param path: Element navigate-path
        :param name: Element name
        """
        self.locator = locator
        self.path = path
        self.name = f'[{name}]'
        self.error = f'❌ {self.path} > {self.name}'

    # ----------------------------------------------------- Helpers ----------------------------------------------------
    @staticmethod
    def _nth_info(nth: int) -> str:
        """
        (Helper) Returns nth-index / empty string for logging

        :param nth: nth-index of locator
        :return: str
        """
        return '' if nth == 0 else f' (nth: {nth})'

    # ---------------------------------------------------- ▶ ACTIONS ---------------------------------------------------
    # Click
    def click(self, nth: int = 0):
        """
        ▶ Click [Element]

        :param nth: nth-index of locator
        """
        nth_info = self._nth_info(nth)
        step = f'▶ Click {self.name}{nth_info}'
        with allure.step(step):
            self.logger.info(step)
            self.locator.nth(nth).click()

    # Hover
    def hover(self, nth: int = 0):
        """
        ▶ Hover [Element]

        :param nth: nth-index of locator
        """
        nth_info = self._nth_info(nth)
        step = f'▶ Hover {self.name}{nth_info}'
        with allure.step(step):
            self.logger.info(step)
            self.locator.nth(nth).hover()

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # Visible
    def check_visible(self, nth: int = 0):
        """
        ✔ Check [Element] is visible

        :param nth: nth-index of locator
        """
        nth_info = self._nth_info(nth)
        step = f'✔ Check {self.name}{nth_info} is visible'
        error = f'{self.error}{nth_info} - invisible!'
        with allure.step(step):
            self.logger.info(step)
            expect(self.locator.nth(nth), error).to_be_visible()

    # Hidden
    def check_hidden(self, nth: int = 0):
        """
        ✔ Check [Element] is hidden

        :param nth: nth-index of locator
        """
        nth_info = self._nth_info(nth)
        step = f'✔ Check {self.name}{nth_info} is hidden'
        error = f'{self.error}{nth_info} - visible!'
        with allure.step(step):
            self.logger.info(step)
            expect(self.locator.nth(nth), error).to_be_hidden()

    # Text
    def check_text(self, text: str, nth: int = 0, use_inner_text: bool = False):
        """
        ✔ Check [Element] text

        :param text: Expected text
        :param nth: nth-index of locator
        :param use_inner_text: compare against rendered (visible) text instead of raw DOM text content -
        use for elements with responsive/hidden sibling text (e.g. "sm:hidden" variants)
        """
        nth_info = self._nth_info(nth)
        step = f'✔ Check {self.name}{nth_info} text is "{text}"'
        error = f'{self.error}{nth_info} - incorrect text!'
        with allure.step(step):
            self.logger.info(step)
            expect(self.locator.nth(nth), error).to_have_text(text, use_inner_text=use_inner_text)

    # href (Hypertext Reference)
    def check_href(self, href: str, nth: int = 0):
        """
        ✔ Check [Link] "href" url-attribute

        :param href: "href" url-attribute
        :param nth: nth-index of locator
        """
        nth_info = self._nth_info(nth)
        step = f'✔ Check {self.name}{nth_info} <href> attribute is "{href}"'
        error = f'{self.error}{nth_info} - incorrect <href> attribute!'
        with allure.step(step):
            self.logger.info(step)
            expect(self.locator.nth(nth), error).to_have_attribute('href', href)

    # CSS style
    def check_css(self, css: str, value: str, nth: int = 0):
        """
        ✔ Check [CSS style]

        :param css: CSS style
        :param value: CSS value
        :param nth: nth-index of locator
        """
        nth_info = self._nth_info(nth)
        step = f'✔ Check {self.name}{nth_info} CSS style "{css}" is "{value}"'
        error = f'{self.error}{nth_info} - incorrect CSS style "{css}"!'
        with allure.step(step):
            self.logger.info(step)
            expect(self.locator.nth(nth), error).to_have_css(css, value)


#=======================================================================================================================
