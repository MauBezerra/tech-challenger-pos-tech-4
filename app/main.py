from fastapi import FastAPI, HTTPException
from app.schemas import StockRequest
from app.data_utils import download_stock_data, normalize_data, create_sequences
from app.models import train_lstm_model, load_trained_model

import os

# Instância do FastAPI
app = FastAPI()

# Rota raiz
@app.get("/")
def read_root():
    return {"message": "Welcome to the Stock Prediction API. Check the documentation at /docs."}

# Endpoint para obter dados de ações
@app.post("/get_stock_data/")
def get_stock_data(request: StockRequest):
    try:
        df = download_stock_data(request.symbol, request.start_date, request.end_date)
        return {"symbol": request.symbol, "data": df.to_dict(orient="records")}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint para treinar o modelo
@app.post("/train_model/")
def train_model(request: StockRequest):
    try:
        # Baixar e pré-processar os dados
        df = download_stock_data(request.symbol, request.start_date, request.end_date)
        scaler, df_scaled = normalize_data(df)
        X, y = create_sequences(df_scaled, window_size=60)

        # Treinar o modelo
        model_path, mae, rmse = train_lstm_model(X, y)

        return {
            "message": "Modelo treinado com sucesso!",
            "mae": mae,
            "rmse": rmse,
            "model_path": model_path
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint para fazer previsões
@app.post("/predict/")
def predict(request: StockRequest):
    try:
        # Baixar e pré-processar os dados
        df = download_stock_data(request.symbol, request.start_date, request.end_date)
        scaler, df_scaled = normalize_data(df)
        X, _ = create_sequences(df_scaled, window_size=60)

        # Carregar o modelo e fazer previsões
        predictions = load_trained_model(X, scaler)
        return {"predictions": predictions.flatten().tolist()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
