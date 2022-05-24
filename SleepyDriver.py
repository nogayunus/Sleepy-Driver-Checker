import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

video = cv2.VideoCapture(0)
video.set(3, 1280)
video.set(4, 720)

detector = FaceMeshDetector(maxFaces=1)

while True:
    success, img = video.read()
    img, faces = detector.findFaceMesh(img, draw=False)

    try:
        face = faces[0]
        leftEye = face[145]
        rightEye = face[374]
        cv2.circle(img, leftEye, 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, rightEye, 5, (255, 0, 255), cv2.FILLED)
        cv2.line(img, leftEye, rightEye, (0, 200, 0), 3)
        w, _ = detector.findDistance(leftEye, rightEye)
        W = 6.3
        # d = 50
        # f = (w*d)/W
        f = 740
        d = (W * f) / w

        cvzone.putTextRect(img, f'Distance: {int(d)} cm', (900, 100), scale=2)
        if d <= 35:
            cvzone.putTextRect(img, "You are sleeping.. PLEASE WAKE UP !", (300, 500), scale=2)


    except IndexError:
        cvzone.putTextRect(img, "You are sleeping.. PLEASE WAKE UP !", (300, 500), scale=2)

    cv2.imshow("Sleepy Driver Checker", img)
    cv2.waitKey(1)
