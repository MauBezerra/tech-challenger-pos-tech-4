from pydantic import BaseModel

# Modelo para entrada de dados via API
class StockRequest(BaseModel):
    symbol: str
    start_date: str
    end_date: str
