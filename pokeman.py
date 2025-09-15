import numpy as  np 
import pandas as pd 
import seaborn as sns 

df = pd.read_csv(r"C:\Users\Chinna Joka\Downloads\Pokemon1.csv")

#_______________________________ADDING A NEW COLUMN TO THE EXISTED DATARAME___________________________


df['Status'] = np.random.choice(['YES',"NO"],size=len(df))
#print(df['Status'].value_counts()) 

df['Combat Power'] = df['Attack'] * df['Defense']
print(df)

df.drop(columns='Status' , inplace=True , axis=1)
print(df) 



#________________________________SORTING COLUMNS ____________________________________


sort_total = df.sort_values('Total',ascending=False)
print(sort_total) 

# pd.set_option('display.max_rows' , None)
#print(df.sort_values(by=['Total'] , ascending=True))


#_______________________________GROUP BY ______________________________



#Grouping columns based on the types
Group_ = df['Type 1'].value_counts()
#print(Group_)


Group_x = df.groupby('Type 1')['Type 1'].count()
# print(Group_x.sort_values(ascending=False))


#Adding a new column names as combat power
df["Combat Power "] = (df['Attack']*df["Defense"] )
#print(df) 

#filtering 

cp_lengendary = df[(df['HP'] > 80) & (df['Defense'] > 80)]

filter_ = df[(df.Total > 500)] [['Name','Total'] ]
# print(filter_)
# print(cp_lengendary)

#Calculate descriptive statistics for numerical columns (e.g., mean, median, min, max, standard deviation of HP, Attack, Defense, etc.).



#___________________________________AGGREGATE FUNCTIONS IN PANDAS_______________________ 


mean_total = df['Total'].mean()
#print(f"Mean value of 'Total': {mean_total:.2f}")
sum_total = df['Total'].sum()
#print(f"sum value of 'Total': {sum_total}")
max_total = df['Total'].max()
#print(f"max value of 'Total': {max_total}")
max_total = df['Total'].min()
#print(f"max value of 'Total': {max_total}")


#___________________________________MULTIPLE AGGRIGATE FUNCTION_____________________________

multiple_aggregate_functions = df.agg({'Sp. Atk' : ['mean' , 'min' , 'max', 'sum'], 
                                       'Sp. Def' : ['count' , 'sum' , 'std' , 'var']})


multiple_data_of_Attack = df.agg(
    {'Attack' : ['mean' , 'max' , 'min' , 'sum']}
)

print(multiple_data_of_Attack)



#print(multiple_aggregate_functions_2)

#print(multiple_aggregate_functions)
#print(multiple_aggregate_functions)




group_1 = df['Type 1'].value_counts()
#print(group_1)
group_2 = df.groupby('Type 2')['Type 2'].count()
#print(group_2.sort_values(ascending=False))

Unique_types1 = df['Type 1'].unique()
#print(Unique_types1)                            #   .nunique() to count unqiue values by number 
Unique_types2 = df['Type 2'].unique()
#print(Unique_types2) 


uniq_in_2 = list(set(Unique_types1) - set (Unique_types2))
#print(uniq_in_2)

# for col in df.columns:
    #print(f"Unique  in {col}: {df[col].unique()}")

legendary_pokeman = df[df['Legendary'] == True]
#print(legendary_pokeman.nunique())
#print(legendary_pokeman)

#type 1 primary type == water 
water_type = df[df['Type 1'] == 'Water'].count()
#print(water_type)

#type 2 primary type == flying
flying_type = df[df['Type 2'] == 'Flying'].count()
#print(flying_type) 



#_________________________________________INDEXING AND SLICING_________________________________

#SYNTAX DF.LOC[COL_INDEX , ROW_INDEX]

#LOC 
#ILOC 
#AT
#IAT 


#        Name    Type 1    Type 2  Total   HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Stage  Legendary  Combat Power 

# print(df.loc[0:20, ['Name','Attack' , 'Defense']])
# print(df.loc[0::20, ['Type 1', 'Type 2' , 'Stage', 'Legendary']])   #FOR LOC WE HAVE TO PASS COLUMN NAMES AS ARGUMENTS 
# print(df.loc[100::5, "Name"])

# print(df.iloc[120::5 , 0::2])          #FOR ILOC WE HAVE TO PASS ARGUMENTS IN THE NUMERICAL FORMAT





#__________________________________RENAMING COLUMNS / RESETING INDEX / DROPING COLUMNS / BACKING UP _____________________

#RENAMING COLUMNS 

rename_col = df.rename(columns={'Name' : 'Pokeman_Name'})
print(rename_col)

rename_col.reset_index(inplace=True)
#print(rename_col)

rename_col.set_index('HP', inplace=True)
print(rename_col)

backed_up = df.copy(deep=True)
#print(f"This data is backed_up: {backed_up}")

#print(df)
df.drop('Legendary' , inplace=True , axis=1)
#print(df)
df.drop(columns= 'Combat Power ' , axis=1 , inplace=True , errors='ignore')
#print(df)
 
#__________________________________PIVOT TABLE & CROSS TAB_________________________________________

#PIVOT TABLE 
pivot_table = df.pivot_table(index='Type 1', values='Total', aggfunc='mean')
print(pivot_table)

# piv = pd.pivot_table(df, index='Type 2', values=['HP', 'Attack', 'Speed'], aggfunc='mean')
# print(piv.round().astype(int))

# pivot_ = pd.pivot_table(df, index = 'Name' , values=['Type 1', 'Type 2'] , aggfunc='count')
# print(pivot_)

#df.to_csv('Practised Pokeman Excel sheet.csv' , index= False)