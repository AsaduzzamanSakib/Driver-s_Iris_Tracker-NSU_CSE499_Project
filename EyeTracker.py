

import cv2
from eye_tracking import EyeTracking

eye = EyeTracking()
webcam = cv2.VideoCapture(0)

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to EyeTracking to analyze it
    eye.refresh(frame)

    frame = eye.annotated_frame()
    text = ""


