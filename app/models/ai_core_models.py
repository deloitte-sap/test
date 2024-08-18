from pydantic import BaseModel
from typing import Any, Dict

class PredictionRequest(BaseModel):
    model_id: str
    input_data: Dict[str, Any]

class PredictionResponse(BaseModel):
    prediction: Any