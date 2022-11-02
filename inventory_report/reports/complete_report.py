from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        simple_report = super().generate(products)
        companies_products = super().count_company_products(products)

        companies_report = "".join(
            f"- {key}: {value}\n" for key, value in companies_products.items()
        )

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{companies_report}"
        )
