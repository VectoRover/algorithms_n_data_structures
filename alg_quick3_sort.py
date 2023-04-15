
def partition(A, l, r):
    x = A[l]
    j = l
    k = l
    for i in range(l+1, r + 1):
        if A[i] < x:
            j += 1
            k += 1
            A[i], A[k] = A[k], A[i]
            A[k], A[j] = A[j], A[k]
        elif A[i] == x:
            A[i], A[k + 1] = A[k + 1], A[i]
            k += 1
    A[l], A[j] = A[j], A[l]
    return j, k


def quick_sort(A, l, r):
    if l >= r:
        return
    j, k = partition(A, l, r)
    quick_sort(A, l, j)
    quick_sort(A, k + 1, r)
    return A



