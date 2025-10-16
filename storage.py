class InMemoryStorage:
    def __init__(self):
        self._data = {}

    def add(self, id: int, item):
        """Adiciona item com chave id."""
        self._data[id] = item

    def get(self, id: int):
        """Retorna item ou None."""
        return self._data.get(id)

    def get_all(self) -> list:
        """Retorna lista com todos os valores."""
        return list(self._data.values())

    def delete(self, id: int) -> bool:
        """Remove item, retorna True se removeu, False caso contrário."""
        if id in self._data:
            del self._data[id]
            return True
        return False

    def clear(self):
        """Limpa tudo."""
        self._data = {}
