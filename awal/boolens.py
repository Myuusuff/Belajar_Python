#  Nilai boolean
# boolean mewakili salah satu false atau truee: false 0 sedangkan true 1

# contoh
a = 340
b = 90 
if b > a:
    print("Nilai b,lebih besar dari nilai a")
else:
    print("Nilai b,tidak lebih besar dari nilai a")


# Mengavaluasi Nilai dan Variable
# Fungsi bool() memungkinkan anda untuk mengevaluasi nilai apa pun, dan memberi anda
# true atau false sebagai imbalannya,

# contoh 
# Mengavaluasi string dan angka:

print(bool("Umur saya"))
print(bool(17))


# contoh 
# evaluasi dua variable
x = "Hello"
y = 17
print(bool(x))
print(bool(y))

# kebanykan nilai benar
# Hampir semua nilai dievakuasi true jika memiliki semacam konten 
# semua string true,kecuali string kosong
# setiap nomor true,kecuali 0
# Contoh
print(bool("abc"))
print(bool("123"))
print(bool(["appel,mangga,jeruk"]))


# beberapa nilai salah;
# faktanya,tidak banyak nilai yang dievakuasi ke false,
# Kecuali nilai kosong, seperti (),[],{},"",angka 0 dan nilai none. dan tentu saja nilainya 
# false dievaluasi menjadi false.
# contoh
print(bool(False))     # awal harus huruf besar
print(bool(None))      # ~
print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(()))





# false jika anda memiliki objek yg dibuat dari kelas dengan __len__ fungsi yang mengembalikkan 0 atau false

# contoh
class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print("Hasilnya",bool(myobj))



# fungsi dapt mengambalikkan boolean
def myFuntion():
    return True

print("Hasilnya",myFuntion())



# anda dapat mengeksekusi kode berdasarkan jawaban boolean dari suatu
# fungsi:

# cetak "Ya" jika fungsi mengambalikkan true, jika tidak, cetak "tidak"
def myFunction():
    return True 

if myFuntion():
    print("Yes!")
else:
    print("NO!")

# fungsi isinstance(), yanga dapat digunakan untuk menemukan apakah suatu objek bertipe data tertentu:

# periksa apakah suatu objek apakah bilangan bulat atau tidak:

x = 200
print("ini adalah bilangan bulat",isinstance(x, int))

y = 3.09
print("ini adalah bilangan pecahan",isinstance(y, float))