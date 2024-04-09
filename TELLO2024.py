import cv2 as cv
import numpy as np
import matplotlib as plt
import djitellopy as Tello

# ------------------------------------ Camera setup

tello = Tello()                        # Initiate Tello instance
tello.connect()                        # Connect to the drone
tello.streamon()                       # Start stream
image = tello.get_frame_read().frame   # Get first frame

# ------------------------------------ HSV bounds

LOWER = np.array((88, 166, 51))
UPPER = np.array((179, 255, 255))jakh o