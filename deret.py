print("bilangan deret\n")
print("3,7,11,15,..,un\n")

def un(a,n,b):
    nilai = a+((n-1)*b)
    return nilai

def sn(a,n,b):
    total = (n/2)*(a+un(a,n,b))
    return total
# berapa nilai suku ke n dari n = 10
a = un(3,10,4)
print(a)

# berapa jumlah total suku ke n(n=10)
b = sn(3,10,4)
print(b)
