class User:

    def __init__(
        self,
        user_id,
        name,
        purchase_history=None,
        search_history=None,
        cart_items=None
    ):

        self.user_id = user_id
        self.name = name

        self.purchase_history = purchase_history or []
        self.search_history = search_history or []
        self.cart_items = cart_items or []

    def add_search(self, keyword):

        self.search_history.append(keyword)

    def add_to_cart(self, product_id):

        self.cart_items.append(product_id)

    def purchase(self, product_id):

        self.purchase_history.append(product_id)

    def __str__(self):

        return (
            f"User ID: {self.user_id}\n"
            f"Name: {self.name}\n"
            f"Purchases: {self.purchase_history}\n"
            f"Searches: {self.search_history}\n"
            f"Cart: {self.cart_items}"
        )