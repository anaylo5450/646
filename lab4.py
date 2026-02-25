import pandas as pd
titanic = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv')
print(titanic.groupby(['survived']).size()),
print(list(titanic['survived']).count('no')),
print(list(titanic['survived']).count('yes'))
print(titanic[titanic['survived']=='yes']['survived'].size),
print(titanic[titanic['survived']=='no']['survived'].count())
titanic.groupby("survived")["survived"].count().loc["yes"]