from google import genai
from pypdf import PdfReader
from dotenv import load_dotenv
load_dotenv()

client = genai.Client()

response = client.interactions.create(
    model="gemini-3.8-flash",
    input=("Hi (reply in one word)")
)

print(response.output_text)
