import pandas as pd 

df = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/lego-analysis/master/datasets/lego_sets.csv')

parent_theme = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/lego-analysis/master/datasets/parent_themes.csv')


# print(df.head(20))
# pd.set_option('display.max_rows' , None)
# print(parent_theme.head(20))

merged_data = df.merge(parent_theme , left_on='parent_theme' , right_on='name')
merged_data.drop(columns='name_y' , inplace= True)
#print(merged_data)

nulls_ = merged_data['set_num'].isnull().sum()
merged_data = merged_data.dropna(subset=['set_num'])
# print(merged_data)
null_check = merged_data.isnull().sum()
# print(null_check)


filtered_data = merged_data[(merged_data['is_licensed'] == True)]
starwars = merged_data[(merged_data['parent_theme'] == 'Star Wars')]


# print(filtered_data.shape) #it gives the a tuple (1179 rows , 8 columns)
# print(starwars.shape)

the_force = int(starwars.shape[0]/filtered_data.shape[0]*100)
print(f"The total percentage of star_Wars in the lego dataset = {the_force}%")


#In which year was Star Wars not the most popular licensed theme?


filtered_data_ = filtered_data.sort_values('year' , ascending=True)

grouped_data = filtered_data_.groupby(['year' , 'parent_theme']).sum().reset_index()
# print(group)

# x = group.sort_values('is_licensed' , ascending=False).drop_duplicates(['year'])
# x = x.sort_values('year' , inplace=True)
# # print(x)


# max_theme_per_year = grouped_data[ grouped_data['is_licensed'] == grouped_data.groupby('year')['is_licensed'].transform('max') ]
# print(max_theme_per_year)

# max_theme_per_year = grouped_data.loc[grouped_data.groupby('is_licensed')['year'].idxmax()]
# print(max_theme_per_year)

max_theme_per_year = grouped_data.loc[grouped_data.groupby('year')['is_licensed'].idxmax()]
print(max_theme_per_year)

  
