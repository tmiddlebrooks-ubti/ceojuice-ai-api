

import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Body

from ceojuice_client import CEOJuiceClient
from ai_engine import (
    summarize_comments,
    detect_anomalies,
    forecast_usage,
    summarize_service_calls,
)

load_dotenv()

CUSTOMER_ID = os.getenv("CUSTOMER_ID")
API_KEY_ID125 = os.getenv("API_KEY_ID125")
API_KEY_ID29 = os.getenv("API_KEY_ID29")
API_KEY_ID968 = os.getenv("API_KEY_ID968")
API_KEY_ID136 = os.getenv("API_KEY_ID136")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = CEOJuiceClient(
    customer_id=CUSTOMER_ID,
    api_keys={
        "125": API_KEY_ID125,
        "29": API_KEY_ID29,
        "968": API_KEY_ID968,
        "136": API_KEY_ID136,
    },
)

app = FastAPI()


@app.get("/ai/id125/summaries")
def get_survey_summaries():
    try:
        comments = client.get_survey_comments(process_id=125)
        summary = summarize_comments(
            comments,
            OPENAI_API_KEY,
        )
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/ai/id29/meters")
def get_meter_data():
    try:
        data = client.get_fmaudit_meters(process_id=29)
        anomalies = detect_anomalies(data)
        forecast = forecast_usage(data)
        return {
            "data": data,
            "anomalies": anomalies,
            "forecast": forecast,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ai/id968/post-meter")
def post_meter_readings(readings: list):
    try:
        result = client.post_meter_readings(
            process_id=968,
            readings=readings,
        )
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/ai/id136/service-calls")
def get_service_call_summaries():
    try:
        calls = client.get_service_calls(process_id=136)
        summary = summarize_service_calls(
            calls,
            OPENAI_API_KEY,
        )
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
