#========================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan Rekursif 
#=========================================
#Contoh Rekursi 2: Tracing Masuk/Keluar
#=========================================
def hitung(n):
    #Base case
    if n == 0:
        print("selesai")
        return
    print("masuk", n) #fase tracking
    hitung(n-1)       #pemanggilan rekursif
    print("keluar", n)#fase unwinding
hitung(3)