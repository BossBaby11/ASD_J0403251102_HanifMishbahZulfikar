# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
# Nama  : Hanif Mishbah Zulfikar
# NIM   : J0403251102
# Kelas : A2
# ==========================================================
# -------------------------------
# Konstanta nama file
# -------------------------------
stock_file = "./Praktikum2/data_barang.txt" #memberikan variable pada path penyimpanan data yang berformat txt
# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def read_stock(stock_file):
# """Membaca data stok dari file teks.
# Format per baris: KodeBarang,NamaBarang,Stok
# Output:
# - stok_dict (dictionary)
# key = kode_barang
# value = {"nama": nama_barang, "stok": stok_int}
# """    
    stock_dict = {}# deklarasi dictionary untuk data pada file penyimpanan
# TODO: Buka file dan baca seluruh baris
# Hint: with open(nama_file, "r", encoding="utf-8") as f:
# TODO: Untuk setiap baris:
# - gunakan strip() untuk menghilangkan \n
# - split(",") untuk memisahkan kolom
# - simpan ke dictionary
    with open(stock_file, 'r', encoding='utf-8') as f: #akses file penyimpanan dengan metode read
        for baris in f: #looping untuk memasukkan data dari file penyimpanan ke dictionary satu-persatu
            baris = baris.strip() #menghilangkan spacebar pada data
            kode, nama, stok = baris.split(",") #menghilangkan tanda koma dari format data dalam file penyimpanan
            stock_dict[kode]={"nama": nama, "stok": int(stok)} #format data pada dictionary
        return stock_dict

# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def save_stock(stock_file, stock_dict): 
# """
# Menyimpan seluruh data stok ke file teks.
# Format per baris: KodeBarang,NamaBarang,Stok
# """
# TODO: Tulis ulang seluruh isi file berdasarkan stok_dict
# Hint: with open(nama_file, "w", encoding="utf-8") as f:
    with open(stock_file, 'w', encoding='utf-8') as f: #akses file penyimpanan dengan metode write
        for kode in sorted(stock_dict.keys()): # memastikan kode/id terdapat pada dictionary
            nama = stock_dict[kode]["nama"] #penulisan ulang data nama yang berasal dari dictionary
            stok = stock_dict[kode]["stok"] #penulisan ulang data stok yang berasal dari dictionary
            f.write(f"{kode}, {nama}, {stok}\n")
    pass

# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def show_all_stock(stock_dict):
# """
# Menampilkan semua barang di stok_dict.
# """
# TODO: Jika kosong, tampilkan pesan stok kosong
# TODO: Tampilkan dengan format rapi: kode | nama | stok
    print("\n====== DAFTAR STOK BARANG  KANTIN ======") #template header
    print(f"{'    KODE' : <10} | {'    NAMA' : <12} | {'JUMLAH STOK' : >5}") #formating header tiap item
    print("-" * 40) #Create Line
    #Show Dictionary Value
    for kode in sorted(stock_dict.keys()):
        nama = stock_dict[kode]["nama"].strip()
        stok = stock_dict[kode]["stok"]
        print(f"{kode: <10} | {nama: <12} | {int(stok): >12}") #formating isi dari tiap item
    pass

# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def search_stock(stock_dict):
# """
# Mencari barang berdasarkan kode barang.
# """
    search_code = input("Masukkan kode barang: ").strip().upper() #input user untuk kode data yang ingin dicari
# TODO: Cek apakah kode ada di dictionary
# Jika ada: tampilkan detail barang
# Jika tidak ada: tampilkan 'Barang tidak ditemukan'
    if search_code in stock_dict: #mengecek apakah kode terdapat pada dictionary
        nama = stock_dict[search_code]["nama"]
        stok = stock_dict[search_code]["stok"]
        #format template jika barang tidak ditemukan
        print("======  DATA BARANG DITEMUKAN =====")
        print(f"NIM   : {search_code}")
        print(f"Nama  : {nama}")
        print(f"Stok  : {stok}")
    else: #output jika barang tidak ditemukan
        print("Data tidak ditemukan. Pastikan KODE yang dimasukkan benar!!!")
    pass

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def add_stock(stock_dict, stock_file):
# """
# Menambah barang baru ke stok_dict.
# """
    kode = input("Masukkan kode barang baru: ").strip().upper() #input kode barang baru dari user
# TODO: Validasi kode tidak boleh duplikat
# Jika sudah ada: tampilkan 'Kode sudah digunakan' dan return
# TODO: Input stok awal (integer)
# Hint: stok_awal = int(input(...))
# TODO: Simpan ke dictionary
    if kode in stock_dict: #output jika kode sudah ada dalam dictionary
        print("Kode barang sudah digunakan, pastikan KODE yang anda masukkan belum digunakan!")
        return
    nama = input("Masukkan nama barang: ").strip() #input nama barang baru dari user
    check_name = [item["nama"].strip().lower() for item in stock_dict.values()] #variabel yang berisikan syntax untuk melakukan pengecekan apakah nama sudah tercantum dalam dictionary atau tidak
    if nama.lower() in check_name: #output jika nama sudah ada dalam dictionary
        print("Nama barang sudah digunakan, pastikan NAMA yang anda masukkan belum digunakan!")
        return
    #handler jika user inputan user untuk jumlah stok tidak berupa angka
    try:
        stok = int(input("Masukkan jumlah barang: "))
    except ValueError:
        print("Masukkan harus berupa ANGKA, silahkan coba lagi")
        return
    stock_dict[kode] = {"nama": nama, "stok": int(stok)} #format untuk memasukkan data barang terbaru ke dalam dictionary
    pass

# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stock(stock_dict):
# """
# Mengubah stok barang (tambah atau kurangi).
# Stok tidak boleh menjadi negatif.
# """
    kode = input("Masukkan kode barang yang ingin diupdate: ").upper().strip()
# TODO: Cek apakah kode ada di dictionary
# Jika tidak ada: tampilkan pesan dan return
    if kode not in stock_dict:
        print("Barang yang anda cari tidak ada pada daftar, pastikan anda memasukkan KODE dengan tepat!")
        return
    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")
# TODO: Input jumlah perubahan stok
# Hint: jumlah = int(input("Masukkan jumlah: "))
    try: 
        pilihan = int(input("Masukkan pilihan (1/2): "))
    except ValueError:
        print("Masukkan harus berupa angka silahkan coba kembali")
# TODO:
# - Jika pilihan 1: stok = stok + jumlah
# - Jika pilihan 2: stok = stok - jumlah
# - Jika hasil < 0: batalkan dan tampilkan error
    if pilihan == 1:
        try:
            add = int(input("Masukkan jumlah yang ingin ditambahkan: "))
        except ValueError:
            print("Masukkan harus berupa ANGKA, silahkan coba kembali!")
        # output jika jumlah penambahan = 0
        if add < 0:
            print("Angka harus lebih besar dari 0")
            return
        stok_awal = stock_dict[kode]["stok"] #deklarasi variabel dengan value yang akan ditambahkan jumlah stoknya melalui indikasi kode 
        stok_terbaru = stok_awal + add #menambah nilai stok awal dengan nilai pertambahan
        stock_dict[kode]["stok"] = stok_terbaru #jumlah stok baru
        print(f"Update berhasil. Nilai {kode} berubah dari {stok_awal} menjadi {stok_terbaru}") #notif berhasil
    elif pilihan == 2:
        try:
            minus = int(input("Masukkan jumlah yang ingin dikurangi: "))
        except ValueError:
            print("Masukkan harus berupa ANGKA, silahkan coba kembali!")
        if minus < 0:
            print("Angka harus lebih besar dari 0")
        stok_awal = stock_dict[kode]["stok"] #deklarasi variabel dengan value yang akan dikurangi jumlah stoknya melalui indikasi kode 
        stok_terbaru = stok_awal - minus #mengurangi nilai stok awal dengan nilai pengurangan
        #handler jika nilai akhir ternyata lebih kecil dari 0
        if stok_terbaru < 0: 
            print("Jumlah stok tidak boleh kurang dari 0. Perubahan dibatalkan")
        else: 
            stock_dict[kode]["stok"] = stok_terbaru #jumlah stok baru
            print(f"Update berhasil. Nilai {kode} berubah dari {stok_awal} menjadi {stok_terbaru}") #notif berhasil
    else:
        print("Pilih opsi dengan memasukkan angka antara 1 (menambah) atau 2(mengurangi)!")
        return
    pass

# -------------------------------
# Program Utama
# -------------------------------
def main():
# Membaca data dari file saat program mulai
    stok_barang = read_stock(stock_file)
    while True:
        print("\n=== MENU STOK BARANG ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        option = input("Pilih menu: ").strip()
        #output beruoa menunjukkan seluruh data yang ada pada dictionary
        if option == "1":
            show_all_stock(stok_barang)
        #output berupa pencarian item barang berdasarkan kode barang
        elif option == "2":
            search_stock(stok_barang)
        #output berupa menambahkan barang baru ke dalam dictionary
        elif option == "3":
            add_stock(stok_barang, stock_file)
        #output berupa memanipulasi jumlah stok barang
        elif option == "4":
            update_stock(stok_barang)
        #output berupa menyimpan data perubahan pada dictionary ke file penyimpanan
        elif option == "5":
            save_stock(stock_file, stok_barang)
            print("Data berhasil disimpan.")
        #program diberhentikan
        elif option == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()


