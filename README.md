# 📄 Automated SDLC Document Generator using Agentic AI

A fully automated multi-agent system that generates, reviews, and formats all key SDLC (Software Development Life Cycle) documents — from Requirements to User Stories, PDD, SDD, Test Cases, and more — using **CrewAI**, real-time **voice input**, a **SadTalker-powered interactive avatar**, and a **score-driven feedback loop**. Final documents are auto-pushed to GitHub for seamless access and team collaboration.

---

## 🚀 Key Features

✅ **Multi-Agent Orchestration**  
- Uses **CrewAI** to coordinate specialized agents for understanding requirements, drafting, reviewing, generating test cases, and final evaluation.
- Supports comprehensive SDLC deliverables: Requirements, User Stories, PDD, SDD, Test Cases, Flowcharts, Risk Analysis.

✅ **Voice-Based Input**  
- Integrated **NVIDIA Parakeet** for real-time speech-to-text transcription of problem statements or requirements.

✅ **Interactive Avatar**  
- Powered by the **SadTalker** model to generate a realistic talking avatar that greets and guides users at the start of a session.
- Provides live updates and feedback as each document is created, reviewed, evaluated, and finalized.

✅ **Score-Driven Feedback Loop**  
- Each document is evaluated and improved iteratively until it reaches a defined quality score threshold.
- Final evaluation checks consistency and completeness before approval.

✅ **Automatic GitHub Sync**  
- Final approved documents are automatically pushed to your GitHub repo for developer access and collaboration.

✅ **Fully Automated Workflow**  
- Runs end-to-end: from user voice input → multi-agent understanding → multi-stage generation → final formatting → GitHub push.

---

## 🧩 Tech Stack

| Tool/Tech | Purpose |
|-----------|---------|
| **Python** | Core programming language |
| **CrewAI** | Agentic framework to coordinate multiple specialized agents |
| **NVIDIA Parakeet** | Real-time voice-to-text transcription |
| **SadTalker** | AI-powered talking head avatar |
| **LLM (Google Gemini or OpenAI)** | For drafting, rewriting, and evaluations |
| **GitHub API** | Auto-push final documents |
| **Streamlit** | For the interactive user interface |
| **FFmpeg** | For audio/video processing if needed |

---

## ⚙️ How It Works

1️⃣ **Voice Capture:**  
- User speaks their problem or requirement — the **NVIDIA Parakeet** model transcribes it in real-time.

2️⃣ **Flowchart Approval:**  
- The system generates a proposed flowchart for the SDLC process and asks for user approval.
- If rejected, it loops back for revisions based on user feedback.

3️⃣ **Agentic Document Generation:**  
- CrewAI runs a chain of intelligent agents that:
  - Understand and break down user requirements
  - Draft documents (Requirements, User Story, PDD, SDD)
  - Create flowcharts & visuals
  - Generate related test cases automatically
  - Review each document for factual accuracy and clarity
  - Evaluate with a scoring agent
  - Re-run improvements if the score is below threshold
  - Perform a final evaluation for consistency and completeness

4️⃣ **Interactive UX:**  
- The **SadTalker** avatar greets and guides the user throughout the session.
- Provides real-time status updates for each document phase.

5️⃣ **GitHub Push:**  
- Once approved, final documents are auto-committed and pushed to your designated GitHub repository.

---

## 📂 Project Structure

```plaintext
.
├── agents.py             # Defines all CrewAI agents
├── tasks.py              # Defines tasks for each agent
├── crew.py               # Orchestrates the agent workflow
├── live_audio_to_text.py # Handles Parakeet voice input
├── avatar_intro.py       # Manages SadTalker avatar greeting & updates
├── outputs/              # Generated documents
├── main.py               # Entry point to run the system
├── requirements.txt      # Python dependencies
└── .env                  # API keys and configs
