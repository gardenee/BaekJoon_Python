lst = []


def merge_sort(arr):
    global cnt
    global answer

    if len(arr) == 1:
        return arr

    mid = (len(arr)+1)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    tmp = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            tmp.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            j += 1
        lst.append(tmp[-1])

    while i < len(left):
        tmp.append(left[i])
        lst.append(left[i])
        i += 1
    while j < len(right):
        tmp.append(right[j])
        lst.append(right[j])
        j += 1

    return tmp


N, K = map(int, input().split())
ipt = list(map(int, input().split()))
merge_sort(ipt)

if len(lst) >= K:
    print(lst[K-1])
else:
    print(-1)
