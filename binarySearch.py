#resursive 
def binarySearch(arr, n):
    if len(arr) == 0:
        return False

    arr = sorted(arr)
    mid = len(arr) / 2
    if arr[mid] == n:
      return True
    else:
      if n > arr[mid]:
      	return binarySearch(arr[mid + 1:], n)
      else:
      	return binarySearch(arr[:mid], n)

        


testlist = [0, 1, -2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))




