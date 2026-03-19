from rag.pdf_loader import load_pdf
from rag.text_splitter import split_text
from rag.rag_pipeline import ingest_text, ask_ai
from rag.vector_store import vector_store

def load_pdf_knowledge(file_path):

    text = load_pdf(file_path)
    ingest_text(text)
    

def ask_pdf(question):
    return ask_ai(question)


if __name__ == "__main__":
    load_pdf_knowledge(r"C:\Users\Premchand Sepeni\Downloads\2603.06576v1.pdf")

    question = "What is the main contribution of the paper?"

    answer = ask_pdf(question)

    print("Question:", question)
    print("Answer:", answer)