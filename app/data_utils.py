import yfinance as yf
import numpy as np
from sklearn.preprocessing import MinMaxScaler


# Baixar dados históricos de ações
def download_stock_data(symbol: str, start_date: str, end_date: str):
    try:
        df = yf.download(symbol, start=start_date, end=end_date)
        if df.empty:
            raise ValueError("Nenhum dado encontrado para o símbolo fornecido.")
        return df[['Close']]
    except Exception as e:
        raise ValueError(f"Erro ao baixar dados: {e}")


# Normalizar os dados
def normalize_data(df):
    scaler = MinMaxScaler(feature_range=(0, 1))
    return scaler, scaler.fit_transform(df)


# Criar sequências de dados
def create_sequences(data, window_size):
    X, y = [], []
    for i in range(window_size, len(data)):
        X.append(data[i-window_size:i, 0])
        y.append(data[i, 0])
    return np.array(X), np.array(y)
