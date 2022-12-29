import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
image = cv2.imread("pysource_qrcode.png")
# decodedObjects = pyzbar.decode(image)
# for obj in decodedObjects:
#     print("Type:", obj.type)
#     print("Data: ", obj.data, "\n")
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
while True:
    _, frame = cap.read()
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        print("Data", obj.data)
        cv2.putText(frame, str(obj.data), (50, 50), font, 2,(255, 0, 0), 3)
    cv2.imshow("Image", frame)
    key=cv2.waitKey(1)
    if key == 27:
        break
