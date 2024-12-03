# Tech Challenger 4

## Descrição
Este repositório contém um desafio técnico que implementa uma API para obter dados de ações da Yahoo Finance, treinar um modelo LSTM e fazer previsões com base nos dados de ações.

## Endpoints da API
A API é construída com o **FastAPI** e possui os seguintes endpoints:

### 1. `/get_stock_data/`
- **Método**: POST
- **Descrição**: Obtém dados históricos de ações.
- **Exemplo de corpo da requisição**:
    ```json
    {
      "symbol": "DIS",
      "start_date": "2018-01-01",
      "end_date": "2024-07-20"
    }
    ```

### 2. `/train_model/`
- **Método**: POST
- **Descrição**: Treina o modelo LSTM com os dados fornecidos.
- **Exemplo de corpo da requisição**:
    ```json
    {
      "symbol": "DIS",
      "start_date": "2018-01-01",
      "end_date": "2024-07-20"
    }
    ```

### 3. `/predict/`
- **Método**: POST
- **Descrição**: Faz previsões com o modelo treinado.
- **Exemplo de corpo da requisição**:
    ```json
    {
      "symbol": "DIS",
      "start_date": "2024-01-01",
      "end_date": "2024-07-20"
    }
    ```

## Como Executar

### 1. Instale as dependências:
Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Para Windows, use `venv\Scripts\activate`
