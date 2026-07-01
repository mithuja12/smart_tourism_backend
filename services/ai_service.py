import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def get_ai_recommendation(destination, crowd_level, weather):

    prompt = f"""
You are a smart tourism assistant.

Destination: {destination}

Crowd Level: {crowd_level}

Weather: {weather}

Give:
1. Best visiting time
2. One travel tip
3. One alternate nearby attraction

Return only plain text.
"""

    response = model.generate_content(prompt)

    return response.text