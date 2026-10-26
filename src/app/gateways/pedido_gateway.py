import abc

from src.app.entities.pedido import Pedido


class IPedidoGateway(abc.ABC):
    """Contrato: o caso de uso precisa de alguém que salve e liste pedidos."""

    @abc.abstractmethod
    def salvar(self, pedido: Pedido) -> None:
        pass

    @abc.abstractmethod
    def listar(self) -> list[Pedido]:
        pass