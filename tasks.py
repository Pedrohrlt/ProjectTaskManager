from enum import IntEnum, Enum
from datetime import datetime


class Priority(IntEnum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3


class Status(Enum):
    PENDENTE = "pendente"
    EM_PROGRESSO = "em_progresso"
    CONCLUIDA = "concluida"


class Task:
    def __init__(self, id: int or None, titulo: str, descricao: str, prioridade: Priority, prazo: datetime,
                 status: Status = Status.PENDENTE):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo
        self.status = status

    def validar(self):
        """Verifica se o título tem 3+ caracteres e o prazo não é passado."""
        # 1. Validação do Título
        if not self.titulo or len(self.titulo) < 3:
            raise ValueError("O título da tarefa deve ter no mínimo 3 caracteres.")

        # 2. Validação do Prazo
        # Arredonda a hora atual para o segundo para evitar problemas de comparação milissegundo/nanosegundo
        agora = datetime.now().replace(microsecond=0)
        prazo_limpo = self.prazo.replace(microsecond=0)

        if prazo_limpo <= agora:
            raise ValueError("O prazo da tarefa não pode ser uma data/hora passada.")

    def __repr__(self):
        return f"Task(id={self.id}, titulo='{self.titulo}', status={self.status.value})"
