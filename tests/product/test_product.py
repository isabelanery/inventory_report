from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1, 'Café', 'Baggio', '23/10/22', '23/01/23', 131313, 'em local fresco'
    )

    assert product.id == 1
    assert product.nome_do_produto == 'Café'
    assert product.nome_da_empresa == 'Baggio'
    assert product.data_de_fabricacao == '23/10/22'
    assert product.data_de_validade == '23/01/23'
    assert product.numero_de_serie == 131313
    assert product.instrucoes_de_armazenamento == 'em local fresco'
