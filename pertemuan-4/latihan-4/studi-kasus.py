#Data login yang benar
input_username = "cynienaputri"
input_password = "123"

#Jumlah percobaan login
percobaan = 0
maksimal_percobaan = 3

#Looping untuk percobaan login
while percobaan < maksimal_percobaan:
    try:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

#Cek apakah username dan password benar
        if username == input_username and password == input_password:
            print("Login berhasil!")
            break
        else:
            print("Username atau password salah!")
        percobaan += 1

#Menangani error jika password yg dimasukkan bukan angka
    except ValueError:
        print("Password harus berupa angka!")
        percobaan += 1

    finally:
        print("Percobaan ke-", percobaan)
        print("-" * 20)

#tanda jika percobaan login sudah ke batas maksimal dan gagal login
if percobaan == maksimal_percobaan:
    print("Silakan coba lagi nanti!")