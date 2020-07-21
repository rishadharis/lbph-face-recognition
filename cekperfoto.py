# import the opencv library
import cv2
import time
import function as fc
import pickle
import argparse
# define a video capture object
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

vid = cv2.VideoCapture(0)
# Load data hasil training
hmm = pickle.load(open("data.p","rb"))
hist, labels, dict = hmm
mindistance = 0
# Membalikan key dan value pada dictionary
dict = {v: k for k, v in dict.items()}
# Inisiasi Waktu Awal
i=0
# Real time video capture tiap detik
j=0
frame = cv2.imread('test/'+args["image"])
sad = fc.lbp(frame)
if(sad==False):
    print("Ga kedetek bro"+str(i))
    i+=1
else:
    hstgrm = fc.histCalc(sad[0],8,8)
    waktubanding = time.time()
    for g in range(len(hist)):
        hasil = fc.euclideanDistance(hstgrm, hist[g])
        if mindistance == 0:
            mindistance = hasil
            print(mindistance)
            print(dict[labels[g]])
            j = g
        else:
            if hasil < mindistance:
                mindistance = hasil
                print(mindistance)
                print(dict[labels[g]])
                j = g
    print("Terdeteksi : "+dict[labels[j]])
# Fungsi quite menggunakan tombol Q
if cv2.waitKey(1) & 0xFF == ord('q'):
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

# After the loop release the cap object
