from google import genai #The AI
from dotenv import load_dotenv #For the API key

from prompt import NOTES_PROMPT #The prompt
from pdf_reader import extract_text #The pdf text extract
from save_notes import save_notes #saves the notes to a new .md file

import argparse #To get the PDF path

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--pdf", help="path to the chapter PDF", required=True)
args = parser.parse_args()

path = args.pdf

text = (extract_text(path))

def generate_notes(text):
    client = genai.Client()

    response = client.interactions.create(
        model="gemini-3.6-flash",
        input=(NOTES_PROMPT.format(chapter_text=text))
    )

    return response.output_text

notes = generate_notes(text)

save_notes(path,notes)

