# 📄 Automated SDLC Document Generator using Agentic AI 

A fully automated multi-agent system that generates, reviews, and formats all key SDLC (Software Development Life Cycle) documents — from Requirements to User Stories, PDD, SDD, Test Cases, and more — using CrewAI, real-time voice input, a SadTalker-powered interactive avatar, and a score-driven feedback loop. Final documents are auto-pushed to GitHub for seamless access and team collaboration.

---

## 🚀 Key Features

✅ Multi-Agent Orchestration  
- Uses CrewAI to coordinate specialized agents for understanding requirements, drafting, reviewing, generating test cases, and final evaluation.
- Supports comprehensive SDLC deliverables: Requirements, User Stories, PDD, SDD, Test Cases, Flowcharts, Risk Analysis.

✅ Voice-Based Input  
- Integrated NVIDIA Parakeet for real-time speech-to-text transcription of problem statements or requirements.

✅ Interactive Avatar  
- Powered by the SadTalker model to generate a realistic talking avatar that greets and guides users at the start of a session.
- Provides live updates and feedback as each document is created, reviewed, evaluated, and finalized.

✅ Score-Driven Feedback Loop  
- Each document is evaluated and improved iteratively until it reaches a defined quality score threshold.
- Final evaluation checks consistency and completeness before approval.

✅ Automatic GitHub Sync  
- Final approved documents are automatically pushed to your GitHub repo for developer access and collaboration.

✅ Fully Automated Workflow  
- Runs end-to-end: from user voice input → multi-agent understanding → multi-stage generation → final formatting → GitHub push.

---

## 🧩 Tech Stack

- Python — core programming
- CrewAI — multi-agent orchestration
- NVIDIA Parakeet — real-time voice-to-text
- SadTalker — realistic talking avatar
- LLM (Google Gemini / OpenAI) — document drafting, review, and evaluation
- LangChain — LLM orchestration
- GitHub API — auto-push final files
- Streamlit (optional) — interactive UI
- FFmpeg — audio/video processing

---

## ⚙️ How It Works

1️⃣ Voice Capture  
- Speak your problem or requirement → Parakeet transcribes it in real-time.

2️⃣ Flowchart Approval  
- System generates an initial flowchart → asks for your approval → loops for revision if rejected.

3️⃣ Agentic Document Generation  
- CrewAI runs a chain of agents that:
  - Understand and break down requirements
  - Draft Requirements, User Stories, PDD, SDD
  - Generate visuals and flowcharts
  - Produce related test cases automatically
  - Review for factual accuracy and tone
  - Evaluate with scoring → re-run improvements if score is low
  - Final evaluation for consistency & completeness

4️⃣ Interactive UX  
- SadTalker avatar greets and guides you.
- Provides live updates for each document as it’s generated, reviewed, scored, and finalized.

5️⃣ Auto GitHub Push  
- Final documents auto-commit and push to your configured GitHub repository.

---

## 📂 Project Structure

plaintext
.
├── agents.py             # Defines CrewAI agents
├── tasks.py              # Defines agent tasks
├── crew.py               # Orchestrates the multi-agent workflow
├── live_audio_to_text.py # Handles voice input (Parakeet)
├── avatar_intro.py       # Manages SadTalker greeting & updates
├── outputs/              # Generated docs
├── main.py               # Run the system
├── requirements.txt      # Python dependencies
└── .env                  # API keys

---

## 🏃‍♂️ How To Run

plaintext
1️⃣ Clone the Repo
git clone https://github.com/YOUR_USERNAME/Automated-SDLC-Document-Generator-Agentic-AI.git
cd Automated-SDLC-Document-Generator-Agentic-AI

2️⃣ Create Virtual Environment
python -m venv venv
# Activate:
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add API Keys
Create a `.env` file:
GOOGLE_API_KEY=YOUR_API_KEY
GITHUB_TOKEN=YOUR_GITHUB_TOKEN

5️⃣ Run the App
python main.py

Speak your input → approve flowchart → agents generate documents → get live updates → outputs appear in `/outputs` → final files auto-pushed to GitHub!

---

## 📌 Example Documents Generated

✅ Requirements Document  
✅ User Story  
✅ PDD (Project Design Document)  
✅ SDD (Software Design Document)  
✅ Test Cases  
✅ Flowcharts & Risk Analysis 
✅ Word doc & auto-upload

---

## 🗂️ Future Improvements

- Multi-language voice input
- More realistic avatars & gestures
- JIRA/Trello integration for auto-ticket creation
- Custom templates & styling
