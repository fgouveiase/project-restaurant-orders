from src.models.dish import Dish  # noqa: F401, E261, E501
from models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    pizza = Dish("Pizza", 10.00)
    bacon = Dish("Bacon", 7.00)

    assert pizza.name == "Pizza"
    assert pizza.recipe == {}
    assert pizza.price == 10.00

    assert hash(pizza) == hash(pizza)
    assert hash(pizza) != hash(bacon)

    assert pizza != bacon
    assert pizza == pizza

    assert pizza.__repr__() == "Dish('Pizza', R$10.00)"

    assert pizza.get_restrictions() == set()
    assert pizza.get_ingredients() == set()

    queijo = Ingredient("queijo mussarela")
    pizza.add_ingredient_dependency(queijo, 2)

    assert pizza.recipe == {queijo: 2}

    with pytest.raises(TypeError):
        Dish("Pizza", "10.00")

    with pytest.raises(ValueError):
        Dish("Pizza", -1.00)
