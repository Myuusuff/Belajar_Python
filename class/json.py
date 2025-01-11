import json

#beberapa JSON

x = '{ "nama": "Yusuf", "Umur" : "18", "Kota" : "Makassar"}'

#menguraikan x 
y = json.loads(x) # fungsi json.loads untuk menguraikan

print(y["umur"]) #mencetak hasil dari daftar pustaka x

#konversi dari python ke json
#json.dumps() untuk mengubah jadi string

x = {
    "nama" : "yusuf",
    "umur" : 18,
    "kota" : "Makassar"
}
#konversi ke json
y = json.dumps(x)

#hasil dari sebuah json string:
print(y)

