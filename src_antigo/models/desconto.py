import abc


class IDesconto(abc.ABC):
    """Contrato de desconto: toda regra de desconto sabe calcular o valor a descontar."""

    @abc.abstractmethod
    def calcular(self, valor: float) -> float:
        pass


class DescontoNormal(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.1


class DescontoVIP(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.2


class DescontoPremium(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.3