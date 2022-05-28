# import libraries of python OpenCV
import cv2
# capture frames from a video
cap = cv2.Videocapture('video')
# some object we want detect
car_cascade = cv2.CascadeClassifier('cars.xml')
# loops runs if capturing has been initialized
while True:
    # reads frames from a video
    ret, frames = cap.read()
    # convert to gray scale of each frames
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    # detects cars of different sizes in the input image
    cars = car_cascade.detectMultiscale(gray, 1.1, 1)
    # to draw a rectangle in each cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frames, (x,y),(x+w,y+h),(0,0,255),2)
    # display frames in a window
    cv2.imshow('video2', frames)
    # wait for esc to stop the program
    if cv2.waitkey(33) == 27:
        break

# de-allocate any associated memory usage
cv2.destroyallwindows()


