n = int(input())
switch = list(map(int, input().split()))

for _ in range(int(input())):
    sex, no = map(int, input().split())
    if sex == 1:
        i = 1
        while no * i - 1 < n:
            switch[no*i-1] = abs(switch[no*i-1]-1)
            i += 1
    elif sex == 2:
        switch[no-1] = abs(switch[no-1]-1)
        i = 1
        while 1 <= no-i and no+i < n+1 and switch[no-i-1] == switch[no-1+i]:
            switch[no-1-i] = abs(switch[no-1-i]-1)
            switch[no-1+i] = switch[no-1-i]
            i += 1

for i in range(n):
    print(switch[i], end=" ")
    if i%20 == 19:
        print()
