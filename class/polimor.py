# input 

nama = str(input("Masukkan Nama : "))
mmobil = str(input("Masukkan Merek mobil : "))
umobil = float(input("Masukkan Ukuran Mobil : "))
mrumah = str(input("Masukkan Nama Rumah :"))
urumah = float(input("Masukkan Ukuran : "))


class fungsi():
    def __init__(data, merek,ukuran):
        data.merek = merek
        data.ukuran = ukuran
        
    def move(data):
        print(nama)


class mobil(fungsi):
    def move(data):
        print(mmobil,umobil)

class rumah(fungsi):
    def move(data):
        print(mrumah,urumah)


oto = mobil(mmobil,umobil)
balla = rumah(mrumah,urumah)

for x in (oto,balla):
    print(x.merek)
    print(x.ukuran)
    x.move


    
