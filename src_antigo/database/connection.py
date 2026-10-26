from typing import Any


class DatabaseConnection:
    """Classe de conexão com o banco de dados (aqui, uma lista em memória)."""

    def __init__(self) -> None:
        self.pedidos: list[Any] = []