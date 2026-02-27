#========================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan Rekursif 
#=========================================
#Latihan 2: Tracing Rekursi
#=========================================
def countdown(n):
    if n == 0:
        print("selesai")
        return
    print("Masuk:", n)
    
    countdown(n-1)
    print("Keluar:", n)   
countdown(3)

"""
Pada fungsi di atas program berjalan secara linear dimana nilai n akan dicek apakah = 0 jika iya maka output = selesai, jika tidak
maka akan lanjut ke proses print dengan string "Masuk:" dan nilai n. Kemudian dilanjut dengan rekursif fungsi itu sendiri dan akan
melakukan pengecekan ulang apakah n = 0. Jika n = 0 maka otomatis akan keluar dari rekursif dan melanjutkan kode berikutnya dalam
fungsi yaitu print dengan string "Keluar:" dan nilai n. Itulah mengapa pada contoh dengan n = 3 output yang dihasilkan berupa=
Masuk: 3
Masuk: 2
Masuk: 1
selesai
Keluar: 1
Keluar: 2
Keluar: 3
"""