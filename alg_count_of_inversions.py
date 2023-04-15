#n = int(input())
#A = list(map(int, (input().split())))


c = 0


def mergesort(A):
    if len(A) > 1:
        m = len(A) // 2
        return merge(mergesort(A[0:m]), mergesort(A[m:]))
    else:
        return A


def merge(A, B):
    global c
    C = []
    i = 0
    j = 0
    while i != len(A) and j != len(B):
        len_a = len(A)
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            c += len_a - i
            j += 1
           # count += 1
    if j == len(B):
        C.extend(A[i:])
        #c += len(A[i + 1:]) * len(B)
        #count += len(A[i:])
    if i == len(A):
        C.extend(B[j:])
        #c += len(B[j:])
    return C


print(mergesort([7, 6, 5, 4, 3, 2, 1]))
print(c)


