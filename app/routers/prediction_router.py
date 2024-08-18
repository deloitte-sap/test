from fastapi import APIRouter, HTTPException, Depends
from app.models.ai_core_models import PredictionRequest, PredictionResponse
from app.services.sap_ai_core_service import SAPAICoreService
from app.security import get_api_key
from typing import Any

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse, dependencies=[Depends(get_api_key)])
def get_prediction(request: PredictionRequest, service: SAPAICoreService = Depends(SAPAICoreService)):
    try:
        prediction = service.get_model_prediction(request.model_id, request.input_data)
        return PredictionResponse(prediction=prediction)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
