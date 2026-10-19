import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture(0)

while cv2.waitKey(1) != ord('x'):
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)
    
    person_count = 0

    for box in results[0].boxes:
        class_id = int(box.cls[0])

        if class_id == 0:
            person_count += 1

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, 'Szemely', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.putText(frame, f'Szemelyek szama: {person_count}', (10, 40), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Videofolyam', frame)

cap.release()
cv2.destroyAllWindows()
