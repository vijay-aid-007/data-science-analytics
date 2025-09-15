import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import os 


df = pd.read_csv("C:/Users/Chinna Joka/Desktop/pandas_real_world_problems_python/Input_sales/Sales_April_2019.csv")
# print(df)

all_files = [files for files in os.listdir('C:/Users/Chinna Joka/Desktop/pandas_real_world_problems_python/Input_sales/')]
# print(all_files)

# for files in all_files:
    # print(files) 

all_months_data  = pd.DataFrame()

for files in all_files:
    df = pd.read_csv(f"C:/Users/Chinna Joka/Desktop/pandas_real_world_problems_python/Input_sales/{files}")
    all_months_data = pd.concat([all_months_data , df])

all_months_data.to_csv('All_months_data.csv' , index=False)

print(all_months_data)


all_months_data.dropna(how='all' , inplace=True)

# null_check = all_months_data.isnull().sum() 
# print(f"null check {null_check}")

# all_months_data = all_months_data[all_months_data['Order Date'].str[0:2] != 'Or' ]

# all_months_data['Month'] = all_months_data['Order Date'].str[0:2]
# all_months_data['Month'] = all_months_data['Month'].astype(int) 


all_months_data['Month'] = pd.to_numeric(all_months_data['Order Date'].str[0:2], errors='coerce')
all_months_data.dropna(subset=['Month'], inplace=True)
all_months_data['Month'] = all_months_data['Month'].astype(int)



# print(all_months_data)

all_months_data['Quantity Ordered'] = pd.to_numeric(all_months_data['Quantity Ordered'])
all_months_data['Price Each'] = pd.to_numeric(all_months_data['Price Each'])

all_months_data['Sales'] = all_months_data['Quantity Ordered'] * all_months_data['Price Each']

#Q1> 

highest_month_sales = all_months_data.groupby('Month').sum()[['Quantity Ordered' , 'Price Each', 'Sales']]
print(highest_month_sales)


x= range(1,13)
y = highest_month_sales['Sales']
plt.bar(x , y , label = 'Sales', color ='r')
plt.ylabel("Sales",c='r' , fontdict={'fontname' : 'sans-serif' } , weight = 'bold' , style= 'italic' )
plt.xlabel('Months' , color = 'b' , fontdict={'fontname' : 'sans-serif' } , weight = 'bold' , style= 'italic' )
plt.title('Sales Graphs', color= 'g' , fontdict={'fontname' : 'sans-serif' } , weight = 'bold' , style= 'italic' )
plt.xticks(x)
plt.legend()
plt.show()



#Q2 Which city has more sales 
def get_state(purchase_address):
    return purchase_address.split(' ')[2]

def get_city_state(purchase_address):
    return (purchase_address.split(', ')[-2] +" " +purchase_address.split(', ')[-1][:2])

all_months_data['City'] = all_months_data['Purchase Address'].apply(get_city_state)
print(all_months_data)

x = all_months_data['City'].unique()
print(x)


highest_city_sales = all_months_data.groupby('City').sum()[['Sales' , 'Quantity Ordered']]
print(highest_city_sales)

print(f" {highest_city_sales[highest_city_sales['Sales'] == highest_city_sales['Sales'].max()]}")



plt.figure(figsize= (3,3))
x= [city for city,df in all_months_data.groupby('City')]

y = highest_city_sales['Sales']
plt.bar(x , y , label = 'Sales', color ='g')
plt.ylabel("Sales",c='black' , fontdict={'fontname' : 'sans-serif' } , weight = 'bold' , style= 'italic' )
plt.xlabel('Cities' , color = 'b' , fontdict={'fontname' : 'sans-serif' } , weight = 'bold' , style= 'italic', )
plt.title('Sales Graphs', color= 'r' , fontdict={'fontname' : 'sans-serif' } , weight = 'bold' , style= 'italic' )
plt.xticks(x  , size = 7)
plt.legend()
plt.show()


all_months_data['Order Date'] = pd.to_datetime(all_months_data['Order Date'] , format = 'mixed')

all_months_data['Hours'] = all_months_data['Order Date'].dt.hour
print(all_months_data)
all_months_data['Minutes'] = all_months_data['Order Date'].dt.minute 
print(all_months_data)

best_time_to_advertisements = all_months_data.groupby('Hours').count()[['Sales']] 
print(best_time_to_advertisements)

hours = [hour for hour , df in all_months_data.groupby('Hours')]
plt.plot(hours , all_months_data.groupby(['Hours']).count())
plt.xlabel('Hours' , fontdict={'fontname' : 'sans-serif' } , weight = 'bold' , style= 'italic' )
plt.ylabel('Number of Orders' , fontdict={'fontname' : 'sans-serif' } , weight = 'bold' , style= 'italic' ) 
plt.xticks(hours)
plt.grid()
plt.show() 

# #Q4> which products are most often sold 

df = all_months_data.groupby(['Order ID'])['Product'].count()
print(df)

top_selling = df['Product'].value_counts().head(30)
print(top_selling)

# dataframe = all_months_data[ all_months_data['Order ID'].duplicated(keep=False)]
# print(dataframe)
# dataframe['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x : ",".join(x))
# print(dataframe.head(100))


# import collections
# import itertools 
# from itertools import combinations  
# from  collections import counter 

