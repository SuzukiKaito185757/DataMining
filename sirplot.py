import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv("COVID-19_Case.csv", sep=',')
#data = pd.read_csv("COVID-19_Case.csv", names=('month', 'date'))
#dataConnect = data.month + data.date
#print(dataConnect)
x = df.ix[1:10, 0]
y = df.ix[1:10, 2]

#df.head()
#print(df.head)

plt.plot(x, y)
plt.show()
