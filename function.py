import cv2
import numpy as np
import math

'''
Function.py
Oleh Rishad Harisdias Bustomi
Berisi fungsi yang siap dipanggil
'''

#DETEKSI WAJAH -- Mendapatkan ROI wajah dari gambar yang ada di dataset
def deteksi_wajah(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    haar = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    face = haar.detectMultiScale(img_gray, scaleFactor=1.3, minNeighbors=7)
    if (len(face) > 0):
        (x, y, w, h) = face[0]
        img = img_gray[y:y+h,x:x+w]
        img = cv2.resize(img,(300,300))
        return img, face[0]
    else:
        return False

#Dapatkan Nilai Biner dari hasil pembandingan threshold
def get_binary_value(value, threshold):
    if value>=threshold:
        return "1"
    else:
        return "0"

#Mendapatkan nilai biner dari suatu pixel
def calculate(image, ro, col, threshold):
    sad = ""
    for y in range(ro - 1, ro + 2):
        if y > image.shape[0] - 1:
            y_ = y - 4
        else:
            y_ = y
        for x in range(col - 1, col + 2):
            if x == col and y == ro:
                continue
            if x > image.shape[1] - 1:
                x_ = x - 3
            else:
                x_ = x
            value = image[y_][x_]
            hasil = get_binary_value(value, threshold)
            sad += hasil
    biner = int(sad, 2)
    return biner

#Merubah semua pixel dalam gambar menjadi lbp
def lbp(image):
    lebar = 480
    #tinggi = int((image.shape[0]/image.shape[1])*lebar)
    #oy = cv2.resize(image,(lebar,tinggi))
    face_detect = deteksi_wajah(image)
    if not face_detect == False:
        wajah = face_detect[0]
        area_wajah = face_detect[1]
        height, width = wajah.shape
        img_lbp = np.zeros((height, width), np.uint8)
        for y in range(height):
            for x in range(width):
                threshold = wajah[y][x]
                andai = calculate(wajah, y, x, threshold)
                img_lbp[y][x] = andai
        return img_lbp, area_wajah
    else:
        return False
'''
Fungsi Histogram
'''
def histCalc(image, gridX, gridY):
    hist = []
    if image.any()==False:
        return False,1
    if gridX <= 0 or gridX >= image.shape[1]:
        return False,2
    if gridY <= 0 or gridY >= image.shape[0]:
        return False,3
    gridWidth = image.shape[1]/gridX
    gridHeight = image.shape[0]/gridY
    for gX in range(gridX):
        for gY in range(gridY):
            #Create Slice
            regionHistogram = np.zeros(256)

            #Define Start and End
            startPosX = gX * gridWidth
            startPosY = gY * gridHeight
            endPosX = (gX+1) * gridWidth
            endPosY = (gY+1) * gridHeight

            #Make sure no pixel leave
            if gX==gridX-1:
                endPosX = image.shape[1]
            if gY==gridY-1:
                endPosY = image.shape[0]

            # Creates Histogram for current region
            for x in range(int(startPosX),int(endPosX)):
                for y in range(int(startPosY),int(endPosY)):
                    if x < len(image):
                        if y < len(image[x]):
                            if image[x][y] < len(regionHistogram):
                                regionHistogram[image[x][y]]+=1
            hist = [element for lis in [hist, regionHistogram] for element in lis]
    return hist

'''
Fungsi Matematik Euclidean Distance
'''
def checkHistograms(hist1, hist2):
    if len(hist1) == 0 or len(hist2) == 0:
        return "Could not compare the histogram beause empty"
    if len(hist1) != len(hist2):
        return "Tidak memiliki size yang sama"
    return True

def euclideanDistance(hist1,hist2):
    cek = checkHistograms(hist1,hist2)
    if cek != True:
        return False
    sum = 0
    for y in range(len(hist1)):
        sum += math.pow(hist1[y]-hist2[y],2)

    return math.sqrt(sum)

def euclideanDistance_normalized(hist1,hist2):
    cek = checkHistograms(hist1,hist2)
    if cek != True:
        return False
    sum = 0
    n = len(hist1)
    for y in range(len(hist1)):
        sum += math.pow(hist1[y]-hist2[y],2) / n

    return math.sqrt(sum)

def absoluteValue(hist1,hist2):
    cek = checkHistograms(hist1,hist2)
    if cek!= True:
        return False
    sum = 0
    for y in range(len(hist1)):
        sum += abs(hist1[y]-hist2[y])
    return sum