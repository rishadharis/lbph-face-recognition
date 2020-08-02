import sys
sys.path.append('/usr/local/lib/python3.7/site-packages')
import cv2
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
import function as fc
import pickle
from datetime import datetime
import requests

#Setting pi camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.vflip=True
camera.brightness = 55
camera.contrast = 0
camera.framerate = 5
rawCapture = PiRGBArray(camera, size=(640, 480))

# Load data hasil training
hmm = pickle.load(open("data.p","rb"))
hist, labels, dict = hmm

# Membalikan key dan value pada dictionary
dict = {v: k for k, v in dict.items()}
waktu = time.time()
countdown = 14
mindistance = 0
for frames in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    current = time.time()
    total = current-waktu
    # Capture video perframe
    frame = frames.array
    # Settingan font
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50,50)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2
    # Bikin tulisan countdown
    for aw in range(1,countdown):
        if(total>=aw and total<aw+1):
            print(aw)
    # Tampilkan hasil frame
    if (total >= countdown):
        waktu = time.time()
        sad = fc.lbp(frame)
        if(sad==False):
            print("Ga kedetek bro")
            countdown = 3
        else:
            print("mendeteksi wajah...")
            hstgrm = fc.histCalc(sad[0],8,8)
            for g in range(len(hist)):
                hasil = fc.euclideanDistance(hstgrm, hist[g])
                if mindistance == 0:
                    mindistance = hasil
                    j = g
                else:
                    if hasil < mindistance:
                        mindistance = hasil
                        j = g
            now = datetime.now()
            tanggal = now.strftime("%d-%m-%Y")
            jam = now.strftime("%H-%M-%S")
            r =requests.get('https://ta.risgad.xyz/get/index/'+tanggal+'/'+jam+'/'+dict[labels[j]])
            print(type(r.status_code))
            print("Terdeteksi : "+dict[labels[j]])
            print(time.time()-waktu)
            countdown = 14
    key = cv2.waitKey(1) & 0xFF
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
