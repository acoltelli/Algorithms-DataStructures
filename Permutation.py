# Heap's algorithm
def permutation(arr, n):
    if n == 1:
        yield arr
    else:
        for i in range(n - 1):
            for p in permutation(arr, n - 1):
                yield p
            if n % 2 == 0:  # even len arr
                # zero indexed, called on permutation(n-1), so n is n-1 etc.
                arr[i], arr[n - 1] = arr[n - 1], arr[i]  # swap elements
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]

        for p in permutation(arr, n - 1):
            yield p
