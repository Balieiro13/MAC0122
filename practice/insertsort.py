def insertSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while (j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 4]
    insertSort(A)
    print (A)

main()
