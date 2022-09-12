x = ''
N = str(input())

for i in range(len(N)):
    x += str(int(N[i])//4) + str((int(N[i])%4)//2) + str((int(N[i])%4)%2)

print(int(x))