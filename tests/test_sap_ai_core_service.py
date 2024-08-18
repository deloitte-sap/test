
import os
import pytest
from app.services.sap_ai_core_service import SAPAICoreService

@pytest.fixture
def sap_ai_core_service():
    os.environ["SAP_AI_CORE_BASE_URL"] = "https://example.com"
    os.environ["SAP_AI_CORE_API_KEY"] = "testapikey"
    return SAPAICoreService()

def test_get_model_prediction(sap_ai_core_service, requests_mock):
    model_id = "test_model"
    input_data = {"key": "value"}
    expected_output = {"prediction": "test_prediction"}
    
    requests_mock.post(f"https://example.com/models/{model_id}/predict", =expected_output)
    
    prediction = sap_ai_core_service.get_model_prediction(model_id, input_data)
    assert prediction == expected_output
