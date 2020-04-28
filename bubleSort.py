

arr = list(map(int, input("Enter The List :").split()))


def swap(i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def bubSort(arr):
    size = len(arr)
    for i in range(0, size):
        for j in range(0, size-i-1):#dfghjk
            if arr[j] > arr[j+1]:
                swap(j+1, j)


bubSort(arr)
print("Sorted List :", *arr)
