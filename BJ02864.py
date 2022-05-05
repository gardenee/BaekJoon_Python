A, B = map(str, input().split())

Amin = int(A.replace("6", "5"))
Amax = int(A.replace("5", "6"))
Bmin = int(B.replace("6", "5"))
Bmax = int(B.replace("5", "6"))

print(Amin+Bmin, Amax+Bmax)
