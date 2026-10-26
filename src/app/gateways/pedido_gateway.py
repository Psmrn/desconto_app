import abc
from typing import Any

from src.app.entities.pedido import Pedido


class IPedidoGateway(abc.ABC):
    """Contrato: o caso de uso precisa de alguém que salve e liste pedidos."""

    @abc.abstractmethod
    def salvar(self, pedido: Pedido, tipo_desconto: str) -> None:
        pass

    @abc.abstractmethod
    def listar(self) -> list[dict[str, Any]]:
        """Retorna registros no formato {"pedido": Pedido, "tipo_desconto": str}."""
        pass