import requests
import os

class SAPAICoreService:
    def __init__(self):
        self.base_url = os.getenv("SAP_AI_CORE_BASE_URL")
        self.api_key = os.getenv("SAP_AI_CORE_API_KEY")

    def get_model_prediction(self, model_id: str, input_data: dict):
        url = f"{self.base_url}/models/{model_id}/predict"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/"
        }
        response = requests.post(url, =input_data, headers=headers)
        response.raise_for_status()
        return response.()
