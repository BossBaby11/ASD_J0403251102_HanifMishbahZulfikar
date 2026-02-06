#Nama: Hanif Mishbah Zulfikar 
#NIM: J0403251102
#==========================================================
#Praktikum 2 : Konsep ADT dan File Handing (STUDI KASUS)
#Latihan   1 : Membuat fungsi Load Data dari file
#==========================================================

file_path = "./J0403251102_HanifMishbahZulfikar_A2_Pertemuan1/data_mahasiswa.txt"

def read_file(file_path):
    data_dict = {} #inisialisasi data dictionary
    with open(file_path, 'r', encoding='utf-8') as file:
        for baris in file: 
            baris = baris.strip() #ambil data per baris dan hilangkan new line
            nim, nama, nilai = baris.split(",") #ambil data per item data
            data_dict[nim]={"nama": nama, "nilai": int(nilai)} #masukkan dalam dictionary
    return data_dict

#open_file = read_file(file_path)
#print("jumlah data tebaca", len(open_file))

#==========================================================
#Praktikum 2 : Konsep ADT dan File Handing (STUDI KASUS)
#Latihan   2 : Membuat fungsi menampilkan data
#==========================================================

def show_file(data_dict):
    #Create Table Header
    print("\n========= Daftar Mahasiswa =========")
    print(f"{'    NIM' : <10} | {'    NAMA' : <12} | {' Nilai' : >5}")
    print("-" * 36)#Create Line
    #Show Dictionary Value
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim: <10} | {nama: <12} | {int(nilai): >5}")


#show_file(open_file) #Call Function

#==========================================================
#Praktikum 2 : Konsep ADT dan File Handing (STUDI KASUS)
#Latihan   3 : Membuat fungsi mencari data
#==========================================================

def search_data(data_dict):
    #Pencarian data berdasarkan nim sebagai key dictionary
    #Membuat input nim mahasiswa yang akan dicari
    search_nim = input("Masukkan NIM Mahasiswa yang akan dicari: ").strip()
    
    if search_nim in data_dict:
        nama = data_dict[search_nim]["nama"]
        nilai = data_dict[search_nim]["nilai"]
        print("====== Data Mahasiswa Ditemukan =====")
        print(f"NIM   : {search_nim}")
        print(f"Nama  : {nama}")
        print(f"Nilai : {nilai}")
    else: print("Data tidak ditemukan. Pastikan NIM yang dimasukkan benar")

#Call data function
#search_data(open_file)

#==========================================================
#Praktikum 2 : Konsep ADT dan File Handing (STUDI KASUS)
#Latihan   4 : Membuat fungsi update data
#==========================================================
def update_data(data_dict):
    #Mulai dengan mencari data mahasiswa
    nim = input("Masukkan NIM Mahasiswa yang akan diubah datanya: ").strip()
    if nim not in data_dict:
        print("Data tidak ditemukan. Update dibatalkan")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru 0-100 : "))
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus 0 - 100. Update dibatalkan")
    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru
    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#update_data(open_file)

#==========================================================
#Praktikum 2 : Konsep ADT dan File Handing (STUDI KASUS)
#Latihan   5 : Membuat fungsi menyimpan data
#==========================================================
def save_data(file_path, data_dict):
    with open(file_path, 'w', encoding='utf-8') as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim}, {nama}, {int(nilai)}\n")

#save_data(file_path, open_file)
#print("\nData berhasil disimpan ke file: ", file_path)

#==========================================================
#Praktikum 2 : Konsep ADT dan File Handing (STUDI KASUS)
#Latihan   6 : Membuat menu interaktif
#==========================================================

def main():
    #load otomatis saat program dimulai
    open_file = read_file(file_path) #fs.1 fungsi load data
    while True:
        print("\n===== MENU DATA MAHASISWA =====")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Berdasarkan NIM")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Simpan Data ke File")
        print("0. Keluar")

        choice = input("Pilih Menu: ").strip

        if choice == "1":
            show_file(open_file)
        elif choice == "2":
            search_data(open_file)
        elif choice == "3":
            update_data(open_file)
        elif choice == "4":
            save_data(file_path, open_file)
            print("Data Berhasil Disimpan")
        elif choice == "0":
            print("Program Berakhir")
            break
        else :
            print("Input tidak valid")

if __name__ == "__main__":
    main()