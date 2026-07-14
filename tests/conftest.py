import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    """登录后返回 InventoryPage"""
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    return InventoryPage(page)