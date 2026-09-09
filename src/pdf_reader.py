from pypdf import PdfReader
import fontTools

def extract_text(path):

    #EXTRACTING THE TEXT
    file = PdfReader(path)
    content = []

    for page in file.pages:
        content.append(page.extract_text())
    

    return "\n".join(content)
