ans = 0

for i in range(1, int(input())+1):
    if len(str(i)) < 3:
        ans += 1
    if len(str(i)) == 3:
        if (i//100)+((i%100)%10) == 2 * ((i%100)//10):
            ans +=1

print(ans)