

import requests


class CEOJuiceClient:
    def __init__(
        self,
        customer_id: str,
        api_keys: dict,
    ):
        self.base_url = "https://api.ceojuice.com"
        self.customer_id = customer_id
        self.api_keys = api_keys

    def _headers(self, process_id: int) -> dict:
        return {
            "CustomerNumber": self.customer_id,
            "ApiKey": self.api_keys.get(str(process_id)),
            "Content-Type": "application/json",
        }

    def get_survey_comments(
        self,
        process_id: int = 125,
    ) -> list:
        url = f"{self.base_url}/Process/{process_id}/Comments"
        resp = requests.get(url, headers=self._headers(process_id))
        resp.raise_for_status()
        return resp.json()

    def get_fmaudit_meters(
        self,
        process_id: int = 29,
    ) -> list:
        url = f"{self.base_url}/Process/{process_id}/MeterData"
        resp = requests.get(url, headers=self._headers(process_id))
        resp.raise_for_status()
        return resp.json()

    def post_meter_readings(
        self,
        process_id: int = 968,
        readings: list | None = None,
    ) -> dict:
        url = f"{self.base_url}/Process/{process_id}/Readings"
        payload = readings or []

        resp = requests.post(
            url,
            json=payload,
            headers=self._headers(process_id),
        )
        resp.raise_for_status()
        return resp.json()

    def get_service_calls(
        self,
        process_id: int = 136,
    ) -> list:
        url = f"{self.base_url}/Process/{process_id}/ServiceCalls"
        resp = requests.get(url, headers=self._headers(process_id))
        resp.raise_for_status()
        return resp.json()
