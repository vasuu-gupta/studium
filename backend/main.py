from ai_client import generate_material
from pdf_reader import extract_text #The pdf text extract
from save_output import save_material #saves the notes to a new .md file
from prompt import NOTES_PROMPT, QUIZ_PROMPT, FLASHCARD_PROMPT #prompts

import argparse #To get the PDF path

parser = argparse.ArgumentParser()
parser.add_argument("--pdf", help="path to the chapter PDF", required=True)
parser.add_argument("--type", help="type of content generated", required=True)
args = parser.parse_args()

path = args.pdf
type = args.type
text = (extract_text(path))

if type == "notes":
    notes = generate_material(text, NOTES_PROMPT)
    save_material(path,notes, "notes")

elif type == "quiz":
    quiz = generate_material(text, QUIZ_PROMPT)
    save_material(path, quiz, "quiz")

elif type == "flashcards":
    flashcards = generate_material(text, FLASHCARD_PROMPT)
    save_material(path, flashcards, "flashcards")
