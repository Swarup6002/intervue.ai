from backend.gemini_client import GeminiClient
import json
import re

class Evaluator:
    def __init__(self):
        self.client = GeminiClient()

    def evaluate(self, question, user_answer, language="English"):
        print(f"🚀 Evaluator: Analyzing answer...")

        # ✅ Your Prompt Structure
        prompt = f"""
        You are a Technical Interviewer.
        
        Context:
        - Question: {question}
        - Candidate Answer: {user_answer}
        
        Task:
        1. Compare the Candidate Answer with the technical facts.
        2. Provide feedback in the requested language: {language}.
        
        Output Format (Strict JSON):
        {{
            "score": 0,
            "feedback": "...",
            "correct_solution": "..."
        }}
        
        IMPORTANT: Return ONLY the JSON. No markdown formatting.
        """

        response_text = self.client.generate(prompt)

        # 1. Handle Network/API Failures
        if not response_text:
            return {
                "score": 0,
                "feedback": "Server is busy (Rate Limit) or Model not found. Please wait 1 minute.",
                "correct_solution": "N/A"
            }

        # 2. Robust JSON Parsing (Fixes "Could not process answer")
        try:
            # Use Regex to extract JSON object even if Gemini adds text around it
            match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if match:
                json_str = match.group(0)
                return json.loads(json_str)
            else:
                # Fallback if no JSON found
                return {
                    "score": 0,
                    "feedback": response_text[:200], # Return raw text as feedback
                    "correct_solution": "N/A"
                }

        except Exception as e:
            print(f"❌ Parsing Error: {e}")
            return {
                "score": 0,
                "feedback": "Error parsing AI response.",
                "correct_solution": "N/A"
            }