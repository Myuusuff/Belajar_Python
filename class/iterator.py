#menginput data iteror

a = str(input("Masukkan Nama : "))
b = str(input("Masukkan Alamat : "))
c = str(input("Masukkan Hoby : "))

tuple = a,b,c

for x in tuple :
    print(len(x))  # fungsi len() menghitung jumlah karakter

#iterator adalah objek yang berisi nilai yang bisa dihitung
#fungsi __iter()__ & __next()__ harus selalu mengambalikan objek iterator itu sendiri
# dengan menggunakan return
    

z = int(input("Masukkan Nilai : "))
class nomor:
    def __iter__(data):
        data.a = 1
        return data
    
    def __next__(data):
        if data.a <= z :
            x = data.a 
            data.a += 1
            return x
        else: 
            raise StopIteration

classku = nomor()
iteratorku = iter(classku)
for x in iteratorku :
    print(x)

