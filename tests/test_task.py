import pytest
from datetime import datetime, timedelta
from task_manager.task import Task, Priority, Status

# Cria um prazo válido para os testes (amanhã)
prazo_valido = datetime.now() + timedelta(days=1)


def test_task_valida_e_status_padrao():
    # 1. Teste de criação válida
    task = Task(None, "Estudar Python", "Orientacao a Objetos", Priority.ALTA, prazo_valido)
    task.validar()  # Nao deve lancar erro

    assert task.titulo == "Estudar Python"
    assert task.prioridade == Priority.ALTA
    assert task.status == Status.PENDENTE  # Verifica status padrão


def test_titulo_curto_invalido():
    # 2. Teste de título inválido (deve lançar ValueError)
    task = Task(None, "AB", "Desc", Priority.BAIXA, prazo_valido)
    with pytest.raises(ValueError, match="no mínimo 3 caracteres"):
        task.validar()


def test_titulo_vazio_invalido():
    # Teste adicional: Título vazio
    task = Task(None, "", "Desc", Priority.BAIXA, prazo_valido)
    with pytest.raises(ValueError, match="no mínimo 3 caracteres"):
        task.validar()


def test_prazo_passado_invalido():
    # 3. Teste de prazo no passado (deve lançar ValueError)
    prazo_passado = datetime.now() - timedelta(seconds=1)
    task = Task(None, "Título OK", "Desc", Priority.MEDIA, prazo_passado)
    with pytest.raises(ValueError, match="não pode ser uma data/hora passada"):
        task.validar()


def test_prazo_exatamente_agora_invalido():
    # Teste adicional: Prazo exatamente 'agora'
    agora = datetime.now()
    task = Task(None, "Título OK", "Desc", Priority.MEDIA, agora)
    # A validação arredonda, então deve falhar
    with pytest.raises(ValueError, match="não pode ser uma data/hora passada"):
        task.validar()
