from pathlib import Path

def save_material(path, material, type):

    pdf_name = Path(path).stem

    if type == "notes":
        output_name = f"{pdf_name}_notes.md"

    elif type == "quiz":
        output_name = f"{pdf_name}_quiz.md"

    elif type == "flashcards":
        output_name = f"{pdf_name}_flashcards.md"

    with open(f"output/{output_name}", "w") as file:
        file.write(material)

    print(f"Notes saved at output/{output_name}")
