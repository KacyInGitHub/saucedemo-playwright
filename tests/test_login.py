import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from test_data.login_data import VALID_LOGIN, INVALID_LOGIN_DATA

class TestLogin:

    def test_login_success(self, login_page: LoginPage):
        """正确账号密码 → 登录成功，跳转到商品页"""
        login_page.goto()
        login_page.login(VALID_LOGIN["username"], VALID_LOGIN["password"])

        expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")

    @pytest.mark.parametrize("username, password, expected_error", INVALID_LOGIN_DATA)
    def test_invalid_login(self, login_page: LoginPage, username, password, expected_error):
        """各种错误登录场景 → 显示对应错误信息"""
        login_page.goto()
        login_page.login(username, password)
        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_contain_text(expected_error)