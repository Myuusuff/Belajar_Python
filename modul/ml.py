# mengubah modul dengan singkatan md
import modul as md     

# mengambil dari data modul lalu ambil bagian orang1 
from modul import orang1
from modul import orang2
from modul import orang3


#mencetak yang di panggil pada modul 
print("Hasil yang keluar :",orang1["nama"],orang2["nama"],orang3["nama"])

#mencetak dengan menggunakan singkatan md lalu memanggil dat dari modu
a = md.orang1["nama"]
md.perkenalan(md.orang3["nama"])
md.perkenalan(md.orang2["nama"])
# md.perkenalan("nama saya ",md.orang2["umur"])
print("hasilnya :",a)


a = int(input("Masukkan angka : "))
b = int(input("masukkan pangkat :"))

md.kuadrat(a,b)





