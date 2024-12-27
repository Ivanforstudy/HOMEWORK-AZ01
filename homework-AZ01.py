import  pandas as pd

#df = pd.read_csv('london_houses.csv')

#print(df.head())
#print(df.info)
#print(df.describe())


df = pd.read_csv('dz (1).csv')

salary_by_city = df.groupby('City')['Salary'].mean()
print(salary_by_city)