import httpx
import anthropic 
import os
from docx import Document 
from memory import build_memory_prompt, get_answered_questions, save_answered_question  

client = anthropic.AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY")) 
CV_PATH = "data/cv.docx" 

