def x(z):
    y = ['A','B','C','D']
    d = ''
    for word in z:
        for r in word:
            if r not in y and ord(r) < 87:
                d += r
    return d.sort(revers = True)

print(x('BED'))
print(x('CLOSET'))