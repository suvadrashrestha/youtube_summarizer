#  YouTube Transcriber and summarizer App

This Streamlit app downloads audio from a YouTube video and transcribes the speech into text using OpenAI's Whisper model and summarize it using google gemini llm.

---

##  Run with Docker

### 1. Build the Docker image

```bash
docker build -t youtube-transcriber-app .

### 2. Run the Docker Container

```bash
docker run -p 8501:8501 youtube-transcriber-app

Visit http://localhost:8501 to see your Streamlit app running inside Docker!
