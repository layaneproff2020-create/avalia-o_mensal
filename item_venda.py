from produto import Produto

class ItemVenda:
    def __init__(self, produto: Produto, quantidade: int):
        self.produto = produto
        self.quantidade = quantidade
        self.valor_item = produto.preco_unitario * quantidade

    def calcular_subtotal(self) -> float:
        """Retorna o valor total deste item (preço * quantidade)."""
        return self.produto.preco_unitario * self.quantidade

    def __str__(self):
        return f"{self.quantidade}x {self.produto.descricao} = R$ {self.calcular_subtotal():.2f}"
