import random
rnd = random.sample(range(100), 9)
rnd1 = random.sample(range(100), 11)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [num1 == mun2 for num1 in a for mun2 in b]
d = rnd
d.sort()
e = rnd1
e.sort()
print(d)
print(e)

f = random.sample(range(1,30), 12)
f.sort()
g = random.sample(range(1,30), 16)
g.sort()
result = [i for i in f if i in g]
print(f)
print(g)
print(result)