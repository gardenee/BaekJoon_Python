n = int(input())
squares = [i**2 for i in range(1, 224)]
answer = 4

if n in squares:
    answer = 1
else:
    temp = []
    for i in range(len(squares)):
        if n < squares[i]:
            break
        temp.append(n-squares[i])
        if n-squares[i] in squares:
            answer = 2
            break
    if answer == 4:
        for i in range(len(temp)):
            for j in range(len(squares)):
                if squares[j] > temp[i]:
                    break
                if temp[i]-squares[j] in squares:
                    answer = 3
                    break
            if answer != 4:
                break

print(answer)
