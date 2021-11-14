n = [5, 6, 7, 8, -9, 0, -11, 9]
min = n.pop()
while n:
    a = n.pop()
    if a < min:
       min = a
print(min)