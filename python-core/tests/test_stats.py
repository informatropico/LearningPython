from python_core.person import Person
from python_core.stats import average_age
from python_core.stats import adults_only


def test_average_age_normal_case():
    people = [
        Person("Anna", 30),
        Person("Marco", 20),
    ]

    assert average_age(people) == 25.0


def test_average_age_empty_list():
    people = []

    assert average_age(people) == 0.0


def test_adults_only():
    people = [
        Person("Anna", 30),
        Person("Luca", 17),
        Person("Marco", 22),
    ]

    adults = adults_only(people)

    assert len(adults) == 2
    assert all(p.is_adult() for p in adults)

