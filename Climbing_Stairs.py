n = 2
if n == 1:
    print(1)
if n == 2:
    print(2)
a = 1
b = 2
for _ in range(2, n):
    c = a + b
    a = b
    b = c
print(b)
