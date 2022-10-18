T = 0

while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0: break

    T += 1
    print("Case " + str(T) + ": " + str((V//P)*L + min(V%P, L)))
