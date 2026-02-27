#=======================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan Rekursif 
# ======================================
# Studi Kasus: Generator PIN
# ======================================
def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)
buat_pin(3)

"""
Fungsi akan berjalan dengan melakukan pengecekan kondisi apakah index hasil sudah sama dengan nilai panjang. Jika belum maka akan
dilanjut dengan looping dimana string hasil akan dimasukkan dengan nilai index antara "0", "1", "2". Berdasarkan looping maka nilai
index yang akan diprioritaskan adalah nilai 0 hingga kondisi len(hasil) == panjang, baru beganti ke optional lainnya yaitu 1 dan
terakhir 2. maka pada contoh dengan panjang = 3 nilai yang diberikan adalah =
PIN: 001
PIN: 002
PIN: 010
PIN: 011
PIN: 012
PIN: 020
PIN: 021
PIN: 022
PIN: 100
PIN: 101
PIN: 102
PIN: 110
PIN: 111
PIN: 112
PIN: 120
PIN: 121
PIN: 122
PIN: 200
PIN: 201
PIN: 202
PIN: 210
PIN: 211
PIN: 212
PIN: 220
PIN: 221
PIN: 222
Karena looping akan selalu memprioritaskan indeks terkecil terlebih dahulu sebagai acuan utama barulah beralih ke nilai index akhir
"""