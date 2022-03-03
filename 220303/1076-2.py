color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
ref = dict()

for i, c in enumerate(color):
    ref[c] = i

print((10 * ref[input()] + ref[input()]) * 10 ** ref[input()])
