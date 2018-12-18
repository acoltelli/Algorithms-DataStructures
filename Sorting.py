def bubbleSort(arr):
	for i in range(0, len(arr)):
		for j in range(0,len(arr)-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

def insertionSort(arr):
    for i in range(1,len(arr)):
        current = arr[i]
        while i > 0 and arr[i-1] > current:         
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = current
    return arr








