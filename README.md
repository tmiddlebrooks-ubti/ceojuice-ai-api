# CEO Juice AI API Integration

This project provides a FastAPI-based AI-enhanced interface to CEO Juice web services.

## Setup

1. Copy `.env.sample` to `.env` and add your credentials:
   ```
   CUSTOMER_ID=051
   API_KEY_ID125=...
   API_KEY_ID29=...
   API_KEY_ID968=...
   API_KEY_ID136=...
   OPENAI_API_KEY=...
   ```

2. Build and run with Docker:
   ```
   docker build -t ceojuice-ai-api .
   docker run -d -p 8000:8000 --env-file .env ceojuice-ai-api
   ```

3. Endpoints:
   - `GET /ai/id125/summaries` – Survey comment summaries
   - `GET /ai/id29/meters` – Meter data with anomalies & forecast
   - `POST /ai/id968/post-meter` – Post meter readings
   - `GET /ai/id136/service-calls` – Service call summaries

4. Power BI
   - Open `powerbi_template.pbix` in Power BI Desktop
   - Set the data source to `https://<your-host>/ai/id125/summaries` using `Web.Contents()`
