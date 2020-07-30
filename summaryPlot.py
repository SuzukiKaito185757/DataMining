import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv("./covid19-master/data/summary2.csv", sep=',')
#data = pd.read_csv("./covid19-master/data/summary.csv", names=('month', 'date'))
#dataConnect = data.month + data.date
#print(dataConnect)
x = df.ix[:, 0]
y = df.ix[:, 1]

#df.head()
#print(df.head)

plt.plot(x, y)
plt.show()
