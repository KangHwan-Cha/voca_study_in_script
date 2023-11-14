import fitz
path = "./Script/the Proposal 2009.pdf"
doc = fitz.open(path)
for page in doc:
    text = page.get_text()
    print(text)