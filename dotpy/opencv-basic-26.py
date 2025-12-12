import cv2
import numpy as np

def contraction(img_in):
    height, width = img_in.shape
    img_out = np.zeros(img_in.shape, np.uint8)
    for y in range(1, height-1):
        for x in range(1, width-1):
            img_out[y,x] = img_in[y,x]
            if img_in[y-1,x-1]==0:  
                img_out[y,x] = 0
            if img_in[y-1,x  ]==0:
                img_out[y,x] = 0
            if img_in[y-1,x+1]==0:
                img_out[y,x] = 0
                
            if img_in[y  ,x-1]==0:
                img_out[y,x] = 0
            if img_in[y  ,x+1]==0:
                img_out[y,x] = 0
                
            if img_in[y+1,x-1]==0:
                img_out[y,x] = 0
            if img_in[y+1,x  ]==0:
                img_out[y,x] = 0
            if img_in[y+1,x+1]==0:
                img_out[y,x] = 0
    return img_out

imgMPG = cv2.imread("dotpy/data/morphology.jpg", cv2.IMREAD_GRAYSCALE)
imgMPG_cont = contraction(imgMPG)
cv2.imshow("MPG", imgMPG)
cv2.imshow("imgMPG_cont", imgMPG_cont)
cv2.waitKey()
cv2.destroyAllWindows()