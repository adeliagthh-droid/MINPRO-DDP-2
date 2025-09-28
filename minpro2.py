# Program CRUD Travel Log dengan Login & Role

# Data user (username: {password, role})
users = {
    "admin": {"password": "123", "role": "Manager"},
    "budi": {"password": "456", "role": "Karyawan"}
}

# Data Travel Log (id: {tujuan, tanggal, catatan})
travel_log = {
    1: {"tujuan": "Bali", "tanggal": "2025-01-12", "catatan": "Liburan keluarga"},
    2: {"tujuan": "Yogyakarta", "tanggal": "2025-03-05", "catatan": "Perjalanan bisnis"}
}

# ==== Fungsi CRUD ====
def read_log():
    if not travel_log:
        print("Belum ada catatan perjalanan.")
    else:
        print("\n=== Travel Log ===")
        for id_log, data in travel_log.items():
            print(f"{id_log} Tujuan: {data['tujuan']}, "
                  f"{data['tanggal']}, Catatan: {data['catatan']}")

def create_log():
    try:
        id_log = max(travel_log.keys(), default=0) + 1
        tujuan = input("Masukkan tujuan perjalanan: ")
        tanggal = input("Masukkan tanggal perjalanan (YYYY-MM-DD): ")
        catatan = input("Masukkan catatan: ")
        travel_log[id_log] = {"tujuan": tujuan, "tanggal": tanggal, "catatan": catatan}
        print("Catatan perjalanan berhasil ditambahkan!")
    except Exception as e:
        print("Terjadi kesalahan:", e)

def update_log():
    try:
        read_log()
        id_log = int(input("Masukkan ID perjalanan yang ingin diupdate: "))
        if id_log in travel_log:
            tujuan = input("Masukkan tujuan baru: ")
            tanggal = input("Masukkan tanggal baru (YYYY-MM-DD): ")
            catatan = input("Masukkan catatan baru: ")
            travel_log[id_log] = {"tujuan": tujuan, "tanggal": tanggal, "catatan": catatan}
            print("Catatan perjalanan berhasil diupdate!")
        else:
            print("ID tidak ditemukan!")
    except ValueError:
        print("Input harus berupa angka!")

def delete_log():
    try:
        read_log()
        id_log = int(input("Masukkan ID perjalanan yang ingin dihapus: "))
        if id_log in travel_log:
            del travel_log[id_log]
            print("Catatan perjalanan berhasil dihapus!")
        else:
            print("ID tidak ditemukan!")
    except ValueError:
        print("Input harus berupa angka!")

# ==== Fungsi Menu ====
def menu_manager():
    while True:
        print("\n=== MENU MANAGER (Travel Log) ===")
        print("1. Lihat Travel Log")
        print("2. Tambah Travel Log")
        print("3. Update Travel Log")
        print("4. Hapus Travel Log")
        print("5. Logout")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            read_log()
        elif pilihan == "2":
            create_log()
        elif pilihan == "3":
            update_log()
        elif pilihan == "4":
            delete_log()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid!")

def menu_karyawan():
    while True:
        print("\n=== MENU KARYAWAN (Travel Log) ===")
        print("1. Lihat Travel Log")
        print("2. Logout")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            read_log()
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid!")

# ==== Fungsi Login ====
def login():
    print("=== LOGIN SISTEM TRAVEL LOG ===")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print(f"Login berhasil! Selamat datang, {username} ({users[username]['role']})")
        return users[username]["role"]
    else:
        print("Username atau password salah!")
        return None

# ==== Main Program ====
while True:
    role = login()
    if role == "Manager":
        menu_manager()
    elif role == "Karyawan":
        menu_karyawan()