for _ in range(int(input())):
    N = int(input())
    if str(N ** 2)[-len(str(N)):] == str(N):
        print('YES')
    else:
        print('NO')