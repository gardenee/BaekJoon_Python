for _ in range(int(input())):
    sentence = list(input().split())

    for word in sentence:
        for letter in word[::-1]:
            print(letter, end="")
        print(" ", end="")
    print()
