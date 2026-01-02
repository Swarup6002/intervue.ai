import google.generativeai as genai
import time
import os

# 🔑 YOUR API KEY
GOOGLE_API_KEY = "AIzaSyCh_smoqcA3cIy376_ScwrvCFyy4a6iNrU"

class GeminiClient:
    def __init__(self):
        try:
            genai.configure(api_key=GOOGLE_API_KEY)
            
            # ✅ FIX: Using the model name that works for you
            self.model_name = 'models/gemini-flash-latest' 
            self.model = genai.GenerativeModel(self.model_name)
            
            print(f"✅ Connected to {self.model_name}")
        except Exception as e:
            print(f"❌ Connection Failed: {e}")

    def generate(self, prompt: str):
        """
        Generates content with YOUR automatic retry logic.
        """
        # ⚡ FIX 2: Your Automatic Retry Logic
        max_retries = 3
        for attempt in range(max_retries):
            try:
                # print(f"🚀 Sending request to Gemini (Attempt {attempt+1})...")
                response = self.model.generate_content(prompt)
                return response.text
            
            except Exception as e:
                error_str = str(e)
                # If it's a "Quota" or "Rate Limit" error
                if "429" in error_str or "Quota" in error_str:
                    wait_time = 5 + (attempt * 2) 
                    print(f"⚠️ Rate Limit Hit. Waiting {wait_time}s to retry...")
                    time.sleep(wait_time)
                else:
                    print(f"❌ API Error: {e}")
                    # If it's a 404/Model error, don't retry, just break
                    break
        
        return None