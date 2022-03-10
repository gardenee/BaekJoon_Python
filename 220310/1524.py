for _ in range(int(input())):
    trash = input()
    N, M = map(int, input().split())

    S = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if max(S) < max(B):
        print('B')
    elif max(S) == max(B) and S.count(max(S)) < B.count(max(B)):
        print('B')
    else:
        print('S')
