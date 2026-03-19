from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image, UnidentifiedImageError

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-vqa-base",)
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-vqa-base",)

def ask_question(image_path, question):
    image=Image.open(image_path).convert("RGB")
    inputs = processor(image, question, return_tensors="pt")
    output = model.generate(**inputs)
    answer = processor.decode(output[0], skip_special_tokens=True)
    return answer

if __name__ == "__main__":
    image_path = r"C:\Users\Premchand Sepeni\Downloads\download.jpg"
    question = "What is in the image?"
    answer = ask_question(image_path, question)
    print("Answer:", answer)
    
    