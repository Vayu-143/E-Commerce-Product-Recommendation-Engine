import heapq

from src.services.similarity_service import (
    SimilarityService
)


class RecommendationService:

    def __init__(self, storage):

        self.storage = storage

    def recommend_products(
        self,
        user_id,
        top_n=5
    ):

        user = self.storage.get_user(
            user_id
        )

        if not user:

            return []

        recommendations = []

        purchased = set(
            user.purchase_history
        )

        for product in (
            self.storage.get_all_products()
        ):

            if (
                product.product_id
                in purchased
            ):
                continue

            score = (
                SimilarityService
                .calculate_score(
                    user,
                    product,
                    self.storage
                )
            )

            recommendations.append(
                (score, product)
            )

        top = heapq.nlargest(
            top_n,
            recommendations,
            key=lambda x: x[0]
        )

        return top

    def explain_recommendation(
        self,
        user_id,
        product
    ):

        user = self.storage.get_user(
            user_id
        )

        reasons = []

        for pid in user.purchase_history:

            purchased = (
                self.storage.get_product(pid)
            )

            if purchased:

                if (
                    purchased.category
                    ==
                    product.category
                ):

                    reasons.append(
                        "Same category as previous purchase"
                    )

                    break

        if product.rating >= 4.5:

            reasons.append(
                "Highly rated product"
            )

        if product.popularity >= 80:

            reasons.append(
                "Popular product"
            )

        return reasons