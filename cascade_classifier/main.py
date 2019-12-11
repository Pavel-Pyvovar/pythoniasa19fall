import cv2
import logging
import time

CASCADESFILE = 'data/haarcascades/haarcascade_frontalface_default.xml'
EYESFILE = 'data/haarcascades/haarcascade_smile.xml'
LOGFILE = 'log/faces.log'

logging.basicConfig(filename=LOGFILE, level='DEBUG')
# filename
# Specifies that a FileHandler be created, using the specified filename, rather than a StreamHandler.

def main():

    model = cv2.CascadeClassifier(CASCADESFILE)
    modeleyes = cv2.CascadeClassifier(EYESFILE)
    webcam = cv2.VideoCapture(0)

    # infinite image processing loop
    while True:

        if not webcam.isOpened():
            logging.warning('Unable to connect to camera.')
            time.sleep(5)
            continue

        # get image from camera
        ret, frame = webcam.read()
        # frame = frame/255

        # convert image to grayscale
        grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        # detect faces
        faces = model.detectMultiScale(grayframe, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60), maxSize=(300, 300))
        eyes = modeleyes.detectMultiScale(grayframe, scaleFactor=1.01, minNeighbors=2, minSize=(50, 50), maxSize=(100, 100))
        logging.info(f'Detected faces: {len(faces)}')
        # print(faces)
        # print(type(eyes))
        # time.sleep(1000)
        # add boxes
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        in_face_box = []
        for (x, y, w, h) in eyes:
            for (x1, y1, w1, h1) in faces:
                if all([x1<x, x+w<x1+w1, y1<y, y+h<y1+h1, y < (y1 + h1/2)]):
                    in_face_box.append([x, y, w, h])
        
        if in_face_box:
            m = in_face_box[0][1]
            rects_of_intr = 0
            e1, e2 = 0, 0
            for i, eye1 in enumerate(in_face_box):
                for j, eye2 in enumerate(in_face_box):
                    if abs(eye1[1] - eye2[1]) < m and i != j:
                        m = abs(eye1[1] - eye2[1])
                        rects_of_intr = i, j
                        e1, e2 = eye1, eye2

            for x, y, w, h in eye1, eye2:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # show image
        cv2.imshow('Video', frame)

        # stop if user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # close everything
    webcam.release()
    cv2.destroyWindows()


if __name__ == '__main__':
    main()
