num = list(str(input()))
num = list(map(int, num))
num.sort(reverse=True)
num=list(map(str, num))
print(''.join(num))