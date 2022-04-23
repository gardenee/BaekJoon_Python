ref = dict()
ref[0] = [10]
ref[1] = [1]
ref[2] = [2, 4, 8, 6]
ref[3] = [3, 9, 7, 1]
ref[4] = [4, 6]
ref[5] = [5]
ref[6] = [6]
ref[7] = [7, 9, 3, 1]
ref[8] = [8, 4, 2, 6]
ref[9] = [9, 1]

for _ in range(int(input())):
    a, b = map(int, input().split())
    x = list(ref[a % 10])
    print(x[b % (len(x)) - 1])
