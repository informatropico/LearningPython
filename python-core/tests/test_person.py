'''poetry add --group dev pytest'''

from python_core.person import Person


def test_person_is_adult_true():
    p = Person("Anna", 30)
    assert p.is_adult() is True


def test_person_is_adult_false():
    p = Person("Luca", 17)
    assert p.is_adult() is False

def test_birthday_increases_age():
    p = Person("Anna", 30)
    p.birthday()
    assert p.age == 31

