def function(line):
    l = len(line)
    if l <= 1:
        return line
    else:
        return function(line[:l//3]) + " " * (l//3) + function(line[-(l//3+1):])


while True:
    try:
        print(function("-" * (3 ** int(input()))))
    except:
        break
