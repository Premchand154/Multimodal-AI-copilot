import whisper

model= whisper.load_model("base")
def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]

if __name__ == "__main__":
    audio_file = r"F:\ML\Project\multimodal_ai_copilot\computer_vision.wav"
    text = transcribe_audio(audio_file)
    print("Transcription:", text)
    