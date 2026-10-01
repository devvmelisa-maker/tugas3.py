class Hewan:
    def __init__(self, nama, usia):
        self.nama = nama
        self. usia = usia
    def makan(self) : 
        print(f"{self.nama} makan.")
    def info(self) : 
        print(f"{self.nama} ({self.usia} th)")

class Ular(Hewan):
    def __init__(self,nama,usia, jenis):
        super().__init__(nama,usia)
        self.jenis = jenis
    def mendesis(self):
        return f'{self.nama}: Ssssttttt....'

class Kuda(Hewan):    
    def __init__ (self, nama, usia):
        super().__init__(nama,usia)
    def suara(self):
        return f'{self.nama}: ihaaaak...'

class Buaya(Hewan):
    def __init__(self, nama, usia):
        super().__init__(nama, usia)
    def suara(self):
        return f"{self.nama}: Hai Sayang, kalo aku chat ada yang marah gak?"

u = Ular("Hebi",2, "panjang")
k = Kuda("Max", 5)
b = Buaya("Kimmy","4")

# Ular
u.makan()
u.info()
print(u.mendesis())
print(u.jenis)

# Kuda
k.makan()
k.info()
print(k.suara())

# Buaya
b.makan()
b.info()
print(b.suara())
print(b.usia)