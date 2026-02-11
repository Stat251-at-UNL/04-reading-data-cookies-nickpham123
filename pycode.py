import pandas as pd
from skimpy import skim

cookies = pd.read_csv("choc_chip_cookie_ingredients.csv",
                      index_col=0,
                      dtype={
                          "Ingredient": str,
                          "Text": str,
                          "Recipe_Index": str,
                          "Rating": float,
                          "Quantity": float,
                          "Unit": str
                      })

skim(cookies[["Rating", "Quantity", "Ingredient"]])

total_recipes = cookies["Recipe_Index"].nunique()

#part1
ingredient_counts = cookies.groupby("Ingredient")["Recipe_Index"].nunique().reset_index()
ingredient_counts.columns = ["Ingredient", "recipe_count"]
ingredient_counts["proportion"] = ingredient_counts["recipe_count"]/total_recipes
ingredient_counts = ingredient_counts.sort_values("proportion", ascending=False)
common_20 = ingredient_counts.head(20)
print(common_20)

#part2
rare_ingredients = ingredient_counts[ingredient_counts["recipe_count"] < 20]
print(", ".join(rare_ingredients["Ingredient"]))

#visualization

# scatter plot of Quantity vs Rating
import matplotlib.pyplot as plt
plt.scatter(cookies["Quantity"], cookies["Rating"])
plt.xlabel("Quantity")
plt.ylabel("Rating")
plt.title("Quantity vs Rating")
plt.show()

#histogram of quantity
plt.figure()
plt.hist(cookies["Quantity"])
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.title("Distribution of Quantity")
plt.show()