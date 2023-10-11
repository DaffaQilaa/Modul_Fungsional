data_user = {}
buku_tersedia = []


def tambah_buku():
    judul = input("Masukkan Judul Buku: ")
    penulis = input("Masukkan Nama Penulis: ")
    buku_tersedia.append({"Judul": judul, "Penulis": penulis})
    print("Buku berhasil ditambahkan!")


def tampilkan_buku_tersedia():
    print("\nBuku yang tersedia:")
    for idx, buku in enumerate(buku_tersedia):
        print(f"{idx + 1}. Judul: {buku['Judul']}, Penulis: {buku['Penulis']}")


def pinjam_buku(username):
    tampilkan_buku_tersedia()
    pilihan = int(input("Pilih nomor buku yang ingin dipinjam: ")) - 1

    if pilihan >= 0 and pilihan < len(buku_tersedia):
        buku_dipinjam = buku_tersedia[pilihan]

        # Periksa apakah buku sudah dipinjam oleh pengguna lain
        is_buku_dipinjam = False
        for user, buku_user in data_user.items():
            if any(buku["Judul"] == buku_dipinjam["Judul"] for buku in buku_user):
                is_buku_dipinjam = True
                break

        if is_buku_dipinjam:
            print(f"Buku '{buku_dipinjam['Judul']}' sudah dipinjam oleh pengguna lain.")
        else:
            buku_tersedia.pop(pilihan)
            if username not in data_user:
                data_user[username] = [buku_dipinjam]
            else:
                data_user[username].append(buku_dipinjam)
            print(f"Anda berhasil meminjam buku '{buku_dipinjam['Judul']}'!")
    else:
        print("Nomor buku tidak valid.")


def kembalikan_buku(username):
    if username in data_user:
        if len(data_user[username]) > 0:
            buku_dikembalikan = data_user[username].pop()
            buku_tersedia.append(buku_dikembalikan)
            print(f"Anda telah mengembalikan buku '{buku_dikembalikan['Judul']}'!")
        else:
            print("Anda belum meminjam buku.")
    else:
        print("Anda belum meminjam buku.")


def tampilkan_data_user():
    print("\nData User:")
    for username, buku in data_user.items():
        print(f"Nama: {username}")
        print(f"Jumlah Buku yang Dipinjam: {len(buku)}")
        if len(buku) > 0:
            print("Buku yang Dipinjam:")
            for idx, buku_dipinjam in enumerate(buku):
                print(
                    f"{idx + 1}. Judul: {buku_dipinjam['Judul']}, Penulis: {buku_dipinjam['Penulis']}"
                )


while True:
    print("\nMenu:")
    print("1. Admin - Tambah Buku")
    print("2. User - Pinjam Buku")
    print("3. User - Kembalikan Buku")
    print("4. Tampilkan Data User")
    print("5. Tampilkan Buku yang Tersedia")
    print("6. Keluar")
    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "1":
        tambah_buku()
    elif pilihan == "2":
        username = input("Masukkan Nama Anda: ")
        pinjam_buku(username)
    elif pilihan == "3":
        username = input("Masukkan Nama Anda: ")
        kembalikan_buku(username)
    elif pilihan == "4":
        tampilkan_data_user()
    elif pilihan == "5":
        tampilkan_buku_tersedia()
    elif pilihan == "6":
        print("Terima kasih! Sampai jumpa.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
