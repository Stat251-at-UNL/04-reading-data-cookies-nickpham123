library(tidyverse)
library(skimr)

cookies <- read_csv("choc_chip_cookie_ingredients.csv",
                     col_types = cols(
                       Ingredient = col_character(),
                       Text = col_character(),
                       Recipe_Index = col_character(),
                       Rating = col_double(),
                       Quantity = col_double(),
                       Unit = col_character(),            
                     ))

cookies <- select(cookies, -1)

skim(select(cookies, Rating, Quantity, Ingredient))

total_recipes <- n_distinct(cookies$Recipe_Index)

#part1
ingredients_counts <- summarise(group_by(cookies, Ingredient), 
                                  recipe_count = n_distinct(Recipe_Index),
                                  proportion = n_distinct(Recipe_Index)/total_recipes)

ingredients_counts <- arrange(ingredients_counts, desc(proportion))
common_20 <- head(ingredients_counts, 20)
print(common_20)

#part2
rare_ingredients <- filter(ingredients_counts, recipe_count < 20)
print(paste(rare_ingredients$Ingredient, collapse = ", "))

