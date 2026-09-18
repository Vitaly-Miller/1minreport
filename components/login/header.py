"""
Login page header
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Locator
from elements.image import Image
from elements.text import Text

#=======================================================================================================================
class LoginPageHeaderComponent(BaseComponent):
    """
    Header component

    - Logo
    - Navigation links
    - Authentication buttons
    """
    PATH = 'Login page > Header'

    # --------------------------------------------------- ㉧ LOCATORS ---------------------------------------------------
    def logo_image_locator(self) -> Locator:
        return self.page.get_by_role(role='img')

    def logo_title_locator(self) -> Locator:
        return self.page.locator('div[class="mt-2.5 text-base font-bold tracking-tight sm:mt-3 sm:text-lg"]')

    def logo_description_locator(self) -> Locator:
        return self.page.get_by_role('paragraph').nth(0)

    def welcome_title_locator(self) -> Locator:
        return self.page.get_by_role('main').get_by_role('heading')

    def welcome_description_locator(self) -> Locator:
        return self.page.get_by_role('paragraph').nth(1)


    # --------------------------------------------------- ◈ ELEMENTS ---------------------------------------------------
    def logo_image(self) -> Image:
        return Image(self.logo_image_locator(), self.PATH, 'Logo image')

    def logo_title(self) -> Text:
        return Text(self.logo_title_locator(), self.PATH, 'Logo title')

    def logo_description(self) -> Text:
        return Text(self.logo_description_locator(), self.PATH, 'Logo description')

    def welcome_title(self) -> Text:
        return Text(self.welcome_title_locator(), self.PATH, 'Welcome title')

    def welcome_description(self) -> Text:
        return Text(self.welcome_description_locator(), self.PATH, 'Welcome description')


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Header]
    # ──────────────────────────────────┐
    @allure.step('✔ Check [Header]')
    def check(self):
        """
        ✔ Check [Header]

        - ✔ Logo
        - ✔ Titles
        - ✔ Descriptions
        """
        self.check_image()
        self.check_logo_title()
        self.check_logo_description()
        self.check_welcome_title()
        self.check_welcome_description()
    # ──────────────────────────────────┘

    # [Logo image]
    def check_image(self):
        """
        ✔ Check [Image] is visible

        .
        """
        self.logo_image().check_visible()

    # [Logo title]
    @allure.step('✔ Check [Logo title]')
    def check_logo_title(self):
        """
        ✔ Check [Logo title]

        - ✔ Logo title - visible
        - ✔ Logo title - text
        """
        self.logo_title().check_visible()
        self.logo_title().check_text('1 MINUTE REPORT')

    # [Logo description]
    @allure.step('✔ Check [Logo description]')
    def check_logo_description(self):
        """
        ✔ Check [Logo description]

        - ✔ Logo description - visible
        - ✔ Logo description - text
        """
        self.logo_description().check_visible()
        self.logo_description().check_text('Clear progress. Better communication.')

    # [Welcome title]
    @allure.step('✔ Check [Welcome title]')
    def check_welcome_title(self):
        """
        ✔ Check [Welcome title]

        - ✔ Welcome title - visible
        - ✔ Welcome title - text
        """
        self.welcome_title().check_visible()
        self.welcome_title().check_text('Welcome back')

    # [Welcome description]
    @allure.step('✔ Check [Welcome description]')
    def check_welcome_description(self):
        """
        ✔ Check [Welcome description]

        - ✔ Welcome description - visible
        - ✔ Welcome description - text
        """
        self.welcome_description().check_visible()
        self.welcome_description().check_text('Log in to continue to 1 Minute Report.')


#=======================================================================================================================
