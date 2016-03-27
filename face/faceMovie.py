import cv2

cascade_path = 'data/haarcascades/cascade.xml'

def detectFace(image):
    image_gray = cv2.cvtColor(image,  cv2.COLOR_BGR2GRAY)
    return cv2.CascadeClassifier(cascade_path).detectMultiScale(image_gray, scaleFactor=1.15, minNeighbors=3, minSize=(50, 50))

video_path = 'data/movie/testdata/2/face.avi'
cap = cv2.VideoCapture(video_path)

framenum = 0
facerect = []

while(True):
    framenum += 1
    ret, image = cap.read()
    if not ret:
        break

    if framenum%10 == 0:
        facerect = detectFace(image)

    if len(facerect) != 0:
        for rect in facerect:
            cv2.rectangle(image, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), (255, 255, 255), thickness=2)
    cv2.imshow('application', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()