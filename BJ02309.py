data = []
for _ in range(9):
    data.append(int(input()))
data.sort()
dif = sum(data) - 100
for i in range(8):
    j = 1
    while i + j < 9:
        if dif == data[i] + data[i+j]:
            data.pop(i+j)
            data.pop(i)
            break
        j += 1
    if len(data) == 7:
        break

for i in data:
    print(i)
