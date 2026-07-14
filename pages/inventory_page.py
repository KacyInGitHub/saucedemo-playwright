from playwright.sync_api import Page, Locator

class InventoryPage:

    def __init__(self, page: Page):
        self.page = page

        # 页面元素
        self.product_list = page.get_by_test_id("inventory-item")
        self.cart_icon = page.get_by_test_id("shopping-cart-link")
        self.cart_badge = page.locator(".shopping_cart_badge")  # 暂时保留，待确认 HTML
        self.sort_dropdown = page.get_by_test_id("product-sort-container")

    def get_product_names(self) -> list[str]:
        """获取所有商品名称"""
        return self.page.locator(".inventory_item_name").all_inner_texts()

    def get_product_prices(self) -> list[str]:
        """获取所有商品价格"""
        return self.page.locator(".inventory_item_price").all_inner_texts()

    def add_to_cart_by_name(self, product_name: str):
        """根据商品名称点击 Add to cart"""
        self.page.locator(f".inventory_item:has-text('{product_name}')").locator("button").click()

    def click_cart_icon(self):
        """点击购物车图标"""
        self.cart_icon.click()

    def sort_by(self, option: str):
        """排序，option 可选值：az, za, lohi, hilo"""
        self.sort_dropdown.select_option(option)

    def click_product(self, product_name: str):
        """点击商品名称进入详情页"""
        self.page.locator(f".inventory_item_name:has-text('{product_name}')").click()