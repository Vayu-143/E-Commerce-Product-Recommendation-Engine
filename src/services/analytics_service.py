from collections import defaultdict


class AnalyticsService:

    def __init__(self, storage):

        self.storage = storage

    def category_distribution(self):

        stats = defaultdict(int)

        for product in self.storage.get_all_products():

            stats[product.category] += 1

        return stats

    def average_rating_by_category(self):

        ratings = defaultdict(list)

        for product in self.storage.get_all_products():

            ratings[
                product.category
            ].append(
                product.rating
            )

        result = {}

        for category, values in ratings.items():

            result[category] = round(
                sum(values) / len(values),
                2
            )

        return result

    def top_popular_products(
        self,
        top_n=5
    ):

        products = sorted(
            self.storage.get_all_products(),
            key=lambda p: p.popularity,
            reverse=True
        )

        return products[:top_n]