from pathlib import Path

def save_notes(path, text):

    pdf_name = Path(path).stem
    output_name = f"{pdf_name}_notes.md"

    with open(f"output/{output_name}", "w") as file:
        file.write(text)

    print(f"Notes saved at output/{output_name}")