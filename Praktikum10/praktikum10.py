def validasi_nama(nama):
    if not nama:
        return False, "Nama tidak boleh kosong"

    for char in nama:
        if not char.isalpha() and char != ' ':
            return False, "Nama harus hanya berisi huruf"
    
    return True, "Nama Valid"

def validasi_nomor(nomor):
    if not nomor:
        return False, "Nomor telepon tidak boleh kosong"

    for char in nomor:
        if not char.isdigit():
            return False, "Nomor harus hanya berisi angka"
    return True, "Nomor Telepon Valid"

def validasi_email(email):
    if not email:
        return False, "Email tidak boleh kosong"

    if '@' not in email or "." not in email:
        return False, "Email harus mengandung karakter @ dan ."

    return True, "Email Valid"

def main():
    nama = input("Masukan Nama Lengkap: ")
    nomor = input("Masukan Nomor Telepon: ")
    email = input("Masukan Email: ")

    valid_nama, msg_nama = validasi_nama(nama)
    valid_nomor, msg_nomor = validasi_nomor(nomor)
    valid_email, msg_email = validasi_email(email)

    validasi_list = [
        ('Nama', valid_nama, msg_nama),
        ('Nomor Telepon', valid_nomor, msg_nomor),
        ('Email', valid_email, msg_email)
    ]

    semua_valid = True
    errors = []

    for field, is_valid, message in validasi_list:
        if not is_valid:
            semua_valid = False
            errors.append(f"{field}: {message}")
    
    if semua_valid:
        print("\n✓ Data pendaftaran valid")

    else:
        print("\nData pendaftaran tidak valid!")
        print("\nKesalahan yang ditemukan:")
        for i, error in enumerate(errors):
            print(f"{i}. {error}")

if __name__ == "__main__":
    main()
