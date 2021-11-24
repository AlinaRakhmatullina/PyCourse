Persons = {
    ('Рахматуллина', 'Алина','Римовна'):
        {'Рост': 161,
         'Вес': 60.5
         },
    ('Иванова', 'Алиса','Романовна'):
        {'Рост': 175,
         'Вес': 55
         },
    ('Костарева', 'Арина','Олеговна'):
        {'Рост': 180,
         'Вес': 59
         }
}


from SearchFunction import find_most_in_dict

print(find_most_in_dict(Persons))

girls = [['Иванова', 'Алиса', 'Романовна', 'Ж', 175, 55],
         ['Рахматуллина', 'Алина', 'Римовна', 'Ж', 161, 60.5],
         ['Костарева', 'Арина', 'Олеговна', 'Ж', 180, 59]]

from SearchFunction import find_most_in_list

print(find_most_in_list(girls))

s1 = str(input())
s2 = str(input())
from CompareFunction import fuzzyComparing
print(fuzzyComparing(s1,s2))
print(max(len(s1),len(s2)))