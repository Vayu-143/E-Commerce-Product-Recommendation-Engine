# app.py

import os
import pandas as pd
import plotly.express as px
import streamlit as st

from src.storage.data_storage import DataStorage
from src.services.recommendation_service import RecommendationService
from src.services.analytics_service import AnalyticsService
from src.services.report_service import ReportService


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="E-Commerce Product Recommendation Engine",
    page_icon="🛒",
    layout="wide"
)

# --------------------------------------------------
# LOAD SERVICES
# --------------------------------------------------
storage = DataStorage()

recommendation_engine = (
    RecommendationService(storage)
)

analytics_engine = (
    AnalyticsService(storage)
)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
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

# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------
if menu == "Dashboard":

    st.title(
        "🛒 E-Commerce Product Recommendation Engine"
    )

    st.markdown(
        """
        Industry-Level Recommendation System using:

        - Hash Maps
        - Heap Ranking
        - Similarity Scoring
        - Analytics Dashboard
        - Streamlit
        """
    )

    products = storage.get_all_products()
    users = storage.get_all_users()

    total_products = len(products)
    total_users = len(users)

    avg_rating = round(
        sum(
            p.rating
            for p in products
        ) / total_products,
        2
    )

    total_categories = len(
        set(
            p.category
            for p in products
        )
    )

    st.subheader(
        "📈 System Statistics"
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "📦 Products",
        total_products
    )

    col2.metric(
        "👥 Users",
        total_users
    )

    col3.metric(
        "📂 Categories",
        total_categories
    )

    col4.metric(
        "⭐ Avg Rating",
        avg_rating
    )

    st.divider()

    st.subheader(
        "🔥 Trending Products"
    )

    top_products = sorted(
        products,
        key=lambda p: p.popularity,
        reverse=True
    )[:10]

    trend_df = pd.DataFrame(
        [
            {
                "Product": p.name,
                "Popularity": p.popularity,
                "Rating": p.rating,
                "Price": p.price
            }
            for p in top_products
        ]
    )

    st.dataframe(
        trend_df,
        use_container_width=True
    )

# --------------------------------------------------
# PRODUCTS
# --------------------------------------------------
elif menu == "Products":

    st.header(
        "📦 Product Catalog"
    )

    products = (
        storage.get_all_products()
    )

    cols = st.columns(4)

    for index, product in enumerate(products):

        with cols[index % 4]:

            image_path = (
                f"images/products/"
                f"{product.product_id}.jpg"
            )

            if os.path.exists(
                image_path
            ):
                st.image(
                    image_path,
                    use_container_width=True
                )

            st.markdown(
                f"""
                ### {product.name}

                📂 {product.category}

                ⭐ {product.rating}

                💰 ₹{product.price}

                🔥 {product.popularity}
                """
            )

            st.divider()

# --------------------------------------------------
# USERS
# --------------------------------------------------
elif menu == "Users":

    st.header(
        "👤 Users"
    )

    data = []

    for user in storage.get_all_users():

        data.append(
            {
                "User ID": user.user_id,
                "Name": user.name,
                "Purchases": len(
                    user.purchase_history
                ),
                "Searches": len(
                    user.search_history
                ),
                "Cart Items": len(
                    user.cart_items
                )
            }
        )

    st.dataframe(
        pd.DataFrame(data),
        use_container_width=True
    )

# --------------------------------------------------
# RECOMMENDATIONS
# --------------------------------------------------
elif menu == "Recommendations":

    st.header(
        "🎯 Personalized Recommendations"
    )

    user_ids = [
        u.user_id
        for u in storage.get_all_users()
    ]

    selected_user = st.selectbox(
        "Select User",
        user_ids
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

            for item in recommendations:

                if len(item) == 3:

                    score, product, reasons = item

                else:

                    score, product = item
                    reasons = []

                st.subheader(
                    product.name
                )

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "⭐ Rating",
                    product.rating
                )

                col2.metric(
                    "🔥 Popularity",
                    product.popularity
                )

                col3.metric(
                    "🎯 Score",
                    round(score, 1)
                )

                st.write(
                    "Recommendation Reasons"
                )

                for reason in reasons:

                    st.write(
                        f"✓ {reason}"
                    )

                st.divider()

# --------------------------------------------------
# ANALYTICS
# --------------------------------------------------
elif menu == "Analytics":

    st.header(
        "📊 Analytics Dashboard"
    )

    stats = (
        analytics_engine
        .category_distribution()
    )

    if stats:

        df = pd.DataFrame(
            {
                "Category":
                list(stats.keys()),
                "Count":
                list(stats.values())
            }
        )

        st.subheader(
            "Category Distribution"
        )

        fig = px.pie(
            df,
            names="Category",
            values="Count",
            hole=0.4
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.subheader(
            "Top Products"
        )

        top_products = sorted(
            storage.get_all_products(),
            key=lambda p: p.popularity,
            reverse=True
        )[:10]

        top_df = pd.DataFrame(
            [
                {
                    "Product": p.name,
                    "Popularity": p.popularity,
                    "Rating": p.rating,
                    "Price": p.price
                }
                for p in top_products
            ]
        )

        st.dataframe(
            top_df,
            use_container_width=True
        )

# --------------------------------------------------
# REPORTS
# --------------------------------------------------
elif menu == "Reports":

    st.header(
        "📄 Reports"
    )

    user_ids = [
        u.user_id
        for u in storage.get_all_users()
    ]

    selected_user = st.selectbox(
        "Select User",
        user_ids
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

        with open(
            path,
            "rb"
        ) as file:

            st.download_button(
                label="⬇ Download Recommendation Report",
                data=file,
                file_name="recommendation_report.txt",
                mime="text/plain"
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

        with open(
            path,
            "rb"
        ) as file:

            st.download_button(
                label="⬇ Download Analytics Report",
                data=file,
                file_name="analytics_report.txt",
                mime="text/plain"
            )

