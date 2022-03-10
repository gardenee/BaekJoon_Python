for _ in range(int(input())):
    trash = input()
    N, M = map(int, input().split())

    S = list(map(int, input().split()))
    B = list(map(int, input().split()))
    S.sort(); B.sort()

    while len(S) != 0 and len(B) != 0:
        if S[0] >= B[0]:
            B.pop(0)
        else:
            S.pop(0)

    if len(S) > len(B):
        print('S')
    elif len(B) > len(S):
        print('B')
    else:
        print('C')
