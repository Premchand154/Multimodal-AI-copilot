from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

def detect_objects(image_path):
    results= model(image_path)
    detected_objects = []
    
    for result in results:
        boxes=result.boxes
        for box in boxes:
            class_id = int(box.cls[0])
            label = model.names[class_id]
            detected_objects.append(label)
    return list(set(detected_objects))


        
if __name__ == "__main__":
    image_path = r"C:\Users\Premchand Sepeni\Downloads\download.jpg"
    objects = detect_objects(image_path)
    print("Detected objects:", objects)
    detect_and_visualize(image_path)
            