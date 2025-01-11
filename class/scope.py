# ruang lingkup
def lokal(): #fungsi lokal
    x = 300
    print(x)

lokal()

#fungsi dalam fungsi
n = int(input("Masukkan Nilai : "))
def luarfungsi():
    x = n
    def dalamfungsi():
        print(x)
    dalamfungsi()

luarfungsi()


# global
a = int(input("Masukkan Nilai : "))
x = a
def global1():
    print(x)

global1() #membuat variabel luar bersifat global dapat di gunakan siapa saja
        #contohnya memanggil global1() dan print(x) yg ada dalam fungsi

print(x) 


#  penamaan variabel
a = int(input("Masukkan Nilai a : "))
b = int(input("Masukkan Nilai b : "))
x = b
def globalluar():
    x = a
    print("Nilai a : ",x)

globalluar() #mencetak nilai a

print("Nilai b : ",x) #mencetak nilai b

#cara kerja dari mencetak fungsi globalluar lalu mencetak 
#cetak print b

#menggunakan kata kunci global untuk 
#membuat perubahan daalam variabel di dalam suatu fungsi
# input1 = int(input("Masukkan nilai 1: "))
# input2 = int(input("Masukkan Nilai 2: "))

nilai1 = 300

def fungsi():
    global nilai1
    nilai1 = 200

fungsi()
print(nilai1)


