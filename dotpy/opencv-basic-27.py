import cv2
import numpy as np

def expansion(img_in):
    height, width = img_in.shape
    img_out = np.zeros(img_in.shape, np.uint8)
    for y in range(1, height-1):
        for x in range(1, width-1):
            img_out[y,x] = img_in[y,x]
            if img_in[y-1,x-1]==255:
                img_out[y,x] = 255
            if img_in[y-1,x  ]==255:
                img_out[y,x] = 255
            if img_in[y-1,x+1]==255:
                img_out[y,x] = 255
                
            if img_in[y  ,x-1]==255:
                img_out[y,x] = 255
            if img_in[y  ,x+1]==255:
                img_out[y,x] = 255
                
            if img_in[y+1,x-1]==255:
                img_out[y,x] = 255
            if img_in[y+1,x  ]==255:
                img_out[y,x] = 255
            if img_in[y+1,x+1]==255:
                img_out[y,x] = 255
    return img_out

imgMPG = cv2.imread("dotpy/data/morphology.jpg", cv2.IMREAD_GRAYSCALE)
imgMPG_cont = expansion(imgMPG)
cv2.imshow("MPG", imgMPG)
cv2.imshow("imgMPG_cont", imgMPG_cont)
cv2.waitKey()
cv2.destroyAllWindows()