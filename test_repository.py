import pytest
from datetime import datetime, timedelta
from task_manager.task import Task, Priority
from task_manager.repository import TaskRepository

# Cria um prazo válido para os testes
prazo_valido = datetime.now() + timedelta(days=1)
task_base = Task(None, "Teste Repo", "Desc Repo", Priority.MEDIA, prazo_valido)


def test_save_atribui_id(mocker):
    # 1. Teste save atribui ID
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)

    task = task_base  # Usa a task base
    resultado = repo.save(task)

    assert resultado.id == 1
    assert repo._next_id == 2  # Verifica se o ID foi incrementado


def test_save_chama_storage_add(mocker):
    # 2. Teste save chama storage.add
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)

    task = task_base
    repo.save(task)

    # Verifica se o método add foi chamado uma vez, com o ID e o objeto task
    mock_storage.add.assert_called_once_with(1, task)


def test_find_by_id_chama_storage_get(mocker):
    # 3. Teste find_by_id chama storage.get
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)

    repo.find_by_id(1)

    # Verifica se o método get foi chamado com o ID
    mock_storage.get.assert_called_once_with(1)


def test_find_all_retorna_lista(mocker):
    # 4. Teste find_all retorna lista
    mock_storage = mocker.Mock()
    # Configura o mock para retornar uma lista de tarefas
    tarefas_mock = [task_base, task_base]
    mock_storage.get_all.return_value = tarefas_mock

    repo = TaskRepository(mock_storage)

    resultado = repo.find_all()

    mock_storage.get_all.assert_called_once()
    assert resultado == tarefas_mock
    assert isinstance(resultado, list)


def test_delete_chama_storage_delete(mocker):
    # Teste adicional: delete chama storage.delete
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)

    repo.delete(5)

    mock_storage.delete.assert_called_once_with(5)


def test_save_atualiza_task_existente(mocker):
    # Teste adicional: save atualiza se o ID já existir
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)

    task = Task(5, "Task Existente", "Desc", Priority.MEDIA, prazo_valido)

    # Simula a atualização
    resultado = repo.save(task)

    # Não deve alterar o _next_id
    assert resultado.id == 5
    assert repo._next_id == 1
    mock_storage.add.assert_called_once_with(5, task)