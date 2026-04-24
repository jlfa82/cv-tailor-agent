import json 
import os
from datetime import datetime 

MEMORY_FILE = "data/memory.json" 

def _load() -> dict: 
    if not os.path.exists(MEMORY_FILE): 
        return {
            "preferences":[], 
            "answered_questions":{}, 
            "feedback_history": []
        } 
    
    with open(MEMORY_FILE, "r") as f: 
        return json.load(f) 

def _save(data: dict) -> None: 
    with open(MEMORY_FILE, "w") as f: 
        json.dump(data, f, indent=2) 

def get_preferences() -> list: 
    return _load()["preferences"] 

def add_feedback(job_title: str, rating: str, notes: str) -> None: 
    data = load() 
    data["feedback_history"].append({
        "job_title": job_title, 
        "rating": rating, 
        "notes": notes, 
        "timestamp": datetime.now().isoformat() 
    })
    if notes: 
        data["preferences"].append(notes) 
    _save(data) 

def get_answered_questions() -> dict: 
    return _load()["answered_questions"] 

def save_answered_question(question: str, answer: str) -> None: 
    data = _load() 
    data["answered_questions"][question] = answer 
    _save(data) 

def build_memory_prompt() -> str: 
    data = _load() 

    preferences = data["preferences"] 
    answered = data["answered_questions"] 

    if not preferences and not answered: 
        return "" 
    
    prompt ="MEMORY FROM PREVIOUS SESSIONS :\n" 

    if preferences: 
        pompt += "\nUser preferences and feedback:\n" 
        for p in preferences[-10:]: 
            prompt += f"- {p}\n" 
    
    if answered: 
        prompt += "\nQuestions already answered about the user:\n" 
        for q, a in answered.items(): 
            prompt += f"Q: {q}\nA: {a}\n" 
    
    return prompt 