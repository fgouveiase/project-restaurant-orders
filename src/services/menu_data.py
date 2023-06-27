import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.new_dishes(source_path)

    def new_dishes(self, path):
        obj_dishes = {}
        with open(path, "r") as arquivo:
            file = csv.reader(arquivo)
            next(file)

            for line in file:
                dish, price, name_ingredient, recipe_amount = line

                if dish not in obj_dishes:
                    obj_dishes[dish] = Dish(dish, float(price))

                ingredient = Ingredient(name_ingredient)
                obj_dishes[dish].add_ingredient_dependency(
                    ingredient, int(recipe_amount)
                )

        return set(obj_dishes.values())
