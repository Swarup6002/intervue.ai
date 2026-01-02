import sys
import os

# Fix imports so they work from anywhere
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uuid
import uvicorn
import json

from backend.database import init_db, get_session, update_session, get_user_sessions
from backend.question_engine import QuestionEngine
from backend.evaluator import Evaluator
from backend.difficulty_controller import DifficultyController

app = FastAPI(title="AI Interviewer")

# --- CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- INITIALIZATION ---
print("🚀 Starting AI Interviewer Backend...")
init_db()
q_engine = QuestionEngine()
evaluator = Evaluator()
diff_controller = DifficultyController()
print("✅ Backend Ready!")

# --- MODELS ---
class StartRequest(BaseModel):
    user_id: str
    topic: str = "General Coding"
    experience_level: str = "Fresher"

class AnswerRequest(BaseModel):
    session_id: str
    question_text: str
    answer: str

# --- ENDPOINTS ---

@app.get("/my_sessions/{user_id}")
def get_my_sessions(user_id: str):
    """Return a list of past interviews for the user."""
    sessions = get_user_sessions(user_id)
    return {"sessions": sessions}

@app.post("/start_interview")
def start_interview(req: StartRequest):
    session_id = str(uuid.uuid4())
    initial_history = [{"meta": "init", "topic": req.topic, "level": req.experience_level}]
    update_session(session_id, "Easy", initial_history, user_id=req.user_id)
    print(f"✅ Session Started: {req.topic} | Level: {req.experience_level}")
    return {"session_id": session_id, "message": "Interview Started"}

@app.get("/get_question/{session_id}")
def get_next_question(session_id: str):
    session_data = get_session(session_id)
    if not session_data:
        raise HTTPException(status_code=404, detail="Session not found")
    
    current_diff = session_data[0]
    history = session_data[1]
    
    topic = "General Coding"
    level = "Fresher"

    if history and isinstance(history, list) and len(history) > 0:
        if isinstance(history[0], dict):
            topic = history[0].get("topic", "General Coding")
            level = history[0].get("level", "Fresher")

    try:
        question_text = q_engine.get_question(topic, current_diff, level, history)
        return {
            "question": question_text,
            "difficulty": current_diff,
            "topic": topic,
            "history": history
        }
    except Exception as e:
        print(f"Error: {e}")
        return {"question": f"Tell me about {topic}.", "difficulty": "Easy", "topic": topic}

@app.post("/submit_answer")
def submit_answer(req: AnswerRequest):
    evaluation = evaluator.evaluate(req.question_text, req.answer)
    score = evaluation.get("score", 0)
    feedback = evaluation.get("feedback", "")
    correct_solution = evaluation.get("correct_solution", "")
    
    session_data = get_session(req.session_id)
    if not session_data:
        raise HTTPException(status_code=404, detail="Session not found")

    current_diff = session_data[0]
    history = session_data[1]
    
    new_diff = diff_controller.adjust_difficulty(current_diff, score)
    
    history.append({
        "question": req.question_text,
        "answer": req.answer,
        "score": score,
        "feedback": feedback
    })
    
    update_session(req.session_id, new_diff, history, user_id=None)
    
    return {
        "score": score,
        "feedback": feedback,
        "next_difficulty": new_diff,
        "correct_solution": correct_solution
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)