s1 = "xkjaaksdsa xkjfsdk xxxxsd sdfajkl"
s2 = ""
for x in s1:
    if x == "x":
        s2 += "y"
    else:
        s2 += x
print(s2)

set1 = [5, 6, 8, 2, 65, 2, 33, 6, 99, 22, 11, 55, 10, 6]
multi = 1
for x in set1:
    if x // 5 == x / 5 or x // 3 == x / 3:
        multi *= x
print(multi)

s1 = "xkjaaksdsa xkjfsdk xxxxsd sdfajkl"
s1 = s1.replace('x', 'y')
print(s1)

I1 = ['Рахматуллина', 'Алина', 'Римовна', 'Ж',161,60.5 ]
I2 = {
    'Фамилия': 'Рахматуллина',
    'Имя': 'Алина',
    'Отчество': 'Римовна',
    'Рост': 161,
    'Вес': 60.5
}