# Sistema de Gerenciamento de Tarefas (Task Manager)

## Objetivo do Projeto

Este projeto implementa um sistema simples de gerenciamento de tarefas em Python, seguindo uma **arquitetura em camadas** (Entidade, Armazenamento, Repositório e Serviço) e aplicando o princípio da **separação de responsabilidades**.

O sistema permite:
* Criar tarefas com título, descrição, prioridade e prazo.
* Listar todas as tarefas.
* Buscar tarefas por ID.
* Atualizar o status de uma tarefa.
* Deletar tarefas.

## Estrutura do Projeto

O projeto está organizado em camadas para facilitar a manutenção e os testes:

task_manager/ ├── task.py # Camada de Entidade (Task, Priority, Status, validação) ├── storage.py # Camada de Armazenamento (InMemoryStorage) ├── repository.py # Camada de Repositório (TaskRepository) ├── service.py # Camada de Serviço/Regras de Negócio (TaskService - Bônus) tests/ ├── test_task.py # Testes para a Entidade Task ├── test_repository.py # Testes para o Repositório (utilizando mocks) requirements.txt # Dependências README.md # Este arquivo


## Tecnologias

* Python 3.8+
* `pytest` (Para testes automatizados)
* `pytest-mock` (Para mockar dependências em testes de repositório)

## Como Instalar

1.  **Instale as dependências** do projeto utilizando o arquivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

2.  (Opcional) Recomendado: Crie e ative um ambiente virtual.

## Como Testar

Para executar os testes automatizados e verificar se todas as regras de negócio e a integração das camadas estão corretas, use o `pytest`:

```bash
pytest -v
Detalhes dos Testes
O projeto inclui:

Mais de 3 testes para a classe Task, incluindo validações de título e prazo (test_task.py).

Mais de 4 testes para a classe TaskRepository, utilizando mocks para garantir que a comunicação com o storage está correta (test_repository.py).
