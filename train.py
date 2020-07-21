import function as fc
import cv2
import pickle
import os

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
            wajah2, area2 = fc.lbp(dataset)
            hist2 = fc.histCalc(wajah2,8,8)
            hist.append(hist2)
            labels.append(i)
            print(image_path[8:] + ' succesfully trained')
        else:
            print(image_path[8:] + ' tidak terdeteksi wajah')
    i+=1
hmm = [hist,labels,dict]
print(hmm)
pickle.dump(hmm, open("data.p","wb"))
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
