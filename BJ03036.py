def gcs(a, b):
    temp = b
    b = a % b
    a = temp
    if b==0: return a
    else: return gcs(a, b)


N = int(input())
ipt = list(map(int, input().split()))
ref = ipt[0]

for i in range(1, N):
    curr = ipt[i]
    GCS = gcs(max(ref, curr), min(ref, curr))
    print(str(ref//GCS) + "/" + str(curr//GCS))
