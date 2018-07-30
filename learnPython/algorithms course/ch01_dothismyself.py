def insertionSort( A ):
    for x in range(1, len(A)):
        currentval = A[x]
        pos = x

        while pos>0 and A[pos-1]<currentval:
            A[pos]=A[pos-1]
            pos = pos-1

        A[pos]=currentval

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)
