import numpy as np
import pandas as pd


if __name__ == '__main__':
    data = pd.Series([0.25, 0.5, 0.75, 1.0])
    print(data)

    print(data.values)
    print(data.index)

    print(data[1])
    print(data[1:3])

    data = pd.Series([0.25, 0.5, 0.75, 1.0],
                     index=['a', 'b', 'c', 'd'])
    
    print(data['b'])

    data = pd.Series([0.25, 0.5, 0.75, 1.0],
                     index=[2, 5, 3, 7])
    print(data)
    print(data[5])

    population_dict = {'California': 38332521,
                       'Texas': 26448193,
                       'New York': 19651127,
                       'Florida': 19552860,
                       'Illinois': 12882135}
    population = pd.Series(population_dict)
    print(population)

    print(population['California'])
    print(population['California':'Illinois'])

    print(pd.Series([2, 4, 6]))
    print(pd.Series(5, index=[100, 200, 300]))
    print(pd.Series({2:'a', 1:'b', 3:'c'}))
    print(pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2]))

    print(pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2]))
    






    



    



