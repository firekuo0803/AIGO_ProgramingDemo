import cv2

# 讀取圖檔
# img = cv2.imread("v5.jpg")
# 裁切區域的 x 與 y 座標（左上角）
x = 400
y = 100

# 裁切區域的長度與寬度
w = 1500
h = 1080

import cv2
from cvzone.PoseModule import PoseDetector
import os

path = 'no'
# cap = cv2.VideoCapture(1)
i=0


images = []
classNames = []
myList = os.listdir(path)
# for cl in myList:
#     imgCur = cv2.imread(f'{path}/{cl}',0)
#     images.append(imgCur)
#     classNames.append(os.path.splitext(cl)[0])

detector = PoseDetector()
posList = []

# while True:
    # success, img = cap.read()
for cl in myList:
    imgCur = cv2.imread(f'{path}/{cl}')
    images.append(imgCur)
# img = cv2.imread()
for img in images:
    img = img[y:y + h, x:x + w]
    # img = detector.findPose(img)
    # lmList, bboxInfo = detector.findPosition(img)

    # if bboxInfo:
    #     lmString = ''
    #     for lm in lmList:
    #         lmString += f'{lm[1]},{img.shape[0]-lm[2]}{lm[3]}'
    #
    #     posList.append(lmString)

    print(len(posList))

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    cv2.imwrite('./wrong/'+'img'+f'{i}'+'.jpg',img)
    i = i+1

# 裁切圖片
# crop_img = img[y:y+h, x:x+w]
# cv2.imshow("cropped", crop_img)
# cv2.waitKey(0)