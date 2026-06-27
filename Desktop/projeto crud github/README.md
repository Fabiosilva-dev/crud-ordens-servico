# CRUD - Gerenciamento de Ordens de Serviço

Sistema de backend desenvolvido em Python para o gerenciamento e persistência de Ordens de Serviço (OS), utilizando o banco de dados relacional SQLite. Este projeto foi construído para demonstrar conceitos práticos de Programação Orientada a Objetos (POO) e manipulação de dados estruturados (SQL).

##  Funcionalidades (CRUD)

O sistema implementa o ciclo de vida completo de uma Ordem de Serviço de forma automatizada:
* **Create (Criar):** Inserção de novos serviços com dados validados (Cliente, Equipamento, Defeito, Serviço Realizado, Orçamento, Data e Status).
* **Read (Ler):** Listagem completa de todos os registros salvos no banco e busca detalhada de uma OS específica através do seu ID.
* **Update (Atualizar):** Modificação e atualização dinâmica de qualquer dado de uma OS existente.
* **Delete (Deletar):** Remoção segura de registros do banco de dados por ID.

## 🛠️ Tecnologias Utilizadas

* **Python 3** (Lógica de programação e POO)
* **SQLite3** (Banco de dados relacional embutido para persistência de dados)
* **Componente `os`** (Manipulação de caminhos absolutos para garantir que o banco seja criado no diretório correto do projeto)

## 📁 Estrutura do Projeto

* `crud_2.py`: Arquivo principal contendo a classe `OrdemDeServico` e a lógica de execução dos testes.
* `ordens_servico.db`: Banco de dados gerado automaticamente pelo script.

## 🔧 Como Executar o Projeto

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone o repositório ou baixe o arquivo `crud_2.py`.
3. Abra o terminal na pasta do arquivo e execute o comando:
   ```bash
   python crud_2.py