
import cv2
import pytesseract

# Set the Tesseract OCR executable path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def extract_text_from_video():

    # Open video file
    cap = cv2.VideoCapture("video.mp4")

    if not cap.isOpened():
        print("Video not found!")
        return

    frame_count = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1

        # Extract text from every 10th frame
        if frame_count % 10 == 0:

            # Convert frame to grayscale
            gray = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2GRAY
            )

            # Extract text using OCR
            text = pytesseract.image_to_string(gray)

            if text.strip():
                print("Frame:", frame_count)
                print("Extracted Text:")
                print(text)
                print("----------------------")

        # Resize video frame for small output window
        small_frame = cv2.resize(
            frame,
            (400, 300)
        )

        cv2.imshow(
            "Video Text Extraction",
            small_frame
        )

        # Press q to stop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()


# Call function
extract_text_from_video()
