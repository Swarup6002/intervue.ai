from backend.gemini_client import GeminiClient

class QuestionEngine:
    def __init__(self):
        self.client = GeminiClient()

    def get_question(self, topic: str, difficulty: str, experience_level: str = "Fresher", history: list = []):
        # 1. Context
        past_questions = [h.get('question', '') for h in history[-3:]]

        # 2. Adjust instructions based on level
        level_instruction = ""
        if experience_level == "Fresher":
            level_instruction = "Target Audience: Fresh Graduate / Student. Ask theoretical concepts, definitions, basic syntax, and standard algorithms. Avoid complex architecture questions."
        else:
            level_instruction = "Target Audience: Experienced Professional. Ask about system design, scalability, edge cases, real-world scenarios, and deep internal workings."

        # 3. Prompt
        prompt = f"""
        You are a Technical Interviewer for the domain: {topic}.
        
        {level_instruction}
        
        Task: Generate ONE {difficulty}-level interview question about {topic}.
        
        Constraints:
        1. Output ONLY the question text.
        2. Do NOT repeat: {past_questions}
        3. If topic is Hardware/Embedded, stick to C/Registers, NOT Python.
        """

        # 4. Generate
        response_text = self.client.generate(prompt)
        
        if response_text:
            return response_text.strip()
        else:
            return f"Explain the fundamental concepts of {topic}."