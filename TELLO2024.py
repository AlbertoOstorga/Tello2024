import cv2 as cv
import numpy as np
import matplotlib as plt
from djitellopy import Tello
import tkinter as tk
from PIL import Image, ImageTk

# ------------------------------------ Camera setup

tello = Tello()                                # Initiate Tello instance
#tello.connect()                                # Connect to the drone
#tello.streamon()                               # Start stream
#image = tello.get_frame_read().frame           # Get first frame

# ------------------------------------ HSV bounds

LOWER = np.array((88, 166, 51))
UPPER = np.array((179, 255, 255))

# ------------------------------------ INTERFACE

interface = tk.Tk()

interface.geometry("300x600")                   # Dimensiones: Anchura x Altura
interface.configure(background="black")         # Color del fondo: Negro
tk.Wm.wm_title(interface, "Menú de Tello")

def ParoEmergencia():
    tello.emergency()

frame_right = tk.Frame(interface, bg="black")
frame_right.pack(side=tk.RIGHT, fill=tk.Y)

tk.Button(
    frame_right, 
    text="PARO EMERGENCIA",
    bg="red",
    fg="white",
    command=ParoEmergencia, 
    width=5, 
).pack(pady=10)

tk.Label(
    interface,
    text="REPORTE",
    fg="white",
    bg="black",
    justify="center"
).pack(
    fill=tk.BOTH,
    expand=True,
)

interface.mainloop()                            # Refresca la interfaz