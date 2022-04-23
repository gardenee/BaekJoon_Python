dic = {'AA': 'A', 'AG': 'C', 'AC': 'A', 'AT': 'G', 'GA': 'C', 'GG': 'G', 'GC': 'T', 'GT': 'A', 'CA': 'A',
       'CG': 'T', 'CC': 'C', 'CT': 'G', 'TA': 'G', 'TG': 'A', 'TC': 'G', 'TT': 'T'}

N = int(input())
DNA = input()
p1 = DNA[-1]
for i in range(2, N+1):
    p1 = dic.get(DNA[-i]+p1)

print(p1)
