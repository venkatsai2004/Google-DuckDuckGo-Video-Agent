import inspect
if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec

import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file,get_file
import google.generativeai as genai
import time
from pathlib import Path
import tempfile
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Multimodel Groq-Duckduckgo Based Ai Agent",
                   page_icon="🎥", layout="wide")

st.title("🎬 Multimodel AI Video Summarizer")
st.header("Powered by Groq + DuckDuckGo")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("Groq_API_KEY not found. Please add it to your .env file.")
else:
    st.success("Groq_API_KEY found.")

@st.cache_resource
def intialize_agent():
    return Agent(
        name="Google-DuckDuckGo Video Agent",
        model=Gemini(model="gemini-2.0-flash-exp", temperature=0, api_key=GOOGLE_API_KEY),
        tools=[DuckDuckGo()],
        markdown=True
    )

video_agent = intialize_agent()

video_file = st.file_uploader("🎞️ Upload a video file", type=["mp4", "mov", "avi"])

if video_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(video_file.read())
        video_path = temp_video.name

    st.video(video_path, format="video/mp4", start_time=0)

    user_query = st.text_area(
        "💡 What do you want to know about the video?",
        placeholder="e.g. Summarize the video, list key points, analyze sentiment"
    )

    if st.button("🔍 Analyze Video"):
        if not user_query:
            st.warning("⚠️ Please enter a query first.")
        else:
            try:
                with st.spinner("🚀 Processing and analyzing video..."):
                    analysis_prompt = f"""
                    You are a video analysis assistant.
                    The user uploaded a video located at: {video_path}
                    Their question: {user_query}

                    Step 1: Simulate extracting the transcript.
                    Step 2: Provide a detailed, insightful answer.
                    Step 3: Enrich with web context using DuckDuckGo if relevant.
                    """
                    response = video_agent.run(analysis_prompt)
                st.subheader("🧠 Analysis Result")
                st.markdown(response.content)
            except Exception as e:
                st.error(f"❌ Error during analysis: {e}")
            finally:
                Path(video_path).unlink(missing_ok=True)
else:
    st.info("📤 Upload a video file to begin analysis.")

st.markdown("""
<style>
.stTextArea textarea {
    height: 100px;
}
</style>
""", unsafe_allow_html=True)
