"""
Login form (component)
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
    - Password show button
    - Forgot password link
    - Login button
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

    def email_input_field_locator(self) -> Locator:
        return self.page.get_by_role(role='textbox', name='Email')

    def password_field_label_locator(self) -> Locator:
        return self.page.get_by_text('Password')

    def password_input_field_locator(self) -> Locator:
        return self.page.get_by_role(role='textbox', name='Password')

    def password_show_btn_locator(self) -> Locator:
        return self.page.get_by_role(role='button', name='Show')

    def password_hide_btn_locator(self) -> Locator:
        return self.page.get_by_role(role='button', name='Hide')

    def forgot_password_link_locator(self) -> Locator:
        return self.page.get_by_role(role='link', name='Forgot password')

    def login_btn_locator(self) -> Locator:
        return self.page.locator('button[type="submit"]')

    def do_not_have_an_account_locator(self) -> Locator:
        return self.page.locator("div[class='mt-5 text-center text-sm text-slate-400 sm:mt-6']")

    def sign_up_link_locator(self) -> Locator:
        return self.page.get_by_role(role='link', name='Sign Up')


    # --------------------------------------------------- ◈ ELEMENTS ---------------------------------------------------
    def google_auth_btn(self) -> Button:
        return Button(self.google_auth_btn_locator(), self.PATH, 'Google auth button')

    def or_separator(self) -> Text:
        return Text(self.or_separator_locator(), self.PATH, 'OR-separator')

    def email_field_label(self) -> Text:
        return Text(self.email_field_label_locator(), self.PATH, 'Email field label')

    def email_input_field(self) -> InputField:
        return InputField(self.email_input_field_locator(), self.PATH, 'Email input field')

    def password_field_label(self) -> Text:
        return Text(self.password_field_label_locator(), self.PATH, 'Password field label')

    def password_input_field(self) -> InputField:
        return InputField(self.password_input_field_locator(), self.PATH, 'Password input field')

    def password_show_btn(self) -> Button:
        return Button(self.password_show_btn_locator(), self.PATH, 'Password show button')

    def password_hide_btn(self) -> Button:
        return Button(self.password_hide_btn_locator(), self.PATH, 'Password hide button')

    def forgot_password_link(self) -> Link:
        return Link(self.forgot_password_link_locator(), self.PATH, 'Forgot password? link')

    def login_btn(self) -> Button:
        return Button(self.login_btn_locator(), self.PATH, 'Login button')

    def do_not_have_an_account(self) -> Text:
        return Text(self.do_not_have_an_account_locator(), self.PATH, "Don't have an account? Sing Up")

    def sign_up_link(self) -> Link:
        return Link(self.sign_up_link_locator(), self.PATH, 'Sign Up link')

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Fill [Login form]
    @allure.step('▶ Fill [Login form]')
    def fill(self, email: str = '', password: str = ''):
        """
        ▶ Fill [Login form]

        - Email field - ▶ fill | ✔ value
        - Password field - ▶ fill | ✔ value

        :param email: Email (option)
        :param password: Password (option)
        """
        self.email_input_field().fill(email)
        self.password_input_field().fill(password)

    # Click [Forgot password link]
    def click_forgot_password_link(self):
        """
        ▶ Click [Forgot password link]

        .
        """
        self.forgot_password_link().click()

    # Click [Google auth button]
    def click_google_auth_btn(self):
        """
        ▶ Click [Google auth button]

        .
        """
        self.google_auth_btn().click()


    # Hover [Password show button]
    def hover_password_show_button(self):
        """
        ▶ Hover [Password show button]

        .
        """
        self.password_show_btn().hover()

    # Click [Password show button]
    def click_password_show_button(self):
        """
        ▶ Click [Password show button]

        .
        """
        self.password_show_btn().click()


    # Hover [Password hide button]
    def hover_password_hide_button(self):
        """
        ▶ Hover [Password hide button]

        .
        """
        self.password_hide_btn().hover()

    # Click [Password hide button]
    def click_password_hide_button(self):
        """
        ▶ Click [Password hide button]

        .
        """
        self.password_hide_btn().click()


    # Click [Login button]
    def click_login_btn(self):
        """
        ▶ Click [Login button]

        .
        """
        self.login_btn().click()

    # Click [Sign Up link]
    def click_sign_up_link(self):
        """
        ▶ Click [Sign Up link]

        .
        """
        self.sign_up_link().click()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Login form]
    # ─────────────────────────────────────────────┐
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
        - ✔ Password show button
        - ✔ Forgot password? link
        - ✔ Login button
        - ✔ Don't have an account?
        - ✔ Sign up link
        """
        self.check_google_auth_btn()
        self.check_or_separator()
        self.check_email_field_label()
        self.check_email_input_field()
        self.check_password_field_label()
        self.check_password_input_field()
        self.check_password_show_btn()
        self.check_forgot_password_link()
        self.check_login_btn()
        self.check_do_not_have_an_account_sign_up()
    # ─────────────────────────────────────────────┘

    # [Google auth button]
    @allure.step('✔ Check [Google auth button]')
    def check_google_auth_btn(self):
        """
        ✔ Check [Google auth button]

        - ✔ Button - visible
        - ✔ Button - enable
        - ✔ Button - text
        """
        self.google_auth_btn().check_visible()
        self.google_auth_btn().check_enabled()
        self.google_auth_btn().check_text('Continue with Google')

    # [OR-separator]
    @allure.step('✔ Check [OR-separator]')
    def check_or_separator(self):
        """
        ✔ Check [OR-separator]

        - ✔ Text - visible
        - ✔ Text - text
        """
        self.or_separator().check_visible()
        self.or_separator().check_text('OR', use_inner_text=True)


    # [Email field label]
    @allure.step('✔ Check [Email field label]')
    def check_email_field_label(self):
        """
        ✔ Check [Email field label]

        - ✔ Text - visible
        - ✔ Text - text
        """
        self.email_field_label().check_visible()
        self.email_field_label().check_text('Email')

    # [Email input field]
    @allure.step('✔ Check [Email input field]')
    def check_email_input_field(self, value: str = ''):
        """
        ✔ Check [Email input field]

        - ✔ Input field - visible
        - ✔ Input field - placeholder
        - ✔ Input field - value (empty by default)

        :param value: Field value (empty by default)
        """
        self.email_input_field().check_visible()
        self.email_input_field().check_placeholder('you@example.com')
        self.email_input_field().check_value(value)


    # [Password field label]
    @allure.step('✔ Check [Password field label]')
    def check_password_field_label(self):
        """
        ✔ Check [Password field label]

        - ✔ Text - visible
        - ✔ Text - text
        """
        self.password_field_label().check_visible()
        self.password_field_label().check_text('Password')

    # [Password input field]
    @allure.step('✔ Check [Password input field]')
    def check_password_input_field(self, value: str = ''):
        """
        ✔ Check [Email input field]

        - ✔ Input field - visible
        - ✔ Input field - placeholder
        - ✔ Input field - value (empty by default)

        :param value: Field value (empty by default)
        """
        self.password_input_field().check_visible()
        self.password_input_field().check_placeholder('Enter your password')
        self.password_input_field().check_value(value)

    # [Password show button]
    @allure.step('✔ Check [Password show button]')
    def check_password_show_btn(self):
        """
        ✔ Check [Password show button]

        - ✔ Show-button - visible
        - ✔ Show-button - text
        - ▶ Show-button - hover
        - ✔ Show-button - CSS style (hover color)
        """
        self.password_show_btn().check_visible()
        self.password_show_btn().check_text('Show')
        self.hover_password_show_button()
        self.password_show_btn().check_css('color', 'rgb(255, 255, 255)')  # ⚠️TODO(DEV): "Show/Hide Password" button turns white on hover and blends into the background - low contrast.


    # [Password hide button] (⚠ not in suite)
    @allure.step('✔ Check [Password hide button]')
    def check_password_hide_btn(self):
        """
        ✔ Check [Password hide button]

        - ✔ Hide-button - visible
        - ✔ Hide-button - text
        - ▶ Hide-button - hover
        - ✔ Hide-button - CSS style (hover color)
        """
        self.password_hide_btn().check_visible()
        self.password_hide_btn().check_text('Hide')
        self.hover_password_hide_button()
        self.password_hide_btn().check_css('color', 'rgb(255, 255, 255)')  # ⚠️TODO(DEV): See [Password show button] comment

    # [Forgot password link]
    @allure.step('✔ Check [Forgot password link]')
    def check_forgot_password_link(self):
        """
        ✔ Check [Forgot password link]

        - ✔ Link - visible
        - ✔ Link - text
        - ✔ Link - URL (href)
        """
        self.forgot_password_link().check_visible()
        self.forgot_password_link().check_text('Forgot password?')
        self.forgot_password_link().check_href('/forgot-password')


    # [Login button]
    @allure.step('✔ Check [Login button]')
    def check_login_btn(self):
        """
        ✔ Check [Login button]

        - ✔ Button - visible
        - ✔ Button - enabled
        - ✔ Button - text
        """
        self.login_btn().check_visible()
        self.login_btn().check_enabled()
        self.login_btn().check_text('Log In')


    # [Don't have an account? Sing Up]
    @allure.step("✔ Check [Don't have an account? Sing Up]")
    def check_do_not_have_an_account_sign_up(self):
        """
        ✔ Check [Don't have an account? Sing Up]

        - ✔ Text - visible
        - ✔ Text - text
        - ✔ Sing Up - link
        """
        self.do_not_have_an_account().check_visible()
        self.do_not_have_an_account().check_text("Don't have an account? Sign Up")
        self.sign_up_link().check_href('/signup')


#=======================================================================================================================
