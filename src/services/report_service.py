import os


class ReportService:

    @staticmethod
    def recommendation_report(
        user,
        recommendations
    ):

        os.makedirs(
            "outputs",
            exist_ok=True
        )

        path = (
            "outputs/"
            "recommendation_report.txt"
        )

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                "E-COMMERCE "
                "RECOMMENDATION REPORT\n"
            )

            file.write(
                "=" * 50 + "\n\n"
            )

            file.write(
                f"User: {user.name}\n\n"
            )

            for rank, item in enumerate(
                recommendations,
                start=1
            ):

                score, product = item

                file.write(
                    f"{rank}. "
                    f"{product.name} "
                    f"(Score:{score})\n"
                )

        return path

    @staticmethod
    def analytics_report(
        analytics
    ):

        path = (
            "outputs/"
            "analytics_report.txt"
        )

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                "ANALYTICS REPORT\n"
            )

            file.write(
                "=" * 40 + "\n\n"
            )

            for category, count in (
                analytics.items()
            ):

                file.write(
                    f"{category}: "
                    f"{count}\n"
                )

        return path