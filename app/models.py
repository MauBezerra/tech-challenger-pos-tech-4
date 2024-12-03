import os
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np


# Treinar o modelo LSTM
def train_lstm_model(X, y):
    # Dividir os dados em treino e teste
    train_size = int(len(X) * 0.8)
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    # Reshape para o formato LSTM
    X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
    X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

    # Criar o modelo
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], 1)),
        LSTM(50),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')

    # Treinar o modelo
    model.fit(X_train, y_train, epochs=10, batch_size=32)

    # Avaliar o modelo
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred, squared=False)

    # Salvar o modelo
    model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model_storage")
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, 'modelo_lstm.keras')
    model.save(model_path)

    return model_path, mae, rmse


# Carregar o modelo e fazer previsões
def load_trained_model(X, scaler):
    model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model_storage")
    model_path = os.path.join(model_dir, 'modelo_lstm.keras')

    # Carregar modelo treinado
    model = load_model(model_path)

    # Fazer previsões
    predictions = model.predict(X)
    predictions_rescaled = scaler.inverse_transform(predictions)

    return predictions_rescaled
