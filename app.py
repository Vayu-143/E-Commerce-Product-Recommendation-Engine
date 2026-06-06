import pandas as pd
import streamlit as st

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

# -----------------------------------
# Page Config
# -----------------------------------

st.set_page_config(
    page_title="E-Commerce Recommendation Engine",
    page_icon="🛒",
    layout="wide"
)

# -----------------------------------
# Load Services
# -----------------------------------

storage = DataStorage()

recommendation_engine = (
    RecommendationService(storage)
)

analytics_engine = (
    AnalyticsService(storage)
)

# -----------------------------------
# Sidebar
# -----------------------------------

st.sidebar.title(
    "🛒 Recommendation Engine"
)

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Products",
        "Users",
        "Recommendations",
        "Analytics",
        "Reports"
    ]
)

# -----------------------------------
# Dashboard
# -----------------------------------

if menu == "Dashboard":

    st.title(
        "E-Commerce Product Recommendation Engine"
    )

    st.markdown(
        """
        Industry-Level Recommendation System

        Features:
        - Personalized Recommendations
        - Similarity Scoring
        - Analytics Dashboard
        - Report Generation
        - Heap-Based Ranking
        """
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Products",
            len(
                storage.get_all_products()
            )
        )

    with col2:

        st.metric(
            "Users",
            len(
                storage.get_all_users()
            )
        )

# -----------------------------------
# Products
# -----------------------------------

elif menu == "Products":

    st.header("📦 Products")

    data = []

    for p in storage.get_all_products():

        data.append(
            {
                "ID": p.product_id,
                "Name": p.name,
                "Category": p.category,
                "Rating": p.rating,
                "Price": p.price,
                "Popularity": p.popularity
            }
        )

    st.dataframe(
        pd.DataFrame(data),
        use_container_width=True
    )

# -----------------------------------
# Users
# -----------------------------------

elif menu == "Users":

    st.header("👤 Users")

    data = []

    for u in storage.get_all_users():

        data.append(
            {
                "User ID": u.user_id,
                "Name": u.name,
                "Purchases": len(
                    u.purchase_history
                ),
                "Searches": len(
                    u.search_history
                ),
                "Cart Items": len(
                    u.cart_items
                )
            }
        )

    st.dataframe(
        pd.DataFrame(data),
        use_container_width=True
    )

# -----------------------------------
# Recommendations
# -----------------------------------

elif menu == "Recommendations":

    st.header(
        "🎯 Personalized Recommendations"
    )

    users = {
        user.user_id: user.name
        for user in (
            storage.get_all_users()
        )
    }

    selected_user = st.selectbox(
        "Select User",
        list(users.keys()),
        format_func=lambda x:
        f"{x} - {users[x]}"
    )

    if st.button(
        "Generate Recommendations"
    ):

        recommendations = (
            recommendation_engine
            .recommend_products(
                selected_user
            )
        )

        if not recommendations:

            st.warning(
                "No recommendations found."
            )

        else:

            for score, product in (
                recommendations
            ):

                st.success(
                    f"{product.name}"
                )

                st.write(
                    f"Score: {score}"
                )

                reasons = (
                    recommendation_engine
                    .explain_recommendation(
                        selected_user,
                        product
                    )
                )

                st.write(
                    "Reason:"
                )

                for reason in reasons:

                    st.write(
                        f"✓ {reason}"
                    )

                st.divider()

# -----------------------------------
# Analytics
# -----------------------------------

elif menu == "Analytics":

    st.header(
        "📊 Analytics Dashboard"
    )

    stats = (
        analytics_engine
        .category_distribution()
    )

    st.subheader(
        "Category Distribution"
    )

    df = pd.DataFrame(
        {
            "Category":
            list(stats.keys()),
            "Count":
            list(stats.values())
        }
    )

    st.bar_chart(
        df.set_index(
            "Category"
        )
    )

    ratings = (
        analytics_engine
        .average_rating_by_category()
    )

    st.subheader(
        "Average Rating By Category"
    )

    rating_df = pd.DataFrame(
        {
            "Category":
            list(ratings.keys()),
            "Rating":
            list(ratings.values())
        }
    )

    st.dataframe(
        rating_df,
        use_container_width=True
    )

# -----------------------------------
# Reports
# -----------------------------------

elif menu == "Reports":

    st.header(
        "📄 Report Generation"
    )

    users = {
        user.user_id: user.name
        for user in (
            storage.get_all_users()
        )
    }

    selected_user = st.selectbox(
        "Select User",
        list(users.keys()),
        format_func=lambda x:
        f"{x} - {users[x]}"
    )

    if st.button(
        "Generate Recommendation Report"
    ):

        user = storage.get_user(
            selected_user
        )

        recommendations = (
            recommendation_engine
            .recommend_products(
                selected_user
            )
        )

        path = (
            ReportService
            .recommendation_report(
                user,
                recommendations
            )
        )

        st.success(
            f"Saved: {path}"
        )

    if st.button(
        "Generate Analytics Report"
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

        st.success(
            f"Saved: {path}"
        )