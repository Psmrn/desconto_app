from typing import Any


class MemoryDatabase:
    """Banco de dados em memória (camada de frameworks e drivers)."""

    def __init__(self) -> None:
        self.pedidos: list[Any] = []