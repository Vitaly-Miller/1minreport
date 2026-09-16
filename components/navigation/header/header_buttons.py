"""
Header [Buttons]
"""
import allure
from playwright.sync_api import Locator

from components.base_component import BaseComponent
from elements.button import Button

#=======================================================================================================================
class HeaderButtons(BaseComponent):
    """
    Header [Buttons]

    - Login button
    - Get started button
    """
    PATH = 'Header'

    #---------------------------------------------------- ㉧ LOCATORS ---------------------------------------------------
    def login_btn_locator(self) -> Locator:
        return self.page.get_by_role(role='link', name='Log In', exact=True).nth(0)

    def get_started_btn_locator(self) -> Locator:
        return self.page.locator('a.whitespace-nowrap.bg-blue-500.shadow-lg')


    # -------------------------------------------------- ◈ ELEMENTS ----------------------------------------------------
    def login_btn(self) -> Button:
        return Button(self.login_btn_locator(), self.PATH, 'Login button')

    def get_started_btn(self) -> Button:
        return Button(self.get_started_btn_locator(), self.PATH, 'Get started button')


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # ───────────────────────────────────────┐
    # [Header buttons]
    @allure.step('✔ Check [Header buttons]')
    def check(self):
        """
        ✔ Check [Header auth buttons]

        - ✔ Login button
        - ✔ Get started button (Registration button)

        """
        self.check_login_btn()
        self.check_get_started_btn()
    # ───────────────────────────────────────┘


    # [Login button]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Login button]')
    def check_login_btn(self):
        """
        ✔ Check [Login button]

        - ✔ Button - visible
        - ✔ Button - text
        - ✔ Button - link
        """
        self.check_login_btn_visible()
        self.check_login_btn_text()
        self.check_login_btn_link()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_login_btn_visible(self):
        """
        ✔ Check [Login button] is visible

        .
        """
        self.login_btn().check_visible()

    # Text
    def check_login_btn_text(self):
        """
        ✔ Check [Login button] text

        .
        """
        self.login_btn().check_text('Log In')

    # Link
    def check_login_btn_link(self):
        """
        ✔ Check [Login button] link

        .
        """
        self.login_btn().check_href('/login')


    # [Get started button] (Registration button)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Get started button]')
    def check_get_started_btn(self):
        """
        ✔ Check [Get started button] (Registration button)

        - ✔ Button - visible
        - ✔ Button - text
        - ✔ Button - link
        """
        self.check_get_started_btn_visible()
        self.check_get_started_btn_text()
        self.check_get_started_btn_link()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_get_started_btn_visible(self):
        """
        ✔ Check [Get started button] is visible

        .
        """
        self.get_started_btn().check_visible()

    # Text
    def check_get_started_btn_text(self):
        """
        ✔ Check [Get started button] text

        .
        """
        self.get_started_btn().check_text('Get Started Free', use_inner_text=True)

    # Link
    def check_get_started_btn_link(self):
        """
        ✔ Check [Get started button] link

        .
        """
        self.get_started_btn().check_href('/signup')


#=======================================================================================================================
