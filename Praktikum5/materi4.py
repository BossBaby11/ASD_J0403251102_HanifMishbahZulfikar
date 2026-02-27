#=================================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan Rekursif 
#==================================================
#Contoh Rekursi 4: Backtracking kombinasi biner (n)
#==================================================

def biner(n, hasil=""):
#Case case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    #Choose + Explore: tambah '0'
    biner(n, hasil + "0")
    
    #Choose + Explore: tambah '1'
    biner(n, hasil + "1")
    
biner(3)