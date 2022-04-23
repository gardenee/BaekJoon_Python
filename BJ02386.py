from sys import stdin
while True:
    line = stdin.readline()
    if line[0] == '#':
        break
    else:
        word = line[0]
        print(word, line[2:].count(word)+line[2:].count(word.upper()))
