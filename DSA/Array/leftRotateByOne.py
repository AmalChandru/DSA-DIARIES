def leftRotateByOne(arr, n):
    temp = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]

    arr[n-1] = temp

A = {1,2,3,4,5}
print(A)
leftRotateByOne(A,len(A))
print(A)
