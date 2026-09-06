from pypdf import PdfReader

def extract_text(path):

    file = PdfReader(path)
    content = []

    for page in file.pages:
        content.append(page.extract_text())

    return "\n".join(content)

text = extract_text('/Users/vasugupta/IX/SST book/iest101.pdf')
print(text[:500])
