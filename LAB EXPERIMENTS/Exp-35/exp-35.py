
import cv2

def add_text():
    img = cv2.imread("image.jpg")

    if img is None:
        print("Image not found!")
        return

    text = input("Enter text to display: ")

    cv2.putText(
        img,
        text,
        (50, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    small_original = cv2.resize(img, (400, 300))

    cv2.imshow("Image with Text", small_original)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

add_text()
