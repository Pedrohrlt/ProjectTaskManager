from .storage import InMemoryStorage
from .task import Task, Status


class TaskRepository:
    def __init__(self, storage: InMemoryStorage):
        self.storage = storage
        self._next_id = 1

    def save(self, task: Task) -> Task:
        """Atribui ID se for novo, salva no storage, retorna task."""

        # Se a tarefa não tem ID, é nova, atribui e incrementa
        if task.id is None:
            task.id = self._next_id
            self._next_id += 1

        # O storage não se importa se está atualizando ou criando
        self.storage.add(task.id, task)
        return task

    def find_by_id(self, id: int) -> Task or None:
        """Busca e retorna task ou None."""
        return self.storage.get(id)

    def find_all(self) -> list[Task]:
        """Retorna lista de todas as tasks."""
        return self.storage.get_all()

    def delete(self, id: int) -> bool:
        """Remove task, retorna True se sucesso."""
        return self.storage.delete(id)
