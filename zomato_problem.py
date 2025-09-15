import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as  sns 




df = pd.read_csv(r"C:\Users\Chinna Joka\Desktop\pandas_real_world_problems_python\Input_sales\Zomato-data-.csv")

null_check = df.isnull().sum().sum()


def remove_denominator(rate):
    return rate[:3]

df['rate'] = df['rate'].apply(remove_denominator)

# print(df)

df['rate'] = pd.to_numeric(df['rate'] , downcast='float')  
# print(df)

# print(df.info())
# print(df.describe().astype('int'))


# sns.countplot( x = df['listed_in(type)'] , label = 'Food serving Type' , palette= 'Set1')
# plt.yticks(color = 'black' , weight= 'heavy')
# plt.xticks(color = 'black' , weight= 'heavy')
# plt.title('Dining Category of Restaurants',  pad = 30 ,fontdict= { 'fontname' : 'monospace' , 'size' : 16 , 'weight' : 'bold' , 'style' : 'italic' , 'color' : 'black'})
# plt.xlabel('Listed_in(Type)',labelpad=15 , fontdict= { 'fontname' : 'monospace' , 'size' : 14 , 'weight' : 'bold' , 'style' : 'italic' , 'color' : 'green'})
# plt.ylabel('Count' ,labelpad=15 ,fontdict= { 'fontname' : 'monospace' , 'size' : 14 , 'weight' : 'bold' , 'style' : 'italic' , 'color' : 'red'})
# plt.legend()
# plt.show()


grouped_data = df

# x = grouped_data.loc[grouped_data.groupby('name')['votes'].idxmax()]
# print(x) 
x = grouped_data.loc[grouped_data.groupby('votes')['name'].idxmax()]
print(x)
max = grouped_data[grouped_data['votes'] == grouped_data['votes'].max()]
print(max)

#Online orders plot 
# sns.countplot(x = grouped_data['online_order'] , palette='Set1')
# plt.yticks(color = 'black' , weight= 'heavy')
# plt.xticks(color = 'black' , weight= 'heavy')
# plt.title('Online Order Availbility',  pad = 30 ,fontdict= { 'fontname' : 'monospace' , 'size' : 16 , 'weight' : 'bold' , 'style' : 'italic' , 'color' : 'black'})
# plt.xlabel('Online Order',labelpad=15 , fontdict= { 'fontname' : 'monospace' , 'size' : 14 , 'weight' : 'bold' , 'style' : 'italic' , 'color' : 'green'})
# plt.ylabel('Count' ,labelpad=15 ,fontdict= { 'fontname' : 'monospace' , 'size' : 14 , 'weight' : 'bold' , 'style' : 'italic' , 'color' : 'red'})
# plt.legend()
# plt.show()

#Analyze Ratings
#Checking the distribution of ratings from the rate column.

# plt.hist(df['rate'] , label='Ratings')
# plt.yticks(color = 'black' , weight= 'heavy')
# plt.xticks(color = 'black' , weight= 'heavy')
# plt.title('Rating Distribution',  pad = 30 ,fontdict= { 'fontname' : 'monospace' , 'size' : 16 , 'weight' : 'bold' , 'style' : 'italic' , 'color' : 'black'})
# plt.xlabel('Ratings',labelpad=15 , fontdict= { 'fontname' : 'monospace' , 'size' : 14 , 'weight' : 'bold' , 'style' : 'italic' , 'color' : 'green'})
# plt.ylabel('Count' ,labelpad=15 ,fontdict= { 'fontname' : 'monospace' , 'size' : 14 , 'weight' : 'bold' , 'style' : 'italic' , 'color' : 'red'})
# plt.xlim(2,5)
# plt.legend()
# plt.show()


sns.countplot(x = df['approx_cost(for two people)'] , palette='Set1')
plt.yticks(color = 'black' , weight= 'heavy')
plt.xticks(color = 'black' , weight= 'heavy')
plt.title('Approximation Cost For Couples',  pad = 30 ,fontdict= { 'fontname' : 'monospace' , 'size' : 16 , 'weight' : 'bold' , 'style' : 'italic' , 'color' : 'black'})
plt.xlabel('approx_cost(for two people)',labelpad=15 , fontdict= { 'fontname' : 'monospace' , 'size' : 14 , 'weight' : 'bold' , 'style' : 'italic' , 'color' : 'green'})
plt.ylabel('Count' ,labelpad=15 ,fontdict= { 'fontname' : 'monospace' , 'size' : 14 , 'weight' : 'bold' , 'style' : 'italic' , 'color' : 'red'})
plt.legend()
plt.show()