from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def test_decorar_relatorio():
    mocked_product = [
        {
            "id": "1",
            "nome_do_produto": "Naruto ultimate ninja 3",
            "nome_da_empresa": "Konami",
            "data_de_fabricacao": "2021-02-18",
            "data_de_validade": "2023-09-17",
            "numero_de_serie": "XXX0001111",
            "instrucoes_de_armazenamento": "instrucao 1",
        },
    ]

    simple_colored_report = ColoredReport(SimpleReport).generate(
        mocked_product
    )
    complete_colored_report = ColoredReport(CompleteReport).generate(
        mocked_product
    )

    assert ("\033[36m" in simple_colored_report) is True
    assert ("\033[36m" in complete_colored_report) is True
