import streamlit as st
import os

from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("Google_Api_Key"))

promt = "you will be taking transcript text and you will be summerizing entire video and summerize entire video in bullet points within 400 words. Transcript is appended here : "

def generate_gemini_content(transcript_text, promt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(promt + transcript_text)
    return response.text

def extractTranscript(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_txt = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""

        for i in transcript_txt:
            transcript += " " + i["text"]

        return transcript
    
    except Exception as e:
        if len(youtube_video_url)==0:
            st.write("Please Enter a valid youtube link")
        else:
            st.write("summery for this video is not available")

#just bunch of streamlit page config
st.set_page_config(page_title="AI Video Summerizer")

st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

st.title("Youtube Video Summerizer and Notes Converter Using AI")
youtube_link = st.text_input("Enter Youtube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width = True)

if st.button("Get Detailed Notes"):
    with st.spinner("Please wait your summery/notes are being generated"):
        transcript_text = extractTranscript(youtube_link)

        if transcript_text:
            summery = generate_gemini_content(transcript_text, promt)
            st.markdown("## Detailed Summery:")
            st.write(summery)
        else:
            summery = "summery not available at this time"
