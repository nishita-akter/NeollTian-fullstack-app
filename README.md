# 🤖 NeoIITian – AI Software Engineer Chatbot

![NeoIITian Banner](neo_iitian/assets/logo.png)
_Your Personal AI Software Engineer Assistant_

---

## 🚀 About NeoIITian

**NeoIITian** is a **smart, professional chatbot** designed to think and respond like a **top-tier Software Engineer**.
It can answer **any Computer Science question** — from **programming, AI, ML, OS, DBMS, networks, to algorithms** — in a **structured, motivating, and clear way**.

Built with **[LangChain](https://www.langchain.com/)** + **[Groq LLM API](https://www.groq.com/)**
Developed with **Python FastAPI backend** and **React frontend** for modern web experience.

---

## 🧩 Features

- 💡 **Professional AI Software Engineer personality**
- 🧠 **Persistent chat memory**
- 💾 **Frontend React interface with elegant chat UI**
- ⚡ **Fast, modular, and beginner-friendly codebase**
- 🔗 **Supports Groq LLM API**
- 🧰 **Simple file structure for easy customization**

---

## 📁 Project Structure

```
NeoIITian/
├── backend/
│   ├── main.py            # FastAPI app
│   ├── neo_iitian/
│   │   ├── chatbot.py     # Core chat logic (LLM response generator)
│   │   ├── llm_connector.py   # Groq connector
│   │   ├── prompt_templates.py# Chatbot persona prompt
│   │   ├── utils.py       # Helper functions
│   │   ├── config.py      # Environment variables
│   │   └── assets/logo.png
│   ├── requirements.txt   # Python dependencies
│   └── .env.example       # Example env variables
├── frontend/
│   ├── package.json       # React project dependencies
│   ├── public/
│   └── src/
├── data/
│   └── sample_context.txt # Optional contextual knowledge
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Project

```bash
git clone https://github.com/yourusername/NeoIITian.git
cd NeoIITian
```

---

### 2️⃣ Backend Setup (FastAPI + LLM)

#### a) Create Conda Environment

```bash
conda create -n neo-backend python=3.10 -y
conda activate neo-backend
```

#### b) Install Python Dependencies

```bash
cd backend
pip install -r requirements.txt
```

> ⚠️ If you get pip launcher errors, ensure your conda environment is active and Python is from conda.

#### c) Setup Environment Variables

Copy `.env.example` to `.env` and update:

```
GROQ_API_KEY=your_groq_api_key_here
LLM_PROVIDER=groq
```

---

### 3️⃣ Frontend Setup (React)

```bash
cd ../frontend
npm install
```

---

## 💬 Running NeoIITian Locally

### Backend (FastAPI)

```bash
cd backend
conda activate neo-backend
uvicorn main:app --reload --port 8000
```

- Runs FastAPI server at [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Provides `/chat` endpoint for frontend requests

### Frontend (React)

```bash
cd frontend
npm start
```

- Runs React app at [http://localhost:3000](http://localhost:3000)
- Connects automatically to FastAPI backend

---

## 🧠 Testing Backend Integration

1. Ask a question in the React frontend.
2. If you get a meaningful response (e.g., “tell me about CSE”), it confirms **frontend ↔ FastAPI ↔ Groq LLM** is working.
3. Responses are generated dynamically by your LLM backend.

---

## 💡 Example Questions

```
- Explain process scheduling algorithms in OS.
- Difference between deep learning and ML?
- How does a database transaction work?
- What is Big O notation?
- How to debug Python code efficiently?
```

---

## 🛠️ Tech Stack

| Layer       | Technology                      |
| ----------- | ------------------------------- |
| LLM Backend | Groq API                        |
| Framework   | LangChain + FastAPI             |
| Frontend    | React                           |
| Language    | Python 3.10 + JavaScript        |
| Optional    | FAISS / Chroma (context memory) |

---

## 👨‍💻 Developer

**Tawfica Bhuiyan** – AI/ML & LLM Enthusiast | Software Engineer in Progress
📧 [bhuiyantawfica@gmail.com](mailto:bhuiyantawfica@gmail.com)
🌐 [GitHub](https://github.com/TawficaBhuiyan)

---

## ⭐ Support

If you find this project useful, **⭐ Star it on GitHub** and share with your friends 🚀
