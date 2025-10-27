from datetime import datetime
from .repository import TaskRepository
from .task import Task, Priority, Status


class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def criar_tarefa(self, titulo: str, descricao: str, prioridade: Priority, prazo: datetime) -> Task:
        """Cria, valida e salva uma nova tarefa."""
        task = Task(
            id=None,
            titulo=titulo,
            descricao=descricao,
            prioridade=prioridade,
            prazo=prazo
        )
        task.validar()
        return self.repository.save(task)

    def listar_todas(self) -> list[Task]:
        """Retorna todas as tarefas."""
        return self.repository.find_all()

    def atualizar_status(self, task_id: int, novo_status: Status) -> Task:
        """Busca a tarefa, atualiza o status e salva."""
        task = self.repository.find_by_id(task_id)
        if not task:
            raise ValueError(f"Tarefa com ID {task_id} não encontrada.")

        task.status = novo_status
        return self.repository.save(task)

    def buscar_por_id(self, task_id: int) -> Task or None:
        """Busca tarefa por ID."""
        return self.repository.find_by_id(task_id)

    def deletar_tarefa(self, task_id: int) -> bool:
        """Deleta a tarefa por ID."""
        return self.repository.delete(task_id)
