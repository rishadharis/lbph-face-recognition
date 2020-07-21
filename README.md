# lbph-face-recognition
Project created to complete my final project.

main-run.py
adalah program utama untuk melakukan pendeteksian wajah dan dibandingkan dengan data yang sudah ditraining, sebelum menggunakannya pastikan data sudah ditraining.

train.py
program untuk mentraining gambar yang tersimpan menjadi histogram yang disimpan dalam suatu file pickle yang siap dipanggil, data yang dilatih adalah data yang berada di folder dataset dengan format nama folder tersebut NIM_Nama, foto foto tersebut lalu akan dikategorikan menurut nim mereka

getdata.py
program untuk mengscrape data dari web yang sudah dibuat di https://ta.risgad.xyz untuk diambil dan dimasukan ke folder dataset sesuai dengan nama nim masing-masing, jika folder belum ada maka folder tersebut akan dibuat sendiri.

function.py
program yang berisi kumpulan program utama meliputi: deteksi wajah, lbp, histogram calculation, euclidean distance, absolute value, histogram check, neighbour calculation, get binary value
