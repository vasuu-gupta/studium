from google import genai #The AI
from dotenv import load_dotenv #For the API key
from prompt import NOTES_PROMPT #The prompt
from pdf_reader import extract_text #The pdf text extract
import argparse

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--pdf", help="path to the chapter PDF", required=True)
args = parser.parse_args()

path = args.pdf
text = (extract_text(path))

client = genai.Client()

response = client.interactions.create(
    model="gemini-3.8-flash",
    input=(NOTES_PROMPT.format(chapter_text=text))
)

print(response.output_text)