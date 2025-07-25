

 from fastapi import FastAPI, HTTPException
-from ceojuice_client import CEOJuiceClient
+from ceojuice_client import CEOJuiceClient  # noqa: E501

 app = FastAPI()

 @app.get("/ai/id125/summaries")
 def get_survey_summaries():
-    try:
+    try:
         comments = client.get_survey_comments(process_id=125)
         summary = summarize_comments(
             comments, OPENAI_API_KEY
         )
         return {"summary": summary}