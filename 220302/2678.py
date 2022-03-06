for _ in range(int(input())):
    P = ''
    R, S = input().split()
    for i in range(len(S)):
        P += S[i] * int(R)

    print(P)