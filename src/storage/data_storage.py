import json

from src.models.product import Product
from src.models.user import User


class DataStorage:

    def __init__(self):

        self.products = {}
        self.users = {}

        self.load_products()
        self.load_users()

    def load_products(self):

        with open(
            "data/products.json",
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        for item in data:

            product = Product(
                item["id"],
                item["name"],
                item["category"],
                item["rating"],
                item["price"],
                item["popularity"]
            )

            self.products[
                product.product_id
            ] = product

    def load_users(self):

        with open(
            "data/users.json",
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        for item in data:

            user = User(
                item["id"],
                item["name"],
                item["purchase_history"],
                item["search_history"],
                item["cart_items"]
            )

            self.users[user.user_id] = user

    def get_product(self, product_id):

        return self.products.get(product_id)

    def get_user(self, user_id):

        return self.users.get(user_id)

    def get_all_products(self):

        return list(self.products.values())

    def get_all_users(self):

        return list(self.users.values())