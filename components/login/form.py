"""
Login form
"""
import allure
from playwright.sync_api import Locator

from components.base_component import BaseComponent
from elements.button import Button
from elements.input_field import InputField
from elements.link import Link
from elements.text import Text

#=======================================================================================================================
class LoginFormComponent(BaseComponent):
    """
    - Google auth button
    - OR-separator
    - Email field label
    - Email input field
    - Password field label
    - Password input field
    - Login button
    - Forgot password link
    - Don't have an account text
    - Sign up link
    """
    PATH = 'Login page > Form'
    # --------------------------------------------------- ㉧ LOCATORS ---------------------------------------------------
    def google_auth_btn_locator(self) -> Locator:
        return self.page.get_by_role(role='button', name='Continue with Google')

    def or_separator_locator(self) -> Locator:
        return self.page.locator('div.my-5')

    def email_field_label_locator(self) -> Locator:
        return self.page.get_by_text('Email')

    def email_field_input_locator(self) -> Locator:
        return self.page.get_by_role(role='textbox', name='Email')

    def password_field_label_locator(self) -> Locator:
        return self.page.get_by_text('Password')

    def password_field_input_locator(self) -> Locator:
        return self.page.get_by_role(role='textbox', name='Password')

    def password_field_input_show_btn_locator(self) -> Locator:
        return self.page.get_by_role(role='button', name='Show')

    def forgot_password_link_locator(self) -> Locator:
        return self.page.get_by_role(role='link', name='Forgot password')



    # --------------------------------------------------- ◈ ELEMENTS ---------------------------------------------------
    def google_auth_btn(self) -> Button:
        return Button(self.google_auth_btn_locator(), self.PATH, 'Google auth button')

    def or_separator(self) -> Text:
        return Text(self.or_separator_locator(), self.PATH, 'OR-separator')

    def email_field_label(self) -> Text:
        return Text(self.email_field_label_locator(), self.PATH, 'Email field label')

    def email_field_input(self) -> InputField:
        return InputField(self.email_field_input_locator(), self.PATH, 'Email field input')

    def password_field_label(self) -> Text:
        return Text(self.password_field_label_locator(), self.PATH, 'Password field label')

    def password_field_input(self) -> InputField:
        return InputField(self.password_field_input_locator(), self.PATH, 'Password field input')

    def password_field_input_show_btn(self) -> Button:
        return Button(self.password_field_input_show_btn_locator(), self.PATH, 'Password field input Show-button')

    def forgot_password_link(self) -> Link:
        return Link(self.forgot_password_link_locator(), self.PATH, 'Forgot password? link')


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Login form]
    # ──────────────────────────────────┐
    @allure.step('✔ Check [Login form]')
    def check(self):
        """
        ✔ Check [Login form]

        - ✔ Google auth button
        - ✔ OR-separator
        - ✔ Email field label
        - ✔ Email field input
        - ✔ Password field label
        - ✔ Password field input
        - ✔ Password field input Show-button
        - ✔ Forgot password? link
        - ✔
        - ✔
        """
        self.check_google_auth_btn()
        self.check_or_separator()
        self.check_email_field_label()
        self.check_email_field_input()
        self.check_password_field_label()
        self.check_password_field_input()
        self.check_password_field_input_show_btn()
        self.check_forgot_password_link()

    # ───────────────────────────────────┘

    # [Google auth button]
    @allure.step('✔ Check [Google auth button]')
    def check_google_auth_btn(self):
        """
        ✔ Check [Google auth button]

        - Button - visible
        - Button - enable
        - Button - text
        """
        self.google_auth_btn().check_visible()
        self.google_auth_btn().check_enabled()
        self.google_auth_btn().check_text('Continue with Google')

    # [OR-separator]
    @allure.step('✔ Check [OR-separator]')
    def check_or_separator(self):
        """
        ✔ Check [OR-separator]

        - Text - visible
        - Text - text
        """
        self.or_separator().check_visible()
        self.or_separator().check_text('or')

    # [Email field label]
    @allure.step('✔ Check [Email field label]')
    def check_email_field_label(self):
        """
        ✔ Check [Email field label]

        - Text - visible
        - Text - text
        """
        self.email_field_label().check_visible()
        self.email_field_label().check_text('Email')

    # [Email field input]
    @allure.step('✔ Check [Email field input]')
    def check_email_field_input(self, value: str = ''):
        """
        ✔ Check [Email field input]

        - Input field - visible
        - Input field - placeholder
        - Input field - value (empty by default)

        :param value: Field value (empty by default)
        """
        self.email_field_input().check_visible()
        self.email_field_input().check_placeholder('you@example.com')
        self.email_field_input().check_value(value)

    # [Password field label]
    @allure.step('✔ Check [Password field label]')
    def check_password_field_label(self):
        """
        ✔ Check [Password field label]

        - Text - visible
        - Text - text
        """
        self.password_field_label().check_visible()
        self.password_field_label().check_text('Password')

    # [Password field input]
    @allure.step('✔ Check [Password field input]')
    def check_password_field_input(self, value: str = ''):
        """
        ✔ Check [Email field input]

        - Input field - visible
        - Input field - placeholder
        - Input field - value (empty by default)

        :param value: Field value (empty by default)
        """
        self.password_field_input().check_visible()
        self.password_field_input().check_placeholder('Enter your password')
        self.password_field_input().check_value(value)

    # [Password field input Show-button]
    @allure.step('✔ Check [Password field label]')
    def check_password_field_input_show_btn(self):
        """
        ✔ Check [Password field input Show-button]

        - Text - visible
        - Text - text
        """
        self.password_field_input_show_btn().check_visible()
        self.password_field_input_show_btn().check_text('Show')

    # [Forgot password link]
    def check_forgot_password_link(self):
        """
        ✔ Check [Forgot password link]

        - Link - visible
        - Link - text
        - Link - URL (href)
        """
        self.forgot_password_link().check_visible()
        self.forgot_password_link().check_text('Forgot password?')
        self.forgot_password_link().check_href('/forgot-password')

#=======================================================================================================================
