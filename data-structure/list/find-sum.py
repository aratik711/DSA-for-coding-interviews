def find_sum(lst, k):
    i, j = 0, len(lst) - 1
    lst = sorted(lst)
    while i < j:
        if lst[i] + lst[j] == k:
            return [lst[i], lst[j]]
        elif lst[i] + lst[j] > k:
            j += 1
        else:
            i += 1
    return False

print(find_sum([1, 21, 3, 14, 5, 60, 7, 6],81))
