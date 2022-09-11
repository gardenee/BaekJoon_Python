import math


def merge(arr, p, q, r):
    print("merge", arr[p:q+1], arr[q+1:])
    tmp = []
    i, j, t = p, q, 0
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]
            t += 1
            i += 1
        else:
            tmp[t] = arr[j]
            t += 1
            j += 1
    while i <= q:
        tmp[t] = arr[i]
        t += 1
        i += 1
    while j <= r:
        tmp[t] = arr[j]
        t += 1
        j += 1
    i, t = p, 0
    while i <= r:
        arr[i] = tmp[t]
        i += 1
        t += 1

    return arr


def merge_sort(arr, p, r):
    if p < r:
        q = math.ceil((p + r)/2)
        arr = merge_sort(arr, p, q)
        print("front", arr[p:q+1])
        arr = merge_sort(arr, q+1, r)
        print("back", arr[q+1:])
        arr = merge(arr, p, q, r)
    return arr


N, K = map(int, input().split())
ipt = list(map(int, input().split()))
print(merge_sort(ipt, 0, N-1))
