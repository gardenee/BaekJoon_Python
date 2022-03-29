def hanoi(N):
    if N == 1:
        return [['1', '3']]
    else:
        way = hanoi(N-1)
        way2 = hanoi(N-1)
        for i in range(len(way)):
            for j in range(2):
                if way[i][j] == '2':
                    way[i][j] = '3'
                elif way[i][j] == '3':
                    way[i][j] = '2'
        way.append(['1', '3'])
        for i in range(len(way2)):
            for j in range(2):
                if way2[i][j] == '1':
                    way2[i][j] = '2'
                elif way2[i][j] == '2':
                    way2[i][j] = '1'
        way += way2
        return(way)


ans = hanoi(int(input()))
print(len(ans))
for i in ans:
    print(' '.join(i))
