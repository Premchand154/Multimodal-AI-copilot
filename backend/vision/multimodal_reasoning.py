from vision.image_caption import caption_image
from vision.object_detection import detect_objects
from llm.llm_inference import generate_response

def analyze_image(image_path, question):

    # Step 1: Generate caption
    caption = caption_image(image_path)

    # Step 2: Detect objects
    objects = detect_objects(image_path)

    # Step 3: Build multimodal context
    context = f"""
    Image caption: {caption}

    Objects detected in the image: {', '.join(objects)}
    """

    # Step 4: Ask LLM to reason
    answer = generate_response(context, question)

    return {
        "caption": caption,
        "objects": objects,
        "answer": answer
    }
    
if __name__ == "__main__":
    image = r"C:\Users\Premchand Sepeni\Downloads\download.jpg"
    question = "What is the person likely doing?"
    result = analyze_image(image, question)
    
    print("Caption:", result["caption"])
    print("Objects:", result["objects"])
    print("Answer:", result["answer"])   