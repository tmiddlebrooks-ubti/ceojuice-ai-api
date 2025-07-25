

- import os
+import requests

 
 class CEOJuiceClient:
     def __init__(self, customer_id, api_keys):
         self.base_url = "https://api.ceojuice.com"
         self.customer_id = customer_id
         self.api_keys = api_keys

 
     def _headers(self, process_id):
-        return {
+        return {
             "CustomerNumber": self.customer_id,
             "ApiKey": self.api_keys.get(str(process_id)),
             "Content-Type": "application/json",
         }

 
     def get_survey_comments(self, process_id=125):
-        url = f"{self.base_url}/Process/{process_id}/Comments"
+        url = (
+            f"{self.base_url}"
+            f"/Process/{process_id}/Comments"
+        )
         response = requests.get(url, headers=self._headers(process_id))
         response.raise_for_status()
         return response.json()
