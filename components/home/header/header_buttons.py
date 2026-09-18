"""
Home page Header [Buttons]
"""
import allure
from playwright.sync_api import Locator
from components.base_component import BaseComponent
from elements.button import Button


#=======================================================================================================================
class HeaderButtonsComponent(BaseComponent):
    """
    Header [Buttons]

    - Login button
    - Get started button
    """
    PATH = 'Home page > Header'

    # --------------------------------------------------- ㉧ LOCATORS ---------------------------------------------------
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
    @allure.step('✔ Check [Login button]')
    def check_login_btn(self):
        """
        ✔ Check [Login button]

        - ✔ Button - visible
        - ✔ Button - text
        - ✔ Button - link
        """
        self.login_btn().check_visible()
        self.login_btn().check_text('Log In')
        self.login_btn().check_href('/login')

    # [Get started button] (Registration button)
    @allure.step('✔ Check [Get started button]')
    def check_get_started_btn(self):
        """
        ✔ Check [Get started button] (Registration button)

        - ✔ Button - visible
        - ✔ Button - text
        - ✔ Button - link
        """
        self.get_started_btn().check_visible()
        self.get_started_btn().check_text('Get Started Free', use_inner_text=True)
        self.get_started_btn().check_href('/signup')


#=======================================================================================================================
