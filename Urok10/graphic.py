# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

import pandas as pd

data = pd.DataFrame({'whoAmI':lst})

for value in data['whoAmI'].unique():
    data[value] = data['whoAmI'].apply(lambda x: 1 if x == value else 0)

data.head()
