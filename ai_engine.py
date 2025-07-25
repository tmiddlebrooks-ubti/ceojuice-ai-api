

- import os
 from typing import List
 try:
     import openai
 except ImportError:
     openai = None

 
-def summarize_comments(comments: List[dict], api_key: str):
+def summarize_comments(
+    comments: List[dict],
+    api_key: str
+) -> str:
     text = "\n".join([c.get("commentText", "") for c in comments])
     if openai and api_key:
         openai.api_key = api_key
         response = openai.ChatCompletion.create(
-            model="gpt-4", messages=[{"role": "user", "content": f"Summarize these comments:\n{text}"}]
+            model="gpt-4",
+            messages=[
+                {"role": "user", 
+                 "content": f"Summarize these comments:\n{text}"}
+            ],
         )
         return response.choices[0].message.content
     # Fallback simple summary
     return " ".join(text.split()[:100]) + "..."
 
 
-def detect_anomalies(data: List[dict]):
+def detect_anomalies(
+    data: List[dict]
+) -> List[dict]:
     # Stub: flag entries with value beyond 2x average
     values = [d.get("meterValue", 0) for d in data]
     avg = sum(values) / len(values) if values else 0
     anomalies = [
         d
         for d in data
         if d.get("meterValue", 0) > 2 * avg
     ]
     return anomalies


-def forecast_usage(data: List[dict]):
+def forecast_usage(
+    data: List[dict]
+) -> dict:
     # Stub: simple next value forecast = last + (last - first)
     if not data:
         return {}
     first = data[0].get("meterValue", 0)
     last = data[-1].get("meterValue", 0)
     return {"forecastNext": last + (last - first)}


-def summarize_service_calls(calls: List[dict], api_key: str):
+def summarize_service_calls(
+    calls: List[dict],
+    api_key: str
+) -> str:
     text = "\n".join([c.get("issueDescription", "") for c in calls])
     if openai and api_key:
         openai.api_key = api_key
         response = openai.ChatCompletion.create(
-            model="gpt-4", messages=[{"role": "user", "content": f"Summarize these service calls:\n{text}"}]
+            model="gpt-4",
+            messages=[
+                {"role": "user", 
+                 "content": f"Summarize these service calls:\n{text}"}
+            ],
         )
         return response.choices[0].message.content
     return " ".join(text.split()[:100]) + "..."
