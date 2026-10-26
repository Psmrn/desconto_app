from src_antigo.models.desconto import IDesconto


class Pedido:
    """Representa um pedido de um cliente com o tipo de desconto aplicado."""

    def __init__(self, cliente: str, desconto: IDesconto) -> None:
        self.cliente = cliente
        self.desconto = desconto
        self.valor_original = 0.0

    def valor_final(self, valor: float) -> float:
        self.valor_original = valor
        return self.valor_original - self.desconto.calcular(self.valor_original)