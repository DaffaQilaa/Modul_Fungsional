# Fungsi untuk menghitung nilai akhir seorang mahasiswa
def hitung_nilai_akhir(uts, uas):
    return 0.4 * uts + 0.6 * uas

# Fungsi untuk menghitung semua nilai akhir mahasiswa
def hitung_semua_nilai_akhir(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        nilai_akhir = hitung_nilai_akhir(nilai['uts'], nilai['uas'])
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir

# Fungsi untuk menambahkan data mahasiswa ke dalam dictionary data_mahasiswa
def tambahkan_data_mahasiswa(nama, uts, uas, data_mahasiswa):
    data_mahasiswa[nama] = {'uts': uts, 'uas': uas}

# Program utama
def main():
    data_mahasiswa = {
        # Data mahasiswa (nama sebagai kunci dan nilai UTS serta UAS sebagai nilai dalam bentuk dictionary)
        'Mahasiswa1': {'uts': 85, 'uas': 90},
        'Mahasiswa2': {'uts': 70, 'uas': 80},
        'Mahasiswa3': {'uts': 60, 'uas': 75},
    }

    # Menghitung nilai akhir semua mahasiswa
    data_nilai_akhir = hitung_semua_nilai_akhir(data_mahasiswa)

    # Menampilkan hasil nilai akhir
    tampilkan_nilai_akhir(data_nilai_akhir)

def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

if __name__ == "__main__":
    main()
