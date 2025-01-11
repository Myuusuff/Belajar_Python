#fungsi lambda dapat menerima sejumlah argumen:

print("\n")
y = lambda a : a + 10
print(y(4),"\n")


a = int(input("Masukkan Angka : "))
b = int(input("Masukkan Angka : "))


x = lambda a,b : a * b
print(x(a,b),"\n")


y = str(input("Masukkana nama depan : "))
z = str(input ("Masukkan nama belakang : "))

def fungsi(a):
    return lambda b : b + a

kedua = fungsi(z)
print(kedua(y),"\n")









