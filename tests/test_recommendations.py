import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from src.storage.data_storage import DataStorage

from src.services.recommendation_service import (
    RecommendationService
)


def test_recommendations():

    storage = DataStorage()

    engine = RecommendationService(
        storage
    )

    recommendations = (
        engine.recommend_products(1)
    )

    assert len(recommendations) > 0


def test_user_exists():

    storage = DataStorage()

    user = storage.get_user(1)

    assert user is not None


def test_product_exists():

    storage = DataStorage()

    product = storage.get_product(101)

    assert product is not None


if __name__ == "__main__":

    test_recommendations()
    test_user_exists()
    test_product_exists()

    print(
        "All tests passed successfully."
    )