# YouTube Video Summarizer and Notes Converter Using AI

This project is a Streamlit-based web application that summarizes YouTube video transcripts using Google’s Gemini AI model. The app extracts transcripts from a provided YouTube video URL, summarizes the content, and presents it in bullet points.

## Features

- Extracts transcript text from a YouTube video using the YouTube Transcript API.
- Summarizes the video transcript into bullet points using Google’s Gemini AI.
- Provides a clean and user-friendly interface with Streamlit.

## Technologies Used

- **Streamlit**: For building the web application.
- **Google Generative AI**: For generating summaries.
- **YouTube Transcript API**: For fetching video transcripts.
- **Python-dotenv**: For managing environment variables.


## Deployment

The application is deployed and accessible at [summerize-ai.streamlit](https://summerize-ai.streamlit.app/)

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt

4. **Set Up Environment Variables**
    Create a .env file in the root directory and add your Google API key:

   ```bash
   Google_Api_Key=your_google_api_key_here

5. **Run the Streamlit Application**

   ```bash
   streamlit run app.py
