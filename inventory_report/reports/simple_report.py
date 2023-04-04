from collections import Counter
from datetime import date


class SimpleReport:
    @staticmethod
    def generate(list):
        manufaturing_date = [info["data_de_fabricacao"] for info in list]
        expiration_date = [
            info["data_de_validade"]
            for info in list
            if info["data_de_validade"] > str(date.today())
        ]
        companies = [info["nome_da_empresa"] for info in list]
        company_with_more_products = Counter(companies).most_common()[0]
        return (
            f"Data de fabricação mais antiga: {min(manufaturing_date)}\n"
            f"Data de validade mais próxima: {min(expiration_date)}\n"
            f"Empresa com mais produtos: {company_with_more_products[0]}"
        )
