def swap(i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp



def  selectionSort(arr):
    n=len(arr)
    for i in range(n-1):
        minI=i
        for j in range(i+1,n):
            if arr[j]<arr[minI]:
                minI=j
        swap(i,minI)

arr = list(map(int, input("Enter The List :").split()))
selectionSort(arr)
print("Sorted List :", *arr)        

