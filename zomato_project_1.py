# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# creating dataframe
dataframe = pd.read_csv("Zomato data .csv")
# print(dataframe.head())

# changing rate data type
def handleRate(value):
    value=str(value).split('/')
    value=value[0]
    return float(value)

dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())

# dataframe.info()

# restaurant type plot
sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Restaurant Type", c="red")
plt.ylabel("Count", c="red")
plt.show()

# second plot
#grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
#result = pd.DataFrame({'votes': grouped_data})
#plt.plot(result, c="green", marker="o")
#plt.xlabel("Type of restaurant", c="red", size=20)
#plt.ylabel("Votes", c="red", size=20)

# online order plot
sns.countplot(x=dataframe['online_order'])
plt.show()

# rate plot
plt.hist(dataframe['rate'],bins=5)
plt.title("Ratings Distribution")
plt.show()

# printing restaurants with max votes
max_votes = dataframe['votes'].max()
restaurant_maxvotes = dataframe.loc[dataframe['votes'] == max_votes, 'name']
print("Restaurants with max votes")
print(restaurant_maxvotes)

# online order boxplot
plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order', y = 'rate', data = dataframe)
plt.show()

# online order heatmap
pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")
plt.show()
