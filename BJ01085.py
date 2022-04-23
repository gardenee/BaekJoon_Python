x, y, w, h = map(int,input().split())
print(min((h-y), y, (w-x), x))
