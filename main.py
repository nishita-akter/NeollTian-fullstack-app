# # backend/main.py
# from fastapi import FastAPI
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware
# from chatbot.get_response import get_response

# # Initialize FastAPI app
# app = FastAPI(title="NeoIITian Backend")

# # Enable CORS for local frontend development
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # ⚠️ replace with your frontend URL in production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Request model
# class ChatRequest(BaseModel):
#     user_input: str

# # Root endpoint (for testing)
# @app.get("/")
# def root():
#     return {"message": "🚀 NeoIITian backend is running successfully!"}

# # Chat endpoint (connects frontend to LLM)
# @app.post("/chat")
# async def chat(req: ChatRequest):
#     """
#     Receives user message and returns LLM response.xcv   
#     """
#     response = get_response(req.user_input)
#     return {"response": response}
# D:\Tawfica&LLM\NeoIITian\backend\main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from neo_iitian.chatbot import get_response

# ===== FastAPI app =====
app = FastAPI(title="NeoIITian Backend API")

# ===== Allow React frontend (CORS) =====
origins = [
    "http://localhost:3000",  # React dev server
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== Request body schema =====
class ChatRequest(BaseModel):
    user_input: str

# ===== Chat endpoint =====
@app.post("/chat")
async def chat_endpoint(payload: ChatRequest):
    user_input = payload.user_input
    response = get_response(user_input)
    return {"response": response}

# ===== Optional: simple health check =====
@app.get("/")
async def root():
    return {"status": "NeoIITian API is running"}
