import cv2
list = []
faceCascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("./haarcascade_eye.xml")
def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
    coords = []
    face = "F"
    for (x, y, w, h) in features:
        face = "P"
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
        cv2.putText(img, text, (x, y-4),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1)
        coords = [x, y, w, h]
    if face == "P":
        check = 1
    elif face == "F":
        check = 0
    list.append(check)
    return img, coords
def create_dataset(img, id, img_id):
    cv2.imwrite("data/picture."+str(img_id)+".jpg", img)
def detect(img, faceCascade, eyeCascade, img_id):
    img, coords = draw_boundary(
        img, faceCascade, 1.1, 10, (255, 255, 0), "Face")
    img, coords = draw_boundary(img, eyeCascade, 1.1, 10, (255, 0, 0), "Eye")
    id = 1
    create_dataset(img, id, img_id)
    return img
img_id = 1
cap = cv2.VideoCapture(0)
class Face_detection():
    while True:
        ret, frame = cap.read()
        frame = detect(frame, faceCascade, eyeCascade, img_id)
        img_id += 1
        if img_id == 51:
            alll = len(list)
            list = sum(list)
            global face_detection_percent
            face_detection_percent = (str(list/alll * 100)+"%")
            break