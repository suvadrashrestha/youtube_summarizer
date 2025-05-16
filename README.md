# YouTube Transcriber and Summarizer App

This Streamlit app downloads audio from a YouTube video, transcribes the speech into text using OpenAI's Whisper model, and summarizes it using Google Gemini LLM.

---

## Run with Docker

Build and run the Docker container with the following commands:

```bash
# Build the Docker image
docker build -t youtube-transcriber-app .

# Run the Docker container
docker run -p 8501:8501 youtube-transcriber-app
Visit http://localhost:8501 to see your Streamlit app running inside Docker!
