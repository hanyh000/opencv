'''
OpenCV 패키지에는 다양한 상수가 정의되어 있다
상수란? 어떤 값이 저장되어 있고 그 의미가 고정되어 있는 변수! 

문제는... OpenCV 에는 상수가 엄청나게 많다는 점이다. 
모두 외울 수는 없으므로.... 그 종류를 빠르게 파악하는
방법을 알아둘 필요가 있다!
'''
import cv2

# dir : 목록 보기 함수 
# startswith : ~~으로 시작해야 True
flags = [flag for flag in dir(cv2) if flag.startswith("COLOR_")]
print(flags[:50])