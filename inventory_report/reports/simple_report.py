from datetime import datetime


class SimpleReport:
    def __init__(self, products):
        self.products = products

    @staticmethod
    def get_oldest_fabrication_date(products):
        return min(product["data_de_fabricacao"] for product in products)

    @staticmethod
    def get_closest_expiration_date(products):
        return min(
            product["data_de_validade"] for product in products
            if product["data_de_validade"] >= str(datetime.now().date())
        )

    @staticmethod
    def count_company_products(products):
        companies = {}

        for product in products:
            if product["nome_da_empresa"] in companies:
                companies[product["nome_da_empresa"]] += 1
            else:
                companies[product["nome_da_empresa"]] = 1

        return companies

    @classmethod
    def get_company_with_most_products(cls, products):
        companies_products_count = cls.count_company_products(products)
        return max(companies_products_count, key=companies_products_count.get)

    @classmethod
    def generate(cls, products):
        oldest_fabrication = cls.get_oldest_fabrication_date(products)
        closest_expiration_date = cls.get_closest_expiration_date(products)
        companies_products_count = cls.get_company_with_most_products(products)

        return (
            f"Data de fabricação mais antiga: {oldest_fabrication}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {companies_products_count}"
        )
