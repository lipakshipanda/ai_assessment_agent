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
   ```bash
   pip install -r requirements.txt