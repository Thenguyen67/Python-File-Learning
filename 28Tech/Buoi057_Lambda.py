func = lambda x : x**3 

sum = lambda x, y, z : x + y + z

check = lambda x, y : x if x > y else y 

print(func(4))

print(sum(5, 6, 7))

a = [1, 2, 3, 4, 5]
b = list(map(lambda x : x**2, a)) # Áp dụng lên mọi phần tử của a
print(b)

c = list(filter(lambda x : x % 2 == 0, a))
print(c)
