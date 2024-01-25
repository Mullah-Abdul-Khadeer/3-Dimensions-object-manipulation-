from cvzone.SerialModule import SerialObject
from cvzone.HandTrackingModule import HandDetector
import cv2
import mediapipe as mp
import openpyxl
workbook = openpyxl.Workbook()
sheet = workbook.active
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)
mySerial = SerialObject("COM7", 9600) # here the COM7 is the USD port of your device the name should be changed accordingly to your device port name  and the "9600" is a bit rate of arduino uno it also has to be changed according to the micro controller device  used 
while True:

    success, img = cap.read()
    hands, img = detector.findHands(img)  
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        centerPoint1 = hand1['center']
        handType1 = hand1["type"]

        fingers1 = detector.fingersUp(hand1)
        print(fingers1)
        mySerial.sendData(fingers1)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
        break
for row in data:
    sheet.append(row)
workbook.save("model_data.xlsx")    
cap.release()
cv2.destroyAllWindows()
