from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestInventory:

    def test_product_list_displayed(self, inventory_page: InventoryPage):
        """登录后商品列表正常显示，应有 6 个商品"""
        items = inventory_page.page.locator(".inventory_item")
        expect(items).to_have_count(6)

    def test_add_to_cart(self, inventory_page: InventoryPage):
        """点击 Add to cart，购物车数量变为 1"""
        inventory_page.add_to_cart_by_name("Sauce Labs Backpack")

        expect(inventory_page.cart_badge).to_be_visible()
        expect(inventory_page.cart_badge).to_have_text("1")

    def test_add_multiple_to_cart(self, inventory_page: InventoryPage):
        """添加两个商品，购物车数量变为 2"""
        inventory_page.add_to_cart_by_name("Sauce Labs Backpack")
        inventory_page.add_to_cart_by_name("Sauce Labs Bike Light")

        expect(inventory_page.cart_badge).to_have_text("2")

    def test_sort_by_price_low_to_high(self, inventory_page: InventoryPage):
        """按价格从低到高排序，第一个商品应该最便宜"""
        inventory_page.sort_by("lohi")

        prices = inventory_page.get_product_prices()
        # 把字符串价格转成数字比较
        price_numbers = [float(p.replace("$", "")) for p in prices]
        assert price_numbers == sorted(price_numbers)

    def test_sort_by_name_a_to_z(self, inventory_page: InventoryPage):
        """按名称 A-Z 排序"""
        inventory_page.sort_by("az")

        names = inventory_page.get_product_names()
        assert names == sorted(names)

    def test_click_product_detail(self, inventory_page: InventoryPage):
        """点击商品名称，进入详情页"""
        inventory_page.click_product("Sauce Labs Backpack")

        expect(inventory_page.page).to_have_url(
            "https://www.saucedemo.com/inventory-item.html?id=4"
        )