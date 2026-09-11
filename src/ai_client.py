from google import genai #The AI
from dotenv import load_dotenv #For the API key


load_dotenv()

def generate_material(text, prompt):
    client = genai.Client()

    response = client.interactions.create(
        model="gemini-3.6-flash",
        input=(prompt.format(chapter_text=text))
    )

    return response.output_text