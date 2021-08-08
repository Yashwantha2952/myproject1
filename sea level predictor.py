import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
#import seaborn as sb

df=pd.read_csv("sea-level.csv")
y=df["CSIRO Adjusted Sea Level"]
x=df["Year"]

fig,ax=plt.subplots()
plt.scatter(x,y)

new_df = df.loc[df ['Year'] >= 2000]
res=linregress(x,y)
print(res)
x_pred=pd.Series([i for i in range(1880,2050)])
y_pred=res.slope*x_pred+res.intercept
plt.plot(x_pred,y_pred,"r")
    
new_x= new_df['Year']
new_y = new_df ["CSIRO Adjusted Sea Level"]
res_2= linregress (new_x, new_y)
x_pred2 = pd.Series ([i for i in range (2000,2050)])
y_pred2 = res_2.slope*x_pred2 + res_2.intercept
plt.plot(x_pred2, y_pred2, 'green')

ax.set_xlabel('Year')
ax.set_ylabel('Sea Level (inches)')
ax.set_title('Rise in Sea Level')
plt.savefig('sea_level_plot.png')
plt.grid()   # for grid lines