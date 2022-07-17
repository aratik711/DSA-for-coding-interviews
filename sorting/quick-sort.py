import random
def choose_pivot(left, right):
    i1 = left + random.randint(0, right - left)
    i2 = left + random.randint(0, right - left)
    i3 = left + random.randint(0, right - left)
    return max(min(i1, i2), min(max(i1, i2), i3))

def partition(lst, left, right):
    pivot_index = choose_pivot(left, right)
    lst[right], lst[pivot_index] = lst[pivot_index], lst[right]
    pivot = lst[right]
    i = left - 1
    for j in range(left, right):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[right] = lst[right], lst[i+1]
    return i+1

def quick_sort(lst, left, right):
    if left < right:
        pi = partition(lst, left, right)
        quick_sort(lst, left, pi - 1)
        quick_sort(lst, pi + 1, right)

# Driver code to test above
if __name__ == '__main__':

    lst = [5, 4, 2, 1, 3]
    quick_sort(lst, 0, len(lst) - 1)

    # Printing Sorted list
    print("Sorted list: ", lst)
