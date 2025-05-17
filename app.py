import streamlit as st
import yt_dlp
import whisper
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()


def download_youtube_audio(url, output_path='audio'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return output_path + '.mp3'

def transcribe_audio(audio_file):
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    return result['text']

def summarize_transcript(transcript):
    prompt="""You are a helpful assistant that summarizes YouTube videos based on their transcripts.
    When given a full transcript, identify the key topics, important explanations, and the overall conclusion of the video.
    Your summary should:
    - Be clear and concise.
    - Highlight the most important ideas.
    - Remove filler and irrelevant speech.
    If the transcript is long, group ideas logically and prioritize relevance.
    If the transcript is missing or empty, inform the user that you cannot summarize it.
    """
    llm= ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    template= ChatPromptTemplate.from_messages([
        ("system", prompt),
        ("human", "{text}")
    ])
    chain= template | llm
    res=chain.invoke({
    "text":transcript
    })
    return res.content

st.title("YouTube Video to Text Transcription")

url = st.text_input("Enter YouTube Video URL")

if st.button("summarize"):
    if url:
        with st.spinner("summarizing..."):
            audio_file = download_youtube_audio(url)
            text = transcribe_audio(audio_file)
            st.text_area("Transcription", text, height=200)
            summarized_content= summarize_transcript(text)
            st.text_area("Summarization", summarized_content)
    else:
        st.warning("Please enter a valid YouTube URL")
