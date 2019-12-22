

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
	
	    if eye.is_blinking():
        text = "Blinking"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (0, 255, 255), 2)

    left_pupil = eye.pupil_left_coords()
    right_pupil = eye.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (10, 130), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 255, 255), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (390, 130), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 255, 255), 1)

    cv2.imshow("Eye", frame)

    if cv2.waitKey(1) == 27:
        break


