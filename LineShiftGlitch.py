import cv2
import random
img = cv2.imread('demo.jpg')
width = 500
height = round(width / img.shape[1] * img.shape[0])
img = cv2.resize(img,(width,height))

frame = img.copy()
while True:
    number_line = random.randint(100,500)
    for i in range(0,number_line):
        n = random.randint(0,img.shape[0] - 1)
        shift_n = random.randint(0,20)
        color_channel = random.randint(0,2)
        frame[n,:frame.shape[1] - shift_n,color_channel] = img[n,shift_n:,color_channel]
    cv2.imwrite('LineShiftGlitch.jpg',frame)
    cv2.imshow('demo',frame)
    cv2.waitKey(50)