a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []

# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

d.append(a)
d.append(b)
d.append(c)
print(d)

e.append(a[0])
e.append(a[1])
e.append(a[2])
e.append(b[0])
e.append(b[1])
e.append(b[2])
e.append(c[0])
e.append(c[1])
e.append(c[2])

print(e)

#print(a[0],a[1],a[2],b[0],b[1],b[2],c[0],c[1],c[2])cd