# Zeklavya AI: Agent-Based Content Creator

An automated educational content pipeline built for the Zeklavya AI Developer Assessment. This application leverages multi-agent collaboration to generate, review, and refine lesson plans and assessments.

## 🤖 Agent Architecture
- [cite_start]**Generator Agent**: Responsible for drafting lesson explanations and MCQs tailored to specific grade levels (1-12) and topics. [cite: 83-85]
- [cite_start]**Reviewer Agent**: Evaluates the draft for age-appropriateness, conceptual correctness, and clarity. [cite: 108, 120-123]
- [cite_start]**Refinement Logic**: Implements a lightweight loop that re-runs the Generator once if the Reviewer provides a "fail" status. [cite: 124-128]

## 🛠️ Tech Stack
- **LLM**: Gemini 2.5 Flash (via Google GenAI SDK)
- [cite_start]**UI**: Streamlit 
- **Language**: Python 3.11+

## 🚀 Setup Instructions
1. Clone the repository.
2. Install dependencies:
   pip install -r requirements.txt
3. Create a .env file in the root directory and add your API key:
   GEMINI_API_KEY=your_api_key_here
4. Run the application:
   streamlit run app.py
## 📋 FeaturesStructured JSON Communication:
    All agents communicate using deterministic JSON schemas.
    Dynamic UI: Real-time display of the agent pipeline, making the "thought process" and feedback loop visible.
   
