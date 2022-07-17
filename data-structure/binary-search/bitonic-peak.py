def find_highest_number(a):
    low = 0
    high = len(a) - 1
    if len(a) < 3:
        return None
    while low <= high:
        mid = (low+high) // 2
        mid_left = a[mid-1] if mid-1>=0 else float("-inf")
        mid_right = a[mid+1] if mid+1 < len(a) else float("inf")
        if mid_left < a[mid] and mid_right > a[mid]:
            low = mid + 1
        elif mid_left > a[mid] and mid_right < a[mid]:
            high = mid - 1
        elif mid_left < a[mid] and mid_right < a[mid]:
            return a[mid]
    return None

# Peak element is "5".
A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(find_highest_number(A))
A = [1, 6, 5, 4, 3, 2, 1]
print(find_highest_number(A))
A = [1, 2, 3, 4, 5]
print(find_highest_number(A))
A = [5, 4, 3, 2, 1]
print(find_highest_number(A))
