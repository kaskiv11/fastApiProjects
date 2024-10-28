import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open camera or video file")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = 20.0

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('myvideo.mp4', fourcc, fps, (frame_width, frame_height))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    out.write(frame)

    cv2.imshow('Camera frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()