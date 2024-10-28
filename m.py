import cv2

cap = cv2.VideoCapture("myvideo.mp4")

if not cap.isOpened():
    print("Could not open camera or video file")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow('Camera frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()