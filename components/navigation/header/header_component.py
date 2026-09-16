"""
Header
(Page component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Page
from components.navigation.header.header_buttons import HeaderButtons
from components.navigation.header.header_logo import HeaderLogo
from components.navigation.header.header_nav_links import HeaderNavLinks

#=======================================================================================================================
class HeaderComponent(BaseComponent):
    """
    Header component

    - Logo
    - Navigation links
    - Authentication buttons
    """
    def __init__(self, page: Page):
        super().__init__(page)

        # ⿳ COMPONENTS
        self.logo = HeaderLogo(page)
        self.nav_links = HeaderNavLinks(page)
        self.buttons = HeaderButtons(page)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Header]
    # ───────────────────────────────┐
    @allure.step('✔ Check [Header]')
    def check(self):
        """
        ✔ Check [Header]

        - ✔ Logo
        - ✔ Navigation links (anchors)
        - ✔ Buttons
        """
        self.logo.check()
        self.nav_links.check()
        self.buttons.check()
    # ───────────────────────────────┘

#=======================================================================================================================
