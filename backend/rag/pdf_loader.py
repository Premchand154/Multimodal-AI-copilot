from pypdf import PdfReader

def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

if __name__ == "__main__":
    text=load_pdf(r"C:\Users\Premchand Sepeni\Downloads\2603.06576v1.pdf")
    print(text[:500])