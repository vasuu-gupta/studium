from google import genai
from pypdf import PdfReader

# Key is zhrcs
client = genai.Client()

response = client.interactions.create(
    model="gemini-3.8-flash",
    input=input("ENTER: "),
)

print(response.output_text)
