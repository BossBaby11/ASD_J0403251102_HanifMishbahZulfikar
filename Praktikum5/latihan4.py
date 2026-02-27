#=======================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan Rekursif 
# ======================================
# Latihan 4: Kombinasi Huruf
# ======================================
def kombinasi(n, hasil=""):
    if len(hasil) == n:
        print(hasil)
        return
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")
kombinasi(2)

"""
Fungsi akan berjalan dengan mengecek kondisi terlebih dahulu apakah panjang string hasil sudah sama dengan n, jika belum terpenuhi
maka akan menjalankan recursive pertama dengan kombinasi A hingga kondisi terpenuhi. jika kombinasi A sudah terpenuhi makan akan
dilanjut dengan kombinasi antara A dan B,setelah sudah memenuhi kondisi lanjut ke kombinasi B dan A dan dilanjut ke kombinasi B. 
Hal ini terus terulang hingga kondisi terpenuhi yaitu panjang string = n, maka berdasarkan contoh di atas didapat hasil
AA
AB
BA
BB
"""