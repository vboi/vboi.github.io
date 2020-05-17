from picamera import PiCamera
import time
import os

with PiCamera() as camera:
    while True:
        print("New cycle, please wait...")
        camera.capture("roomtemp.png")
        os.system("git add .")
        os.system("git commit -m 'roomtemp.png'")
        os.system("git push origin")
        time.sleep(20)
        
        os.system("git pull")
