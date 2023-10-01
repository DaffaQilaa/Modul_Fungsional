# Inisialisasi daftar peserta dan id awal
peserta = []
id_peserta = 0


# Fungsi untuk menambahkan peserta baru oleh admin
def tambah_peserta():
    global id_peserta
    nama = input("Masukkan Nama Peserta: ")
    nilai = int(input("Masukkan Nilai Peserta: "))
    hasil_akhir = "Lolos" if nilai >= 75 else "Tidak Lolos"
    peserta.append(
        {"ID": id_peserta, "Nama": nama, "Nilai": nilai, "Hasil Akhir": hasil_akhir}
    )
    id_peserta += 1
    print("Peserta berhasil ditambahkan!")


# Fungsi untuk mengedit nilai peserta oleh admin
def edit_nilai(id_peserta):
    for p in peserta:
        if p["ID"] == id_peserta:
            nilai_baru = int(input("Masukkan Nilai Baru: "))
            p["Nilai"] = nilai_baru
            p["Hasil Akhir"] = "Lolos" if nilai_baru >= 75 else "Tidak Lolos"
            print("Nilai berhasil diubah!")
            return
    print("ID Peserta tidak ditemukan.")


# Fungsi untuk menampilkan nilai dan hasil akhir peserta oleh peserta
def tampilkan_nilai_dan_hasil(id_peserta):
    for p in peserta:
        if p["ID"] == id_peserta:
            print(f"Nama: {p['Nama']}")
            print(f"Nilai: {p['Nilai']}")
            print(f"Hasil Akhir: {p['Hasil Akhir']}")
            return
    print("ID Peserta tidak ditemukan.")


# Main program
while True:
    print("\nSelamat datang di Aplikasi Pendaftaran Peserta")
    print("1. Admin - Tambah Peserta")
    print("2. Admin - Edit Nilai Peserta")
    print("3. Peserta - Tampilkan Nilai dan Hasil")
    print("4. Keluar")
    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "1":
        tambah_peserta()
    elif pilihan == "2":
        id_peserta = int(input("Masukkan ID Peserta yang akan diedit: "))
        edit_nilai(id_peserta)
    elif pilihan == "3":
        id_peserta = int(input("Masukkan ID Peserta Anda: "))
        tampilkan_nilai_dan_hasil(id_peserta)
    elif pilihan == "4":
        print("Terima kasih! Sampai jumpa.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
