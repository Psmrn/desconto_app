from src.app.use_cases.criar_pedido import CriarPedido


def main() -> None:
    criar_pedido = CriarPedido()

    pedido1 = criar_pedido.executar("Cliente A", 100.0, "normal")
    pedido2 = criar_pedido.executar("Cliente B", 100.0, "vip")
    pedido3 = criar_pedido.executar("Cliente C", 100.0, "premium")

    print("Pedidos criados:")
    for pedido in (pedido1, pedido2, pedido3):
        print(pedido.cliente, pedido.valor_original, pedido.valor_final())


if __name__ == "__main__":
    main()