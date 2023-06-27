from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    camarao = Ingredient("camarão")
    camarao_restriction = {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
    }
    carne = Ingredient("carne")

    assert camarao.name == "camarão"
    assert camarao.restrictions == camarao_restriction

    assert repr(camarao) == "Ingredient('camarão')"

    assert (camarao == carne) is False
    assert (camarao == camarao) is True

    assert hash(camarao) == hash("camarão")
