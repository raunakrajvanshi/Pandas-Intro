import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reading a CSV file into a pandas DataFrame
pizza = pd.read_csv("8358_1.csv")

# Displaying the first 5 rows of the DataFrame using the head() method
pizza.head()

# Displaying information about the DataFrame using the info() method
pizza.info()

# Creating a subset of the DataFrame with selected columns (menus.name is the name of the pizza, name is the name of the restaurant)
pizzaSubset = pizza.copy()[['id', 'city', 'address', 'postalCode', 
                          'menus.name', 'latitude', 'longitude',
                          'menus.amountMax', 'menus.amountMin']]

pizzaSubset.head()

# Removing duplicate rows based on 'id' and 'menus.name'
pizzaSubset = pizzaSubset.drop_duplicates(subset=['id', 'menus.name'])

# Counting the occurrences of each pizza name in the subset
namesOfPizza = pizzaSubset['menus.name'].value_counts()

# Merging the counts back into the subset DataFrame (converting namesOfPizza to DataFrame)
pizzaSubset = pd.merge(pizzaSubset, namesOfPizza.to_frame(),
                     left_on='menus.name', right_index=True, how='left')

pizzaSubset.head()

# Plotting the top 20 popular pizzas
plt.figure(figsize=(18, 4))
plt.plot(namesOfPizza.head(20), linestyle='none', markersize=15, marker='o')
plt.title('Top 20 Most Popular Pizza', fontsize=18)
plt.xticks(rotation=90)
plt.xlabel('Pizza Name', fontsize=14)
plt.ylabel('Counts', fontsize=14)
plt.grid(alpha=.3)
plt.margins(.05)
plt.show()
