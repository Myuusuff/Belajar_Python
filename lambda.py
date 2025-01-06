# x = lambda a : a + 10
# print(x(5))


# def fungsi(n):
#     return lambda a : a * n


# angka1 = int(input("Masukkan Angka: "))
# angka2 = int(input("Masukkan Angka: "))


# hasil1 = fungsi(angka1)
# hasil2 = hasil1(angka2)

# print("hasil: ",hasil2 )


# def myfunc(a,b):
#     hasil = a + b
#     return hasil

# a = int(input("Masukkan Angka: "))
# b = int(input("Masukkan Angka: "))

# print("Hasil: ", myfunc(a,b))
    
def pembagian(a):
    return lambda b : b / a

angka1 = int(input("Masukkan Angka: "))
angka2 = int(input("Masukkan Angka: "))

hasil1 = pembagian(angka1)
hasil2 = hasil1(angka2)

print("Hasil: ", hasil2)