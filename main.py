from src.app.adapters.controllers.pedido_controller import PedidoController
from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.presenters.pedido_presenter import PedidoPresenter
from src.app.use_cases.criar_pedido import CriarPedido


def main() -> None:
    # Montando o fluxo completo:
    # database -> repository (gateway) -> use case -> presenter -> controller
    database = MemoryDatabase()
    pedido_gateway = MemoryPedidoRepository(database)
    criar_pedido_use_case = CriarPedido(pedido_gateway)
    presenter = PedidoPresenter()
    controller = PedidoController(criar_pedido_use_case, presenter)

    # Criando os pedidos (o controller devolve cada pedido já formatado)
    print("Pedidos criados:")
    print(controller.criar_pedido("Cliente A", 100.0, "normal"))
    print(controller.criar_pedido("Cliente B", 200.0, "vip"))
    print(controller.criar_pedido("Cliente C", 300.0, "premium"))

    # Listando todos os pedidos já realizados
    print()
    print("Todos os pedidos realizados:")
    for pedido in controller.listar_pedidos():
        print(
            f"{pedido['cliente']} | {pedido['tipo_desconto']} | "
            f"original: {pedido['valor_original']:.2f} | "
            f"desconto: {pedido['valor_desconto']:.2f} | "
            f"final: {pedido['valor_final']:.2f}"
        )


if __name__ == "__main__":
    main()