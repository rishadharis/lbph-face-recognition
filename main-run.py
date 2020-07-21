# import the opencv library
import cv2
import time
import function as fc
import pickle
from datetime import datetime
import requests
# define a video capture object
vid = cv2.VideoCapture(0)
# Load data hasil training
hmm = pickle.load(open("data.p","rb"))
hist, labels, dict = hmm
mindistance = 0
# Membalikan key dan value pada dictionary
dict = {v: k for k, v in dict.items()}
# Inisiasi Waktu Awal
waktu = time.time()
i=0
# Real time video capture tiap detik
while (True):
    j=0
    # Menghitung waktu proses
    current = time.time()
    # Membandingkan waktu proses dan waktu awal
    total = current-waktu

    # Capture video perframe
    ret, frame = vid.read()

    # Settingan font
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50,50)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2

    # Bikin tulisan countdown
    if(total>=1 and total<2):
        image = cv2.putText(frame, '1', org, font,
                            fontScale, color, thickness, cv2.LINE_AA)
    elif(total>=2 and total<3):
        image = cv2.putText(frame, '2', org, font,
                            fontScale, color, thickness, cv2.LINE_AA)
    elif(total>=3 and total<4):
        image = cv2.putText(frame, '3', org, font,
                            fontScale, color, thickness, cv2.LINE_AA)
    elif(total>=4 and total<5):
        image = cv2.putText(frame, '4', org, font,
                            fontScale, color, thickness, cv2.LINE_AA)
    else:
        image = cv2.putText(frame, 'Check', org, font,
                            fontScale, color, thickness, cv2.LINE_AA)
    # Tampilkan hasil frame
    cv2.imshow('frame', image)
    # Cek apakah total waktu 5 detik atau lebih, jika ya artinya video tersebut dicapture
    if (total >= 5):
        waktu = time.time()
        sad = fc.lbp(frame)
        if(sad==False):
            print("Ga kedetek bro"+str(i))
            i+=1
        else:
            waktulbp = time.time()
            hstgrm = fc.histCalc(sad[0],8,8)
            waktubanding = time.time()
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
            print("Waktu total :"+str(time.time()-waktu))
            print("Waktu lbp : "+str(waktulbp-waktu))
            print("Waktu banding : "+str(time.time()-waktubanding))
    # Fungsi quite menggunakan tombol Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object 
vid.release()
# Destroy all the windows 
cv2.destroyAllWindows() 
