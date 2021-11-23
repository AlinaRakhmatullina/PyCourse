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
s=str(input())
def find_highest_in_dict(dict):
    sorted_dict = {
        k:v
        for k,v in sorted(dict.items(), key=lambda x:x[1][s])
}

    last = list(sorted_dict.keys())[-1]
    return last, dict[last]

print(find_highest_in_dict(Persons))

girls = [['Иванова', 'Алиса', 'Романовна', 'Ж', 175, 55],
         ['Рахматуллина', 'Алина', 'Римовна', 'Ж', 161, 60.5],
         ['Костарева', 'Арина', 'Олеговна', 'Ж', 180, 59]]
def find_highest_in_dict(list):
    rez = sorted(list, key=lambda x:x[4])[-1]
    return rez
print(find_highest_in_dict(girls))


import numpy as np
print(sum(np.array(range(101))))
p=int(input())
print(sum(np.array(range(p))))

import random
arr=np.random.randint(low=1,high=1000,size =(1,100))
print(np.mean(arr))
