# 평균값 필터
import numpy as np
import cv2

def mean_blur(img):
    A = np.zeros(img.shape, dtype=np.uint8)
    height, width = img.shape
    for y in range(height):
        for x in range(width):
            try :
                S = 1*img[y-1, x-1] + img[y-1, x] + img[y-1, x+1] \
                    + img[y  , x-1] + img[y  , x] + img[y  , x+1] \
                    + img[y+1, x-1] + img[y+1, x] + img[y+1, x+1]
                S = S/9
                if S>255:
                    A[y,x] = 255
                elif S<0:
                    A[y,x] = 0
                else:
                    A[y,x] = int(S)
            except:
                pass
    return A

lena_gray = cv2.imread("dotpy/data/lena.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Lena", lena_gray)
cv2.imshow("Mean Blur", mean_blur(lena_gray))
cv2.waitKey()
cv2.destroyAllWindows()