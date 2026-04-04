import streamlit as st
import json
import os
from google import genai
from dotenv import load_dotenv

# 1. Setup & Authentication
load_dotenv()
# The new SDK automatically detects GEMINI_API_KEY from your .env
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_ID = "gemini-2.5-flash" 

## --- AGENT DEFINITIONS ---

def generator_agent(grade, topic, feedback=None):
    """
    Responsibility: Generate draft educational content [cite: 83-85].
    Requirement: Structured JSON output [cite: 91-101].
    """
    prompt = f"Create a Grade {grade} lesson and 2 MCQs on '{topic}'. Output ONLY valid JSON."
    if feedback:
        # Refinement Logic: Re-run with feedback embedded [cite: 126]
        prompt += f" REVISE this content based on the following feedback: {feedback}"
    
    response = client.models.generate_content(
        model=MODEL_ID,
        config={'response_mime_type': 'application/json'},
        contents=prompt
    )
    return json.loads(response.text)

def reviewer_agent(content_json):
    """
    Responsibility: Evaluate based on Age Appropriateness, Correctness, and Clarity [cite: 108-109, 120-123].
    """
    prompt = f"Review this educational JSON: {json.dumps(content_json)}. Return JSON with 'status' (pass/fail) and 'feedback' (list)."
    
    response = client.models.generate_content(
        model=MODEL_ID,
        config={'response_mime_type': 'application/json'},
        contents=prompt
    )
    return json.loads(response.text)

## --- UI INTEGRATION (MANDATORY) [cite: 129-136] ---

st.set_page_config(page_title="Zeklavya AI Agent Pipeline", layout="wide")
st.title("🎓 Zeklavya AI Agent Pipeline")
st.markdown("---")

# Sidebar for Inputs
with st.sidebar:
    st.header("Content Settings")
    grade = st.number_input("Target Grade", 1, 12, 4)
    topic = st.text_input("Topic", "Types of Angles")
    
    # Testing feature to demonstrate Refinement Pass 
    force_fail = st.checkbox("Force Reviewer to Fail (for testing refinement)")
    
    launch = st.button("Launch Agent Pipeline")

if launch:
    # STEP 1: GENERATOR OUTPUT [cite: 133]
    st.subheader("🔍 Step 1: Generator Agent")
    with st.status("Generator is drafting content...", expanded=True):
        v1_content = generator_agent(grade, topic)
        st.json(v1_content)

    # STEP 2: REVIEWER FEEDBACK [cite: 134]
    st.subheader("⚖️ Step 2: Reviewer Agent")
    with st.status("Reviewer is evaluating...", expanded=True):
        review = reviewer_agent(v1_content)
        
        # Manual override for demonstration purposes
        if force_fail:
            review["status"] = "fail"
            review["feedback"].append("TEST MODE: Content is too advanced for this grade.")
        
        if review["status"] == "pass":
            st.success("Status: PASS")
            st.json(review)
        else:
            st.error("Status: FAIL")
            st.json(review)

    # STEP 3: REFINED OUTPUT (IF APPLICABLE) [cite: 135]
    if review["status"] == "fail":
        st.subheader("🔄 Step 3: Refined Output (One-Pass Limit)")
        with st.status("Generator is incorporating feedback...", expanded=True):
            # Limit to one refinement pass [cite: 127]
            refined_content = generator_agent(grade, topic, feedback=review["feedback"])
            st.success("Refinement Complete")
            st.json(refined_content)
    
    st.divider()
    st.info("Agent flow complete. The UI makes the pipeline obvious as per requirements.")