# metode objek
#metode dalam objek adalah fungsi yang dimiliki objek tersebut
#class tidak boleh kosong, tetapi jika ingin mengosongkan class bisa menggunakan kata pass

# class orang:
    # pass 

x = str(input("Masukkan Nama : "))
y = str(input("Masukkan Umur : "))

class orang:
    def __init__(data, nama, umur):
        data.nama = nama
        data.umur = umur
        
    def myfunc(data):
        print(" Hallo nama saya " + data.nama,"\n","Umur saya ", data.umur)


p1 = orang(x,y)
p1.myfunc() 

# del p1.age  dapat menghapus pada objek

