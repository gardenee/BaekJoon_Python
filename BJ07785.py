from sys import stdin

n = int(input())
company = set()

for _ in range(n):
    name, inout = stdin.readline().rstrip().split()
    if inout == 'enter':
        company.add(name)
    elif inout == 'leave':
        company.remove(name)

company = list(company)
company.sort(reverse=True)

for name in company:
    print(name)
