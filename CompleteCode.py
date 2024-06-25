import cv2
from cvzone.HandTrackingModule import HandDetector
from LX16A import LX16A

motor =LX16A()

# Función para mover los motores según los dedos levantados
def flexion_extension(fingers):
    positions = [(200, 900), (0, 600), (0, 600), (0, 700), (0, 700)]
    for i in range(5):
        speed = 800 if i == 0 else 600
        if fingers[i] == 1:
            motor.moveServo(i+1, positions[i][0], speed)
            if motor.readPosition(i+1) == positions[i][0]:
                motor.moveServoStop(i+1)
        elif fingers[i] == 0:
            motor.moveServo(i+1, positions[i][1], speed)
            if motor.readPosition(i+1) == positions[i][0]:
                motor.moveServoStop(i+1)
        else:
            motor.moveServoStop(i+1)

def set_motores():
    for i in range(0,5):
            motor.moveServo(i+1,500,200)
            if motor.readPosition(i+1)== 500:
                motor.moveServoStop(i+1)

def flexion_pulgar(fingers):
    if fingers[0] == 1:
        motor.moveServo(1, 200, 200)
    else:
        motor.moveServo(1,900,200)


def flexion_interfalangica_pulgar(fingers):
    if fingers[0] == 1:
        motor.moveServo(1, 300, 600)
    else:
        motor.moveServo(1,800,700)

def pinza_indice(fingers):
    positions = [(200, 900), (100, 600)]
    for i in range(2):
        if fingers[i]==1:
            motor.moveServo(i+1,positions[1][0],300)
        elif fingers[i]==0:
            motor.moveServo(i+1,positions[0][1],300)


cap = cv2.VideoCapture(2)
detector = HandDetector(maxHands=1, detectionCon=0.9)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        flexion_extension(fingers)
        #flexion_pulgar(fingers)
        #flexion_interfalangica_pulgar(fingers)
        #pinza_indice(fingers)
        

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('o'):
        break

cap.release()
cv2.destroyAllWindows()
set_motores()
