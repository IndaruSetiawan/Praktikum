class DaftarNilai:
    
    def __init__(self):
        self.data_mahasiswa = {}
        
    def tambah(self):
        print("Tambah Data")
        nim = input("NIM :")
        nama = input("Nama :")
        nilai_tugas = float(input("Nilai Tugas :"))
        nilai_uts = float(input("Nilai UTS :"))
        nilai_uas = float(input("Nilai UAS :"))
            
        nilai_akhir = (nilai_tugas * 0.30) + (nilai_uts * 0.35) + (nilai_uas * 0.35)
            
        self.data_mahasiswa[nama] = {
            'nim' : nim,
            'nama' : nama,
            'tugas' : nilai_tugas,
            'uts' : nilai_uts,
            'uas' : nilai_uas,
            'akhir' : nilai_akhir
        }
        print("Data Berhasil Ditambahkan!")
    
    def tampilkan(self):
        print("\n" + "="*78)
        print(f"| {'No':^3} | {'Nama':^15} | {'NIM':^10} | {'Tugas':^7} | {'UTS':^7} | {'UAS':^7} | {'Akhir':^7} |")
        print("="*78)

        count = 0
        for nama in self.data_mahasiswa :
            count = count + 1
            print(f"|{count:^4} | {self.data_mahasiswa[nama]['nama']:<15} | {self.data_mahasiswa[nama]['nim']:^10} | {self.data_mahasiswa[nama]['tugas']:^7.1f} | {self.data_mahasiswa[nama]['uts']:^7.2f} | {self.data_mahasiswa[nama]['uas']:^7.2f} | {self.data_mahasiswa[nama]['akhir']:^7.2f} |")
        print("="*78)
        
    def hapus(self):
        print("Hapus Data")
        nama = input("Masukan Nama yang ingin dihapus :")
        
        if nama in self.data_mahasiswa:
            print(f"Data dengan {self.data_mahasiswa[nama]['nama']} berhasil ditemukan!")
            del self.data_mahasiswa[nama]
            print("Data Berhasil Dihapus!")
        else:
            print(f"Data dengan {nama} tidak dapat ditemukan!")
            
    def ubah(self):
        print("Ubah Data")
        nama = input("Masukan Nama yang ingin diubah :")
        
        if nama in self.data_mahasiswa:
            print(f"Data dengan {self.data_mahasiswa[nama]['nama']} berhasil ditemukan!")
            print("Data yang akan diubah :")
            nilai_tugas = float(input("Nilai Tugas :"))
            nilai_uts = float(input("Nilai UTS :"))
            nilai_uas = float(input("Nilai UAS :"))
                
            nilai_akhir = (nilai_tugas * 0.30) + (nilai_uts * 0.35) + (nilai_uas * 0.35)
                
            self.data_mahasiswa[nama] = {
                'nim' : self.data_mahasiswa[nama]['nim'],
                'nama' : nama,
                'tugas' : nilai_tugas,
                'uts' : nilai_uts,
                'uas' : nilai_uas,
                'akhir' : nilai_akhir
            }
            print("Data Berhasil Diubah!")
        else:
            print(f"Data dengan {nama} tidak dapat ditemukan!")
            
def menu():
    
    daftar = DaftarNilai(
        
    )
    while True:
        print("Program Input Nilai")
        print("="*19)
        print("Menu")
        print("1. Tambah")
        print("2. Tampilkan")
        print("3. Hapus")
        print("4. Ubah")
        print("5. Keluar")
        pilih = input("Pilih Menu :")
            
        if pilih == '1':
            daftar.tambah()
        elif pilih == '2':
            daftar.tampilkan()
        elif pilih == '3':
            daftar.hapus()
        elif pilih == '4':
            daftar.ubah()
        elif pilih == '5':
            break
        else:
            print("Perintah tidak ditemukan!")
        
if __name__ == "__main__":
    menu()

    