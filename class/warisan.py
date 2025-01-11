x = str(input("Masukkan Nama Depan : "))
y = str(input("Masukkan Nama Belakang : "))

class orang :
    def __init__(data, nade, nabe):
        data.namadepan = nade
        data.namabelakang = nabe

    def namalengkap(data):
        print(data.namadepan, data.namabelakang)


# memanggil fungsi harus dengan menggunakan variabel awal


class Murid(orang):
    pass 

a = orang(x,y) 
a.namalengkap()
