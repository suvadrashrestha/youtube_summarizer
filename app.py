import streamlit as st
import yt_dlp
import whisper

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

st.title("YouTube Video to Text Transcription")

url = st.text_input("Enter YouTube Video URL")

if st.button("Convert and Transcribe"):
    if url:
        with st.spinner("Downloading and transcribing..."):
            audio_file = download_youtube_audio(url)
            text = transcribe_audio(audio_file)
            st.text_area("Transcription", text, height=300)
    else:
        st.warning("Please enter a valid YouTube URL")
