a = [10, 20, 30, 40, 50]

b = a[2 : len(a) : 1] # start : end : step
print(b)

c = a[1 : len(a) : 2]
print(c) 

# Nếu end value là số âm thì lấy max index - end index (dương)

d = a[:: -1]
print(d) #In mảng ngược lại, tương đương reverse

f = ["A", "B", "C"]
f[:0] = [10, 20, 30]
print(f)

g = ["A", "B", "C"] #[10, 20, 30, 'A', 'B', 'C']
g[len(f):] = [10, 20, 30] #['A', 'B', 'C', 10, 20, 30]
print(g)

h = g[:] #copy
print(h)