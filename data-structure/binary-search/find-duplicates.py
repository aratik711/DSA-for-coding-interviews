def find(a, target):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low+high) // 2
        if a[mid] < target:
            low = mid+1
        elif a[mid] > target:
            high = mid-1
        else:
            if mid-1<0:
                return mid
            if a[mid-1] != target:
                return mid
            high = mid - 1


A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
target = 108
x = find(A, target)
print(x)
