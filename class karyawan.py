class Karyawan:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan
    
    def bekerja(self):
        print(f"{self.nama} sekarang bekerja")
    
    def istirahat(self):
        print(f"{self.nama} sekarang istirahat")

karyawan1 = Karyawan("Raka", "Manager")
karyawan2 = Karyawan("Sasa", "Staff")

karyawan1.bekerja()
karyawan1.istirahat()

karyawan2.bekerja()
karyawan2.istirahat()
