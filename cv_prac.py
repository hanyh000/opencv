import cv2
import numpy as np
cv2.namedWindow("Canvas")
canvas = np.full((512, 512, 3), 255, dtype=np.uint8)
clear_canvas = canvas.copy()
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN :
        print("왼쪽 버튼 클릭:", x, y)
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON :
            cv2.circle(canvas, (x, y), 3, (0, 0, 0), -1)  
            print("왼쪽 버튼 클릭:", x, y)
            cv2.imshow('Canvas', canvas)

cv2.setMouseCallback('Canvas', mouse_callback, canvas)
while True:
    cv2.imshow('Canvas', canvas)
    
    key = cv2.waitKey(1)
    print(key)
    if key == 99:
        canvas[:] = clear_canvas[:]

    elif key == 113 or key == 27:
        break
cv2.destroyAllWindows()
#c,q,