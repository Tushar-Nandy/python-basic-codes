import pandas as pd
df=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_count=df[df["Primary Fur Color"]=='Gray']
cinnamon_count=df[df["Primary Fur Color"]=='Cinnamon']
black_count=df[df["Primary Fur Color"]=='Black']
# print(len(grey_count))
# print(len(black_count))
# print(len(cinnamon_count))
data_dict={
    "Fur Color":["Black","Grey","Cinnamon"],
    "Number of Squirrels":[len(black_count),len(grey_count),len(cinnamon_count)]
}

new_df=pd.DataFrame(data_dict)
print(new_df)