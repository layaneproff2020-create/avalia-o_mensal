from datetime import datetime
from produto import Produto
from item_venda import ItemVenda

class Venda:
    def __init__(self):
        self.data = datetime.now()
        self.valor_total = 0.0
        self.itens = []

    def adicionar_item(self, produto: Produto, quant: int):
        """
        Tenta adicionar um item à venda.
        Só adiciona se houver estoque disponível no produto.
        """
        if produto.decrementar_estoque(quant):
            novo_item = ItemVenda(produto, quant)
            self.itens.append(novo_item)
            self.calcular_total()
            print(f"Item adicionado: {novo_item}")
        else:
            print("Falha ao adicionar item: Estoque insuficiente.")

    def remover_item(self, produto: Produto):
        """
        Remove um item da venda baseado no produto e devolve ao estoque.
        """
        for item in self.itens:
            if item.produto == produto:
                produto.estoque += item.quantidade
                self.itens.remove(item)
                self.calcular_total()
                print(f"Item removido: {produto.descricao}")
                return
        print(f"Item '{produto.descricao}' não encontrado nesta venda.")

    def calcular_total(self) -> float:
        """Recalcula o valor total da venda somando os subtotais."""
        self.valor_total = sum(item.calcular_subtotal() for item in self.itens)
        return self.valor_total

    def __str__(self):
        info = f"Venda em {self.data.strftime('%d/%m/%Y %H:%M')}\n"
        info += "Itens:\n"
        for item in self.itens:
            info += f"  - {item}\n"
        info += f"Total: R$ {self.valor_total:.2f}"
        return info
