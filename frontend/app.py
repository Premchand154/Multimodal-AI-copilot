import streamlit as st
import requests

st.title("Multimodal AI Copilot")
st.write("Ask questions, upload images or audio to interact with the Multimodal AI Copilot.")

api_url = "http://127.0.0.1:8000"


# ---------------------------
# TEXT QUESTION
# ---------------------------
st.header("Ask a Question")

question = st.text_input("Enter question:",key="text_q")

if st.button("Ask"):
    response = requests.post(
        f"{api_url}/ask",
        json={"question": question}
    )

    result = response.json()
    st.write(result["answer"])

# ---------------------------
# PDF Analysis
# ---------------------------
st.header("PDF Analysis")

pdf_file = st.file_uploader("Upload PDF", type=["pdf"], key="pdf_uploader")

if "pdf_uploaded" not in st.session_state:
    st.session_state.pdf_uploaded = False

if pdf_file is not None and not st.session_state.pdf_uploaded:
    files = {"file": pdf_file}

    response = requests.post(
        f"{api_url}/upload_pdf",
        files=files
    )

    if response.status_code == 200:
        st.success("PDF uploaded successfully!")
        st.session_state.pdf_uploaded = True

if st.session_state.pdf_uploaded:
    pdf_question = st.text_input("Ask question about PDF", key="pdf_question")

    if st.button("Ask PDF"):

        response = requests.post(
            f"{api_url}/ask_pdf",
            json={"question": pdf_question}
        )

        st.write(response.json()["answer"])


# ---------------------------
# IMAGE ANALYSIS
# ---------------------------
st.header("Analyze Image")

image_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"],
    key="image_upload"
)

image_question = st.text_input("Ask question about image", key="image_question")

if image_file is not None:
    
    st.image(image_file, caption="Uploaded Image")

    files = {"file": image_file}

    response = requests.post(
        f"{api_url}/multimodal_reason",
        files=files,
        params={"question": image_question}
    )

    result = response.json()

    st.subheader("Analysis")
    st.write("Caption:", result["caption"])
    st.write("Objects:", result["objects"])

    if image_question:
        st.subheader("AI Reasoning")
        st.write(result["answer"])


# ---------------------------
# AUDIO QUERY
# ---------------------------
st.header("Voice Query")

audio_file = st.file_uploader(
    "Upload an audio file",
    type=["wav", "mp3", "mp4"],
    key="audio_upload"
)

if audio_file is not None:

    st.audio(audio_file)

    response = requests.post(
        f"{api_url}/audio",
        files={"file": (audio_file.name, audio_file, audio_file.type)}
    )

    result = response.json()

    st.write("Transcription:", result["transcription"])
    st.write("Answer:", result["answer"])