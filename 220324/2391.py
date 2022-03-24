for _ in range(int(input())):
    word = input()
    count = {}
    for _ in range(int(input())):
        w = input()
        count[w] = 0
        for i in range(len(word)):
            if word[i] != w[i]:
                count[w] += 1
    for k, v in count.items():
        if min(count.values()) == v:
            print(k)
            break
