def solution(width, height, diagonals):
    answer = 0
    for i in range(len(diagonals)):
        temp = []
        for y in range(diagonals[i][1]):
            temp.append([])
            for x in range(diagonals[i][0] + 1):
                temp[y].append(0)
        for y in range(len(temp)):
            temp[y][0] = 1
        for x in range(len(temp[0])):
            temp[0][x] = 1

        for y in range(1, len(temp)):
            for x in range(1, len(temp[0])):
                temp[y][x] = temp[y-1][x] + temp[y][x-1]
        temp1 = temp[-1][-1]

        temp = []
        for y in range(height - (diagonals[i][1]) + 1):
            temp.append([])
            for x in range(width - (diagonals[i][0]-1) + 1):
                temp[y].append(0)
        for y in range(len(temp)):
            temp[y][0] = 1
        for x in range(len(temp[0])):
            temp[0][x] = 1

        for y in range(1, len(temp)):
            for x in range(1, len(temp[0])):
                temp[y][x] = temp[y - 1][x] + temp[y][x - 1]
        temp2 = temp[-1][-1]

        answer += temp1 * temp2

        ##############################################################################################

        temp = []
        for y in range(diagonals[i][1] + 1):
            temp.append([])
            for x in range(diagonals[i][0]):
                temp[y].append(0)
        for y in range(len(temp)):
            temp[y][0] = 1
        for x in range(len(temp[0])):
            temp[0][x] = 1

        for y in range(1, len(temp)):
            for x in range(1, len(temp[0])):
                temp[y][x] = temp[y - 1][x] + temp[y][x - 1]

        temp1 = temp[-1][-1]

        temp = []
        for y in range(height - (diagonals[i][1] -1) + 1):
            temp.append([])
            for x in range(width - (diagonals[i][0]) + 1):
                temp[y].append(0)
        for y in range(len(temp)):
            temp[y][0] = 1
        for x in range(len(temp[0])):
            temp[0][x] = 1

        for y in range(1, len(temp)):
            for x in range(1, len(temp[0])):
                temp[y][x] = temp[y - 1][x] + temp[y][x - 1]

        temp2 = temp[-1][-1]

        answer += temp1 * temp2

    return answer % 10000019
