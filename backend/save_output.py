from pathlib import Path

def save_material(path, material, type):

    pdf_name = Path(path).stem
    output_name = f"{pdf_name}_{type}.md"

    with open(f"output/{output_name}", "w") as file:
        file.write(material)

    print(f"{type} saved at output/{output_name}")
