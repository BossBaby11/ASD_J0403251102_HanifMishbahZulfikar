#========================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan Rekursif 
#=========================================
#Contoh Rekursi 1: Faktorial
#=========================================
def faktorial(n):
    #Base case berhenti ketika n = 0
    if n == 0:
        return 1
    #recursive case: masalah diperkecil menjadi faktorial(n-1)
    return n * faktorial(n-1)
print(faktorial(5)) #output 120