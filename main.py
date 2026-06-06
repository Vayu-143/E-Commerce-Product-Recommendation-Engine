from src.storage.data_storage import (
    DataStorage
)

from src.services.recommendation_service import (
    RecommendationService
)

from src.services.analytics_service import (
    AnalyticsService
)

from src.services.report_service import (
    ReportService
)


storage = DataStorage()

recommendation_engine = (
    RecommendationService(
        storage
    )
)

analytics_engine = (
    AnalyticsService(
        storage
    )
)
from src.storage.data_storage import DataStorage

from src.services.recommendation_service import (
    RecommendationService
)

from src.services.analytics_service import (
    AnalyticsService
)

from src.services.report_service import (
    ReportService
)

from src.utils.logger import log_event


def view_products(storage):

    print("\nAVAILABLE PRODUCTS")
    print("=" * 60)

    for product in storage.get_all_products():

        print(product)


def view_users(storage):

    print("\nUSERS")
    print("=" * 60)

    for user in storage.get_all_users():

        print(user)
        print("-" * 60)


def generate_recommendations(
    storage,
    recommendation_engine
):

    try:

        user_id = int(
            input(
                "\nEnter User ID: "
            )
        )

        user = storage.get_user(
            user_id
        )

        if not user:

            print(
                "\nUser not found."
            )

            return

        recommendations = (
            recommendation_engine
            .recommend_products(
                user_id
            )
        )

        print(
            "\nRECOMMENDATIONS"
        )

        print("=" * 60)

        for score, product in recommendations:

            print(
                f"\n{product.name}"
                f" | Score: {score}"
            )

            reasons = (
                recommendation_engine
                .explain_recommendation(
                    user_id,
                    product
                )
            )

            print(
                "Reason:",
                ", ".join(reasons)
            )

            print("-" * 60)

        log_event(
            f"Recommendations generated for user {user_id}"
        )

    except ValueError:

        print(
            "Invalid User ID."
        )


def view_analytics(
    analytics_engine
):

    print(
        "\nCATEGORY DISTRIBUTION"
    )

    print("=" * 60)

    stats = (
        analytics_engine
        .category_distribution()
    )

    for category, count in stats.items():

        print(
            f"{category}: {count}"
        )

    print(
        "\nAVERAGE RATING BY CATEGORY"
    )

    print("=" * 60)

    ratings = (
        analytics_engine
        .average_rating_by_category()
    )

    for category, rating in ratings.items():

        print(
            f"{category}: {rating}"
        )


def generate_recommendation_report(
    storage,
    recommendation_engine
):

    try:

        user_id = int(
            input(
                "\nEnter User ID: "
            )
        )

        user = storage.get_user(
            user_id
        )

        if not user:

            print(
                "User not found."
            )

            return

        recommendations = (
            recommendation_engine
            .recommend_products(
                user_id
            )
        )

        path = (
            ReportService
            .recommendation_report(
                user,
                recommendations
            )
        )

        print(
            f"\nReport saved to:"
        )

        print(path)

        log_event(
            f"Recommendation report generated for user {user_id}"
        )

    except ValueError:

        print(
            "Invalid User ID."
        )


def generate_analytics_report(
    analytics_engine
):

    stats = (
        analytics_engine
        .category_distribution()
    )

    path = (
        ReportService
        .analytics_report(
            stats
        )
    )

    print(
        "\nAnalytics report saved to:"
    )

    print(path)

    log_event(
        "Analytics report generated"
    )


def main():

    storage = DataStorage()

    recommendation_engine = (
        RecommendationService(
            storage
        )
    )

    analytics_engine = (
        AnalyticsService(
            storage
        )
    )

    while True:

        print("\n")
        print("=" * 60)
        print(
            "E-COMMERCE PRODUCT RECOMMENDATION ENGINE"
        )
        print("=" * 60)

        print("1. View Products")
        print("2. View Users")
        print("3. Generate Recommendations")
        print("4. View Analytics")
        print("5. Generate Recommendation Report")
        print("6. Generate Analytics Report")
        print("7. Exit")

        choice = input(
            "\nEnter Choice: "
        )

        # --------------------------------
        # View Products
        # --------------------------------

        if choice == "1":

            view_products(
                storage
            )

        # --------------------------------
        # View Users
        # --------------------------------

        elif choice == "2":

            view_users(
                storage
            )

        # --------------------------------
        # Recommendations
        # --------------------------------

        elif choice == "3":

            generate_recommendations(
                storage,
                recommendation_engine
            )

        # --------------------------------
        # Analytics
        # --------------------------------

        elif choice == "4":

            view_analytics(
                analytics_engine
            )

        # --------------------------------
        # Recommendation Report
        # --------------------------------

        elif choice == "5":

            generate_recommendation_report(
                storage,
                recommendation_engine
            )

        # --------------------------------
        # Analytics Report
        # --------------------------------

        elif choice == "6":

            generate_analytics_report(
                analytics_engine
            )

        # --------------------------------
        # Exit
        # --------------------------------

        elif choice == "7":

            print(
                "\nThank you for using the system!"
            )

            log_event(
                "Application closed"
            )

            break

        # --------------------------------
        # Invalid Input
        # --------------------------------

        else:

            print(
                "\nInvalid choice. Please try again."
            )


if __name__ == "__main__":

    main()