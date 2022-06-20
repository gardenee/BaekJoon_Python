def gcf(a, b):
    temp = b
    b = a % b
    a = temp
    if b == 0: return a
    else: return gcf(a, b)


a, b = map(int, input().split())
A = max(a, b)
B = min(a, b)

GCF = gcf(A, B)
LCM = A * B // GCF

print(GCF)
print(LCM)
