import cv2
from random import randrange

# Load some pre-trained data on face frontals from OpenCV(haar cascade algorithms)
trained_face_data = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')

# Choose an image to detect faces in
#img = cv2.imread('kn.jpg')
# to capture from webcam
webcam = cv2.VideoCapture(0)

# Iterate forever over frames
while True:
    # Read thr current frame
    successful_frame_read, frame = webcam.read()

    # convert the image into grayscale first
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# # Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# # Draw rectangles around the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h),
                      (randrange(256), randrange(256), randrange(256)), 3)

# # print(face_coordinates)

    # Showing the face
    cv2.imshow('My first face detection program', frame)
    key = cv2.waitKey(1)

    # stop id Q key is pressed
    if key == 81 or key == 113:
        break

# Release the video capture object
webcam.release()

print("code completed!")
