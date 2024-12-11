class Mahasiswa:
    """Kelas untuk merepresentasikan daftar mahasiswa."""

    def __init__(self):
        self.daftar_mahasiswa = []

    def tambah(self, nama, nilai):
        """Menambah data mahasiswa."""
        self.daftar_mahasiswa.append({'nama': nama, 'nilai': nilai})
        print(f"Data mahasiswa {nama} berhasil ditambahkan.")

    def tampilkan(self):
        """Menampilkan data mahasiswa dalam format tabel."""
        if not self.daftar_mahasiswa:
            print("Tidak ada data mahasiswa.")
            return
        print("+-------+-------+")
        print("|  Nama | Nilai |")
        print("+-------+-------+")
        for mhs in self.daftar_mahasiswa:
            print(f"|  {mhs['nama']: <5} |  {mhs['nilai']: <5} |")
        print("+-------+-------+")

    def hapus(self, nama):
        """Menghapus data mahasiswa berdasarkan nama."""
        self.daftar_mahasiswa = [mhs for mhs in self.daftar_mahasiswa if mhs['nama'] != nama]
        print(f"Data mahasiswa {nama} berhasil dihapus.")

    def ubah(self, nama, nilai_baru):
        """Mengubah data mahasiswa berdasarkan nama."""
        for mhs in self.daftar_mahasiswa:
            if mhs['nama'] == nama:
                mhs['nilai'] = nilai_baru
                print(f"Data mahasiswa {nama} berhasil diubah menjadi nilai {nilai_baru}.")
                return 
        print(f"Data mahasiswa {nama} tidak ditemukan.")
