from produto import Produto
from venda import Venda

if __name__ == "__main__":
    print("--- Iniciando Sistema de Vendas ---")

    # 1. Criando Produtos
    p1 = Produto("Arroz 5kg", 25.00, 10)
    p2 = Produto("Feijão 1kg", 8.50, 5)
    p3 = Produto("Óleo de Soja", 7.00, 2)

    print("\nEstoque Inicial:")
    print(p1)
    print(p2)
    print(p3)

    # 2. Criando uma Venda
    venda1 = Venda()

    # 3. Adicionando itens
    print("\n--- Adicionando Itens ---")
    venda1.adicionar_item(p1, 2) # Deve funcionar
    venda1.adicionar_item(p2, 1) # Deve funcionar
    
    # Teste de estoque insuficiente
    venda1.adicionar_item(p3, 3) # Deve falhar (estoque é 2)

    # 4. Mostrando a venda parcial
    print("\n--- Resumo da Venda Parcial ---")
    print(venda1)

    # 5. Testando Remoção
    print("\n--- Removendo Item ---")
    venda1.remover_item(p1) 

    print("\n--- Resumo da Venda Final ---")
    print(venda1)

    # 6. Verificando estoque final dos produtos
    print("\n--- Estoque Final dos Produtos ---")
    print(p1) 
    print(p2) 
    print(p3) 
