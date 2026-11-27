
import cv2

def reverse_slow_motion():
    cap = cv2.VideoCapture("video.mp4")

    if not cap.isOpened():
        print("Video not found!")
        return

    frames = []

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    print("Total frames:", len(frames))

    for frame in reversed(frames):
        small_frame = cv2.resize(
            frame, (400, 300)
        )

        cv2.imshow("Reverse Slow Motion", small_frame)

        # 100 milliseconds delay
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

reverse_slow_motion()
