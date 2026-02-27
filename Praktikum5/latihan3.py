#========================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan Rekursif 
#=========================================
#Latihan 3: Mencari Niali Maksimum
#=========================================
def cari_maks(data, index=0):
    #Base Case
    if index == len(data) - 1:
        return data[index]
    
    #Recursive case
    maks_sisa = cari_maks(data, index + 1)
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa
    
angka = [3,7,2,9,5]
print("NIlai Maksimum:", cari_maks(angka))

"""
Program ini akan berjalan dengan melakukan pengecekan secara terbalik dari index ujung/akhir hingga index awal, dengan awalan
membaca data dari index terkecil, kemudian berjalan ke index terbesar, sesuai dengan kode dimana base case akan dijalankan lalu
jika belum memenuhi kondisi maka akan dilanjutkan recursive case yang akan mendaftarkan setiap nilai index hingga batas/ujung dari
index yang diinput. Setelah sudah mencapai batas maka fungsi akan melakukan pengecekan secara terbalik apakah nilai index saat
ini lebih kecil dari maks_sisa sebelumnya hingga index awal dan kondisi base case terpenuhi maka pengecekan selesai.

Berdasarkan contoh dapat dilihat jumlah batas index yang dimiliki adalah 5. Maka proses pengecekan akan dilakuakan dari index 0
hingga index 5 karena base case belum terpenuhi. Baru setelah mencapai batas, maka akan dilakukan pengecekan berkala mulai dari
nilai di index tertinggi yaitu 5(maks_sisa) terhadap 9(data[index]), pengecekan akan terus dilakukan dengan menyimpan nilai 
tertinggi dan membandingkannya dengan nilai hingga index ke 0. Maka didapat nilai 9
"""