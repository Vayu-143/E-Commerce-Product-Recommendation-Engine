class Product:

    def __init__(
        self,
        product_id,
        name,
        category,
        rating,
        price,
        popularity
    ):

        self.product_id = product_id
        self.name = name
        self.category = category
        self.rating = rating
        self.price = price
        self.popularity = popularity

    def to_dict(self):

        return {
            "id": self.product_id,
            "name": self.name,
            "category": self.category,
            "rating": self.rating,
            "price": self.price,
            "popularity": self.popularity
        }

    def __str__(self):

        return (
            f"[{self.product_id}] "
            f"{self.name} | "
            f"{self.category} | "
            f"Rating:{self.rating} | "
            f"₹{self.price}"
        )