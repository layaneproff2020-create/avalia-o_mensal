class Produto:
    def __init__(self, descricao: str, preco_unitario: float, estoque: int):
        self.descricao = descricao
        self.preco_unitario = preco_unitario
        self.estoque = estoque

    def decrementar_estoque(self, quant: int) -> bool:
        """
        Verifica se há estoque suficiente e decrementa.
        Retorna True se sucesso, False se estoque insuficiente.
        """
        if self.estoque >= quant:
            self.estoque -= quant
            return True
        else:
            print(f"Erro: Estoque insuficiente para '{self.descricao}'. Disponível: {self.estoque}, Solicitado: {quant}")
            return False

    def __str__(self):
        return f"{self.descricao} (R$ {self.preco_unitario:.2f}) - Estoque: {self.estoque}"
