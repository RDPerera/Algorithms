    import sys
arr = list(map(int, input("Enter The List :").split()))
def swap(arr,r,l):
    tmp=arr[r]
    arr[r]=arr[l]
    arr[l]=tmp
def partition(arr,l,r):
    pivot=arr[l]
    i=l
    j=r
    while i<j:
        while arr[j]>pivot:
            j-=1
        while arr[i]<pivot:
            i+=1
        if i<j:
            swap(arr,i,j)
    swap(arr,l,j)
    return j

def quickSort(arr,l,r):
    div=partition(arr,l,r)
    quickSort(arr,0,div)
    quickSort(arr,div+1,r)


size=len(arr)
arr.append(sys.maxsize)
quickSort(arr,0,size)
print("Sorted List :", *arr)        