from openai import OpenAI
from dotenv import load_dotenv
import os

# Load the environment variable from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
base_url = "https://generativelanguage.googleapis.com/v1beta/openai"

# Initialize the Gemini client
client = OpenAI(base_url=base_url, api_key=api_key)

# System prompt that defines the assistant's behavior
ai_prompt = (
    "You are a musical vibe assistant. "
    "When users describe their emotions, moods, or scenes, "
    "you suggest a short playlist of 5 songs that match the vibe. "
    "Be creative, keep it short, and give only song names or moods — no long text or explanations."
)

# The chatbot function
def ai_chatbot(usermessage, history):
    messages = [{"role": "system", "content": ai_prompt}]
    messages.extend(history)
    messages.append({"role": "user", "content": usermessage})
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=messages
    )
    return response.choices[0].message.content

# For local testing
if __name__ == "__main__":
    print(ai_chatbot("I’m feeling energetic like I want to dance all night", []))
