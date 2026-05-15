import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Task1:

    def mean(self,data):
        print(f"Mean of data: {data.mean()}")
        
    def sum(self,data):
        print(f"Sum: {data.sum()}")
        
    def max(self,data):
        print(f"Max: {data.max()}")
        
    def min(self,data):
        print(f"Minimum: {data.min()}")
        
    def reshape(self,data):
        reshaped_data= data.reshape(-1,1)
        print(f"Reshaping: {reshaped_data}")
        
    def slicing(self,data):
        print(f"Slicing: {data[0:10]}")
        
    def broadcastind(self,data):
        data += 1000
        print(f"Broadcasting: {data[0:5]}")
        


obj= Task1()
country_data= pd.read_csv("country_wise_latest.csv")
data= np.array(country_data["Confirmed"].values)
obj.mean(data)
obj.sum(data)
obj.max(data)



# print(country_data.head())
# Task 1 – NumPy Operations
# ● Create NumPy arrays using COVID confirmed cases data.
# ● Perform:
# ○ Mean
# ○ Sum
# ○ Max
# ○ Min
# ○ Reshaping
# ○ Slicing
# ○ Broadcasting

data=  np.array(country_data["Confirmed"].values)

print(data.mean())
print(data.sum())
print(data.max())
print(data.min())
print(data.shape)
reshaped_data= data.reshape(-1,1)
print(reshaped_data)
print(data[0:10])
data += 1000
print(data[0:5])


# Task 2 – Read CSV using Pandas
# ● Read the COVID dataset using Pandas.
# ● Display:

# ○ First 5 rows
# ○ Last 5 rows
# ○ Data types
# ○ Null values
# ○ Duplicate values

data = pd.read_csv("country_wise_latest.csv")
print(data.head())
print(data.tail())
print(data.dtypes)
print(data.isnull().sum())
duplicate_data= data.duplicated().sum()
print(duplicate_data)

# Task 3 – Data Cleaning
# ● Handle missing values.
# ● Remove duplicate rows.
# ● Replace invalid values like:
# ○ inf
# ○ null
# ○ 0 where necessary

# There is no missing values and duplicate rows
data.drop_duplicates(inplace=True)
print(data.isnull().sum())




# Task 4 – Exploratory Data Analysis (EDA)
# Perform analysis on:
# ● Total confirmed cases
# ● Total deaths
# ● Total recovered cases
# ● WHO region wise analysis
# ● Highest active cases
# ● Top 10 affected regions

confirmed_cases= data["Confirmed"].sum()
print(confirmed_cases)
deaths= data["Deaths"].sum()
print(deaths)

recovered_cases= data["Recovered"].sum()
print(recovered_cases)

region_analysis = data.groupby("WHO Region")["Confirmed"].sum()
print(region_analysis)
active_cases= data.groupby("Country/Region")["Active"].sum().sort_values(ascending=False)
print(f"Top 10 highest Active cases : \n{active_cases.head(10)}")

affected_region = data.groupby("Country/Region")["Deaths"].sum().sort_values(ascending= False)
print(affected_region.head(5))


# Task 5 – Visualization
# Create the following charts:
# ● Line graph for confirmed cases

# ● Bar chart for WHO region wise deaths
# ● Histogram for active cases
# ● Pie chart for recovered cases by region
# ● Scatter plot between confirmed and deaths
# ● Heatmap for correlation analysis

sns.lineplot(x=data["Confirmed"], y=data["Deaths"])

sns.barplot(x=region_analysis.index, y= region_analysis.values)
sns.histplot(data["Active"], bins=30)
data["recovered_cases"]= data.groupby("Country/Region")["Recovered"].sum()
plt.pie(data["Recovered"])
sns.scatterplot(x=data["Confirmed"], y=data["Deaths"])
sns.heatmap(data[["Confirmed","Deaths", "Recovered"]].corr(), annot=True)
plt.show()