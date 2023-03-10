list = (8, 2, 3, 0, 7)


def add(a, b):
    if b == 0:
        return 0
    else:
        return a[b - 1] + add(a, b - 1)
    
total = add(list, len(list))
print(total)
