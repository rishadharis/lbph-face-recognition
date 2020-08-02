import function as fc
import sys
sys.path.append('/usr/local/lib/python3.7/site-packages')
import cv2
import pickle
import os
import time

#start_time = time.time()
source = 'dataset'
folders = os.listdir(source)
hmm = []
hist = []
labels = []
dict = {}
i = 0
for folder in folders:
    image_path_source = source + '/' + folder
    plit = folder.split('_')
    nim = plit[0]
    nama = plit[1].replace("-"," ").lower()
    if not nama in dict:
        dict[nim] = i
    for image in os.listdir(image_path_source):
        image_path = image_path_source + '/' + image
        dataset = cv2.imread(image_path)
        sad = fc.lbp(dataset)
        if not sad == False:
            euys = time.time()
            wajah2, area2 = fc.lbp(dataset)
            print("Waktu lbp : "+str(time.time()-euys))
            euyd = time.time()
            hist2 = fc.histCalc(wajah2,8,8)
            print("Waktu hist calc : "+str(time.time()-euyd))
            hist.append(hist2)
            labels.append(i)
            print(image_path[8:] + ' succesfully trained')
            print("Waktu proses : "+str(time.time()-euys))
        else:
            print(image_path[8:] + ' tidak terdeteksi wajah')
    i+=1
hmm = [hist,labels,dict]
print(hmm[1])
print(hmm[2])
pickle.dump(hmm, open("data.p","wb"))
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
