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
```

### Instale as dependências:

```bash
pip install -r requirements.txt
```

### 2. Inicie o servidor FastAPI:
Execute o seguinte comando para rodar a aplicação:

```bash
uvicorn app.main:app --reload
```

### 3. Acesse a documentação da API:
Depois de iniciar o servidor, você pode acessar a documentação interativa da API em:

```arduino
http://127.0.0.1:8000/docs
```
### 4. Teste os endpoints:
Use o Postman ou cURL para interagir com a API e testar os endpoints.

## Exemplo de Requisições

### 1. Obter dados de ações
Requisição POST para /get_stock_data/:

```bash

curl -X POST http://127.0.0.1:8000/get_stock_data/ \
  -H "Content-Type: application/json" \
  -d '{"symbol": "DIS", "start_date": "2018-01-01", "end_date": "2024-07-20"}'
  ```
### 2. Treinar o modelo
Requisição POST para /train_model/:

 ```bash
curl -X POST http://127.0.0.1:8000/train_model/ \
  -H "Content-Type: application/json" \
  -d '{"symbol": "DIS", "start_date": "2018-01-01", "end_date": "2024-07-20"}'
   ```

### 3. Fazer previsões
Requisição POST para /predict/:

 ```bash
curl -X POST http://127.0.0.1:8000/predict/ \
  -H "Content-Type: application/json" \
  -d '{"symbol": "DIS", "start_date": "2024-01-01", "end_date": "2024-07-20"}'
   ```

## Dependências
As dependências do projeto são listadas no arquivo requirements.txt e podem ser instaladas com o comando:   

 ```bash
pip install -r requirements.txt
 ```

## Principais dependências:
- fastapi: Framework para construção da API.
- uvicorn: Servidor ASGI para executar a aplicação FastAPI.
- tensorflow: Biblioteca para construção e treinamento do modelo LSTM.
- yfinance: Biblioteca para download de dados históricos de ações.
- pandas: Biblioteca para manipulação de dados.
- sklearn: Biblioteca para métricas e pré-processamento de dados.
