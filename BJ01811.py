while True:
    try:
        T, G = input().split()
        G2 = G
        T = list(T); G = list(G)

        b=0; g=0; w=0

        for i in range(len(G)):
            if G[i] == T[i]:
                b += 1
                T[i] = '!'; G[i] = '*'

        for i in range(len(G)):
            if i != 0 and G[i] == T[i-1]:
                g += 1
                T[i-1] = '!'; G[i] = '*'
            if i != len(G)-1 and G[i] == T[i+1]:
                g += 1
                T[i+1] = '!'; G[i] = '*'

        for i in G:
            if i in T:
                w += 1
                T[T.index(i)] = '!'

        print((G2+':'), b, 'black,', g, 'grey,', w, 'white')

    except:
        break
