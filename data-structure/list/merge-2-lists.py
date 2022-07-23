def merge_list(lst1, lst2):
    p1, p2 = 0, 0
    while(p1 < len(lst1) and p2 < len(lst2)):
        if lst1[p1] > lst2[p2]:
            lst1.insert(p1, lst2[p2])
            p1 += 1
            p2 += 1
        else:
            p1 += 1
    if p2 < len(lst2):
        lst1.extend(lst2[p2:])
    return lst1

print(merge_list([1, 3, 4, 5],[2, 6, 7, 8]))
