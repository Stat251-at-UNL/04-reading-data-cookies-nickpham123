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
min_count = ingredient_counts.iloc[19]["recipe_count"]
common_20 = ingredient_counts[ingredient_counts["recipe_count"] >= min_count]
print(common_20)

#part2
rare_ingredients = ingredient_counts[ingredient_counts["recipe_count"] < 20]
print(", ".join(rare_ingredients["Ingredient"]))
print(ingredient_counts[ingredient_counts["recipe_count"] == 9])

#visualization
import matplotlib.pyplot as plt

cups = cookies[cookies["Unit"] == "cup"]
tsp = cookies[cookies["Unit"] == "teaspoon"]

# scatter plot of Quantity (cups) vs Rating
plt.scatter(cups["Quantity"], cups["Rating"])
plt.xlabel("Quantity (cups)")
plt.ylabel("Rating")
plt.title("Quantity (cups) vs Rating")
plt.show()

#histogram of quantity distribution for cups and teaspoons
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.hist(cups["Quantity"])
ax1.set_xlabel("Quantity (cups)")
ax1.set_ylabel("Frequency")
ax1.set_title("Distribution of Quantity (cups)")

ax2.hist(tsp["Quantity"])
ax2.set_xlabel("Quantity (teaspoons)")
ax2.set_ylabel("Frequency")
ax2.set_title("Distribution of Quantity (teaspoons)")

plt.tight_layout()
plt.show()