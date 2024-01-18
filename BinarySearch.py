def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
        
    return -1  # not found

def binary_search(l, target):
    s = 0
    e = len(l) - 1
    while s <= e:
        mid = s + (e-s)//2
        if l[mid] == target:
            return mid
        if target < l[mid]:
            e = mid-1
        else:
            s = mid+1

    return -1




l = [12,33,47,49,56,67,71,78,82,89,94,98]
target = 12
print(naive_search(l, target))
print(binary_search(l, target))