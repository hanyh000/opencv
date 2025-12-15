import cv2

cap = cv2.VideoCapture(0)
number = 1

while cap.isOpened() : 

    ret, frame = cap.read()

    cv2.imshow("frame", frame)
    key = cv2.waitKey(50)
    if key == 27 : break
    elif key == ord("c") : 
        cv2.imwrite(f"tumbler_{number}.png", frame)
        number += 1

cv2.destroyAllWindows()