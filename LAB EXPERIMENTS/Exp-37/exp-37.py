
import cv2
import numpy as np

def foreground_subtraction():
    img = cv2.imread("image.jpg")

    if img is None:
        print("Image not found!")
        return

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    print("Enter foreground HSV lower values")
    h1 = int(input("Lower H: "))
    s1 = int(input("Lower S: "))
    v1 = int(input("Lower V: "))

    print("Enter foreground HSV upper values")
    h2 = int(input("Upper H: "))
    s2 = int(input("Upper S: "))
    v2 = int(input("Upper V: "))

    lower = np.array([h1, s1, v1])
    upper = np.array([h2, s2, v2])

    mask = cv2.inRange(hsv, lower, upper)

    foreground = cv2.bitwise_and(
        img, img, mask=mask
    )

    small_original = cv2.resize(img, (400, 300))
    small_foreground = cv2.resize(
        foreground, (400, 300)
    )

    cv2.imshow("Original Image", small_original)
    cv2.imshow("Foreground", small_foreground)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

foreground_subtraction()
