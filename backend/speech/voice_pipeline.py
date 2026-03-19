from speech.speech_to_text import transcribe_audio
from rag.rag_pipeline import ask_ai

def voice_assistant(audio_file):
    question = transcribe_audio(audio_file)
    print("You asked:", question)
    answer = ask_ai(question)
    print("AI Answer:", answer)
    
if __name__ == "__main__":
    voice_assistant(r"F:\ML\Project\multimodal_ai_copilot\computer_vision.wav")    