#========================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan Rekursif 
#=========================================
#Latihan 1: Rekursif Pangkat
#=========================================
def pangkat(a, n):
    #Base case
    if n == 0:
        return 1
    #Recursive case
    return a * pangkat(a, n-1)
print(pangkat(2, 4)) #output 16
"""
Alur pada pemrograman di atas adalah variabel a berperan sebagai angka yang akan dikali dan variabel n merupakan pangkat yang
akan diproses melalui proses rekursif. pada kode terdapat kondisidimana jika n (pangkat) = 0 maka return 1. jika n lebih dari 
0 maka akan dijalankan proses return a * fungsi rekursif dengan n - 1, dimana logika ini akan mengalikan nilai a hingga
n = 0. Dari contoh inputan a = 2 dan n = 4 maka proses yang dilakukan oleh sistem adalah return nilai a yaitu 2 * fungsi rekursif
yang dimana tiap kali dilakukan fungsi rekursif maka n akan dikurangi 1 hingga n = 0 barulah rekursif berhenti. Maka secara
proses akan tergambar seperti berikut = 2 * 2 * 2 * 2 * 1 = 16
"""

