"""
Header [Navigation links]
"""

import allure
from playwright.sync_api import Locator
from components.base_component import BaseComponent
from elements.link import Link

#=======================================================================================================================
class HeaderNavLinks(BaseComponent):
    """
    Header [Navigation links]

    - "How It Works" link
    - "Pricing" link
    - "Who It's For" link
    """
    PATH = 'Header'

    # ------------------------------------------------- ㉧ LOCATORS -----------------------------------------------------
    def how_it_works_link_locator(self) -> Locator:
        return self.page.get_by_role('navigation').get_by_role(role='link', name='How It Works', exact=True)

    def pricing_link_locator(self) -> Locator:
        return self.page.get_by_role('navigation').get_by_role(role='link', name='Pricing', exact=True)

    def who_its_for_link_locator(self) -> Locator:
        return self.page.get_by_role('navigation').get_by_role(role="link", name="Who It's For", exact=True)

    # Buttons
    def login_btn_locator(self) -> Locator:
        return self.page.get_by_role(role='link', name='Log In', exact=True).nth(0)

    def get_started_btn_locator(self) -> Locator:
        return self.page.locator('a.whitespace-nowrap.bg-blue-500.shadow-lg')


    # ------------------------------------------------- ◈ ELEMENTS -----------------------------------------------------
    def how_it_works_link(self) -> Link:
        return Link(self.how_it_works_link_locator(), self.PATH, 'How It Works link')

    def pricing_link(self) -> Link:
        return Link(self.pricing_link_locator(), self.PATH, 'Pricing link')

    def who_its_for_link(self) -> Link:
        return Link(self.who_its_for_link_locator(), self.PATH, "Who It's For link")


    # ------------------------------------------------ ✔️EXPECTATIONS --------------------------------------------------
    # ────────────────────────────────────────────────┐
    @allure.step('✔ Check [Header navigation links]')
    def check(self):
        """
        ✔ Check [Header navigation links]

        - ✔ "How It Works" link
        - ✔ "Pricing" link
        - ✔ "Who It's For" link
        """
        self.check_how_it_works_link()
        self.check_pricing_link()
        self.check_who_its_for_link()
    # ────────────────────────────────────────────────┘

    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    # [How It Works link]
    @allure.step('✔ Check [How It Works link]')
    def check_how_it_works_link(self):
        """
        ✔ Check [How It Works link]

        - ✔ Link - visible
        - ✔ Link - text
        - ✔ Link - URL (href)
        """
        self.check_how_it_works_link_visible()
        self.check_check_how_it_works_link_text()
        self.check_how_it_works_link_navigates()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_how_it_works_link_visible(self):
        """
        ✔ Check [How It Works link] is visible

        .
        """
        self.how_it_works_link().check_visible()

    # Text
    def check_check_how_it_works_link_text(self):
        """
        ✔ Check [How It Works link] text

        .
        """
        self.how_it_works_link().check_text('How It Works', use_inner_text=True)

    # Link
    def check_how_it_works_link_navigates(self):
        """
        ✔ Check [How It Works link] navigates (anchor)

        .
        """
        self.how_it_works_link().check_href('#how-it-works')


    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    # [Pricing link]
    @allure.step('✔ Check [Pricing link]')
    def check_pricing_link(self):
        """
        ✔ Check [Pricing link]

        - ✔ Link - visible
        - ✔ Link - text
        - ✔ Link - URL (href)
        """
        self.check_pricing_link_visible()
        self.check_pricing_link_text()
        self.check_pricing_link_navigates()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_pricing_link_visible(self):
        """
        ✔ Check [Pricing link] is visible

        .
        """
        self.pricing_link().check_visible()

    # Text
    def check_pricing_link_text(self):
        """
        ✔ Check [Pricing link] text

        .
        """
        self.pricing_link().check_text('Pricing', use_inner_text=True)

    # Link
    def check_pricing_link_navigates(self):
        """
        ✔ Check [Pricing link] navigates (anchor)

        .
        """
        self.pricing_link().check_href('#pricing')


    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    # [Who It's For link]
    @allure.step("✔ Check [Who It's For link]")
    def check_who_its_for_link(self):
        """
        ✔ Check [Who It's For link]

        - ✔ Link - visible
        - ✔ Link - text
        - ✔ Link - URL (href)
        """
        self.check_who_its_for_link_visible()
        self.check_who_its_for_link_text()
        self.check_who_its_for_link_navigates()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_who_its_for_link_visible(self):
        """
        ✔ Check [Who It's For link] is visible

        .
        """
        self.who_its_for_link().check_visible()

    # Text
    def check_who_its_for_link_text(self):
        """
        ✔ Check [Who It's For link] text

        .
        """
        self.who_its_for_link().check_text("Who It's For", use_inner_text=True)

    # Link
    def check_who_its_for_link_navigates(self):
        """
        ✔ Check [Who It's For link] navigates (anchor)

        .
        """
        self.who_its_for_link().check_href('#who-its-for')


#=======================================================================================================================
