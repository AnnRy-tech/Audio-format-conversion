def rotate_array(d, arr):
    n = len(arr)
    d = d % n

    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse(0, d - 1)
    reverse(d, n - 1)
    reverse(0, n - 1)

    return arr
