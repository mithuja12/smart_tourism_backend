import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def get_ai_recommendation(destination, crowd_level, weather):

    prompt = f"""
You are an expert AI tourism guide for Kodaikanal, Tamil Nadu, India.

Tourist Destination:
{destination}

Current Crowd Level:
{crowd_level}

Current Weather:
{weather}

Based on the above information, provide:

1. Best time to visit this destination today.
2. A short travel tip (1-2 sentences).
3. One nearby tourist attraction in Kodaikanal that is a good alternative if this place is crowded.
4. A parking suggestion if applicable.
5. A safety or weather recommendation if necessary.

Keep the response concise, practical and tourist-friendly.

Return only plain text without markdown or numbering symbols.
"""

    response = model.generate_content(prompt)

    return response.text