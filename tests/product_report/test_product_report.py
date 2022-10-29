from inventory_report.inventory.product import Product


def test_relatorio_produto():
    nome_do_produto = 'Café'
    nome_da_empresa = 'Baggio'
    data_de_fabricacao = '23/10/22'
    data_de_validade = '23/01/23'
    instrucoes_de_armazenamento = 'em local fresco'
    numero_de_serie = 131313

    report = (f"O produto {nome_do_produto} fabricado em {data_de_fabricacao} "
              f"por {nome_da_empresa} com validade até {data_de_validade} "
              f"precisa ser armazenado {instrucoes_de_armazenamento}.")

    product = Product(
        13,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento
    )

    assert repr(product) == report
