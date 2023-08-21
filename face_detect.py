import cv2

img = cv2.imread("boy.jpg")
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(grey, 1.1, 5)
print(faces)

for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    face = img[y:y+h, x:x+w]
    cv2.imwrite("face.jpg", face)
cv2.imshow("img", img)
cv2.waitKey(0)
