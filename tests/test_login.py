import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

# 测试数据：(用户名, 密码, 期望的错误信息)
INVALID_LOGIN_DATA = [
    ("standard_user",  "wrong_password", "Username and password do not match"),
    ("locked_out_user","secret_sauce",   "Sorry, this user has been locked out"),
    ("",               "secret_sauce",   "Username is required"),
    ("standard_user",  "",               "Password is required"),
]


class TestLogin:

    def test_login_success(self, login_page: LoginPage):
        """正确账号密码 → 登录成功，跳转到商品页"""
        login_page.goto()
        login_page.login("standard_user", "secret_sauce")

        expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def test_wrong_password(self, login_page: LoginPage):
        """错误密码 → 显示错误提示"""
        login_page.goto()
        login_page.login("standard_user", "wrong_password")

        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_contain_text("Username and password do not match")

    def test_locked_user(self, login_page: LoginPage):
        """锁定用户 → 显示锁定提示"""
        login_page.goto()
        login_page.login("locked_out_user", "secret_sauce")

        expect(login_page.error_message).to_contain_text("locked out")

    @pytest.mark.parametrize("username, password, expected_error", INVALID_LOGIN_DATA)
    def test_invalid_login(self, login_page: LoginPage, username, password, expected_error):
        """各种错误登录场景 → 显示对应错误信息"""
        login_page.goto()
        login_page.login(username, password)
        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_contain_text(expected_error)