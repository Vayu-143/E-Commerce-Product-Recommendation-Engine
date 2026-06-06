from src.utils.constants import (
    CATEGORY_WEIGHT,
    SEARCH_WEIGHT,
    CART_WEIGHT,
    RATING_WEIGHT,
    POPULARITY_WEIGHT
)


class SimilarityService:

    @staticmethod
    def calculate_score(
        user,
        product,
        storage
    ):

        category_score = 0
        search_score = 0
        cart_score = 0

        # Purchase History Match

        for pid in user.purchase_history:

            purchased = storage.get_product(pid)

            if purchased:

                if purchased.category == product.category:

                    category_score += 100

        # Search Match

        for keyword in user.search_history:

            if keyword.lower() in product.name.lower():

                search_score += 100

        # Cart Match

        for cid in user.cart_items:

            cart_product = storage.get_product(cid)

            if cart_product:

                if cart_product.category == product.category:

                    cart_score += 100

        rating_score = (
            product.rating / 5
        ) * 100

        popularity_score = (
            product.popularity
        )

        final_score = (

            category_score * CATEGORY_WEIGHT +

            search_score * SEARCH_WEIGHT +

            cart_score * CART_WEIGHT +

            rating_score * RATING_WEIGHT +

            popularity_score * POPULARITY_WEIGHT

        )

        return round(final_score, 2)