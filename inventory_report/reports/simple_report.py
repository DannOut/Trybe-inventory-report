from collections import Counter
from datetime import date


class SimpleReport:
    @staticmethod
    def generate(list):
        manufaturing_date = [item["data_de_fabricacao"] for item in list]
        expiration_date = [
            item["data_de_validade"]
            for item in list
            if item["data_de_validade"] > str(date.today())
        ]
        companies = [item["nome_da_empresa"] for item in list]
        company_with_more_products = Counter(companies).most_common()[0]
        return (
            f"Data de fabricação mais antiga: {min(manufaturing_date)}\n"
            f"Data de validade mais próxima: {min(expiration_date)}\n"
            f"Empresa com mais produtos: {company_with_more_products[0]}"
        )
