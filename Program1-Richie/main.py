from data.mahasiswa import Mahasiswa
from  view.input_form import InputForm
from view.mahasiswa import TampilMahasiswa

def main():
    mahasiswa = Mahasiswa()  # Membuat objek dari kelas Mahasiswa

    while True:
        print("\nMenu:")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            nama, nilai = InputForm.input_data()
            mahasiswa.tambah(nama, nilai)
        elif pilihan == '2':
            TampilMahasiswa.tampilkan_list(mahasiswa)
        elif pilihan == '3':
            nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
            mahasiswa.hapus(nama)
        elif pilihan == '4':
            nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
            nilai_baru = input("Masukkan nilai baru: ")
            mahasiswa.ubah(nama, nilai_baru)
        elif pilihan == '5':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
