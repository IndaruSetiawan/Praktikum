nilai = [80, 90, 'A', 70, 100, 'B']

total_nilai = 0
jumlah_valid = 0

for item in nilai:
    try:
        angka = float(item)
        total_nilai += angka
        jumlah_valid += 1
        print(f"{item} - valid")
        
    except ValueError, TypeError:
        print(f"{item} - dilewati, karna bukan angka")

if jumlah_valid > 0:
    rata_rata = total_nilai / jumlah_valid
    print(f"Total nilai valid: {total_nilai}")
    print(f"Jumlah data valid: {jumlah_valid}")
    print(f"Rata - rata nilai : {rata_rata:.2f}")
