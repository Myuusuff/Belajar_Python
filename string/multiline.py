# bisa menggunakan kutip tunggal dan ganda
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.\n"""

x ='''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.\n'''

print(a)
print(x)

# sring adalah array

# contoh:
a = "Hello, Kawan"
print("ini adalah string",a[0],"\n")

# looping melalui string
# ulangi huruf huruf dengan kata pisang:
# contoh

for x in "Pisang\n":
    print(x)

# Panjang Tali / string lenght
# Untuk mendapatkan panjang tali/string lenght gunaka len()
# fungsi len() mengembalikkan panjang string contoh:
# dan spasi juga ikut terhitung!

a = "Haii, Teman!\n"
print(len(a))

# periksa tali 
# untuk memeriksa apakah frase atau karakter tertentu ada        # didalam sebuah string, kita dapat menggunakan kata kunci in.
# contoh
# txt adalah string

# true
txt = "Yang terbaik dalam hidup anda adalah kebebasan!\n"
print("kebebasan" in txt) # periksa apakah kebebasan ada dalam teks jika ada maka keluar true

# true
txt = "Yang tebaik dalam hidup anda adalah kebebasan!\n"
print("kekayaan" not in txt) #periksa apakah kekayaan tidak ada dalam teks jika ada maka truee

# false
txt = "Yang tebaik dalam hidup anda adalah kebebasan!\n"
print("besar" in txt) # periksa apakah kata besar ada dalam teks tersebut jika tidak maka false

# false
txt = "Yang tebaik dalam hidup anda adalah kebebasan!\n"
print("hidup" not in txt) #periksa apakah kata hidup tidak ada dalam teks tersebut jika tidak maka false


# Gunakan dalam if pernyataan:
txt = "Keterbatasan hanya ada dalam pikiran!\n"
if "pikiran" in txt:
    print("iya,dengan berpikir masa depan terang")

txt = "Yang tebaik dalam hidup anda adalah kebebasan!\n"
if "gelas" not in txt:
    print("tidak,karena kata gelas tidak ada dalam teks ")






