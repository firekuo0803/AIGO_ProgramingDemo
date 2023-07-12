import cv2
from cvzone.PoseModule import PoseDetector
import os

path = 'photo'
path2 = 'photo_download'
cap = cv2.VideoCapture(1)
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
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img)

    # if bboxInfo:
    #     lmString = ''
    #     for lm in lmList:
    #         lmString += f'{lm[1]},{img.shape[0]-lm[2]}{lm[3]}'

        # posList.append(lmString)

    print(len(posList))

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    cv2.imwrite(f'./{path2}/'+'img'+f'{i}'+'.jpg',img)
    i = i+1
