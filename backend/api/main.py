import os
import uuid
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from rag.rag_pipeline import ask_ai
from rag.vector_store import vector_store
from vision.image_caption import caption_image
from vision.object_detection import detect_objects
from vision.multimodal_reasoning import analyze_image
from speech.speech_to_text import transcribe_audio
from rag.pdf_chat import load_pdf_knowledge, ask_pdf

app = FastAPI(title="Multimodal AI Copilot")


@app.get("/")
def home():
    return {"message": "Multimodal AI Copilot API Running"}


# ---------------- TEXT ----------------
class Question(BaseModel):
    question: str


@app.post("/ask")
def ask_question(q: Question):
    try:
        answer = ask_ai(q.question)
        return {"question": q.question, "answer": answer}
    except Exception as e:
        return {"error": str(e)}


# ---------------- PDF ----------------
@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    os.makedirs("data", exist_ok=True)
    path = f"data/{file.filename}"

    with open(path, "wb") as f:
        f.write(await file.read())

    load_pdf_knowledge(path)

    return {"message": "PDF processed successfully"}


class PDFQuestion(BaseModel):
    question: str


@app.post("/ask_pdf")
def ask_pdf_question(q: PDFQuestion):
    answer = ask_pdf(q.question)
    return {"answer": answer}


# ---------------- IMAGE REASONING ----------------
@app.post("/multimodal_reason")
async def multimodal_reason(file: UploadFile = File(...), question: str = ""):

    os.makedirs("data", exist_ok=True)
    path = f"data/{file.filename}"

    with open(path, "wb") as f:
        f.write(await file.read())

    result = analyze_image(path, question)

    return result


# ---------------- STREAM (OPTIONAL SIMPLE FIX) ----------------
@app.post("/stream")
async def stream_ai(q: Question):

    def generator():
        answer = ask_ai(q.question)
        yield answer

    return StreamingResponse(generator(), media_type="text/plain")


# ---------------- IMAGE ----------------
@app.post("/image")
async def process_image(file: UploadFile = File(...)):

    if not file.content_type.startswith("image"):
        return {"error": "Invalid image file"}

    os.makedirs("temp", exist_ok=True)

    filename = f"{uuid.uuid4()}_{file.filename}"
    path = f"temp/{filename}"

    content = await file.read()

    with open(path, "wb") as f:
        f.write(content)

    caption = caption_image(path)
    objects = detect_objects(path)

    os.remove(path)

    return {
        "caption": caption,
        "objects": objects
    }


# ---------------- AUDIO ----------------
@app.post("/audio")
async def process_audio(file: UploadFile = File(...)):

    if not file.content_type.startswith("audio"):
        return {"error": "Invalid audio file"}

    os.makedirs("temp", exist_ok=True)

    filename = f"{uuid.uuid4()}_{file.filename}"
    path = f"temp/{filename}"

    content = await file.read()

    with open(path, "wb") as f:
        f.write(content)

    text = transcribe_audio(path)
    answer = ask_ai(text)

    os.remove(path)

    return {
        "transcription": text,
        "answer": answer
    }