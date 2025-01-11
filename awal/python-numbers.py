# Angka python ada tiga
# int
# float
# complex

#contoh:

x = 10      #int
y = 3.0     #float
z = 2j      #complex

# Untuk memverifikasi jenis objek apapun dengan python, gunakan type() fungsi:

print(type(x))
print(type(y))
print(type(z))

# int adalah bilangan bulat,posit atau negatif tanpa desimal, dengan panjang tak terbatas contoh::

a = 1
b = 45789483972345628
c = -4576898

print(type(a))
print(type(b))
print(type(c))

# float adalah angka,positif atau negatif,yang akan mengandung satu atau lebih desimal, float juga bisa berupa bilangan ilmiah dengan huruf "e" untuk menujukkan pangkat 10
# contoh::

x = 1.90
y = 9.0
z = -45.90

print(type(x))
print(type(y))
print(type(z))

q = 36e9
w = 23e5
e = -45.7e102

print(type(q))
print(type(w))
print(type(e))


# complex/komplex
# Bilangan complex di tulis dengan "j" sebagai bagian imajiner:

m = 7+5j
y = 4j
j = -6j

print(type(m))
print(type(y))
print(type(j))



# ketik konversi
# konversi ke int float dan complex
# konversi dari satu dengan yang lainnya: contoh::

x = 2
y = 4.5
z =8j

# konversi dari int  ke float
a = float(x)

# konversi dari float ke int
b = int(y)

# konversi dari int ke complex
c = complex(x)

print(a)
print(b)
print(c)

print(type(a)) 
print(type(b))
print(type(c))

# angka acak 
# python tidak memiliki random() fungsi untuk membuat angka acak, tetapi python memiliki modul bawaan yang di sebut "random" yang dapat di gunakan untuk membuat angka acak 
# contoh
# impor modul acak, dan tampilkan nomor acak antara 1 sampai 9:
import random 
print("ini adalah nomor acak/random:",random.randrange(1,10))

