#========================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan sort 
#=========================================

"""Pak Budi adalah seorang manager sumber daya manusia di suatu perusahaan. Ia
saat ini harus menseleksi pelamar kerja berdasarkan skor tes potensi akademik
mereka. Skor tersebut disajikan dalam bentuk list dengan rentang nilai 0 - 100.
Berikut adalah data hasil tes potensi akademik yang tersedia:
[43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
Soal:
1. Jika Pak Budi akan meloloskan lima kandidat dengan nilai tertinggi, tuliskanlah
skor lima kandidat tersebut dari yang paling tinggi hingga terendah.
2. Kandidat berapa saja yang lolos?"""

def seleksi_kandidat(data_skor):
    # 1.Gabungkan skor dengan nomor urut
    list_lengkap = []
    for i in range(len(data_skor)):
        list_lengkap.append([data_skor[i], i + 1])

    # 2. Proses Bubble Sort secara descending 
    n = len(list_lengkap)
    for passnum in range(n - 1, 0, -1):
        for i in range(passnum):
            if list_lengkap[i][0] < list_lengkap[i + 1][0]:
                temp = list_lengkap[i]
                list_lengkap[i] = list_lengkap[i + 1]
                list_lengkap[i + 1] = temp
    
    # Jawaban Nomor 1
    lima_teratas = []
    for k in range(5):
        lima_teratas.append(list_lengkap[k][0])
    print(lima_teratas)

    # Jawaban Nomor 2
    print("\n2. Kandidat yang dinyatakan lolos:")
    for k in range(5):
        print("Kandidat ke-", list_lengkap[k][1])

skor_tes = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
seleksi_kandidat(skor_tes)