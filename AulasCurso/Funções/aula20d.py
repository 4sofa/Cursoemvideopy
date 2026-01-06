def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*= 2
        pos += 1


val = [1, 2, 3, 4, 5]

dobra(val)
print(val)