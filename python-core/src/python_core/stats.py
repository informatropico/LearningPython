from typing import Iterable
from .person import Person

def adults(people: Iterable[Person]) -> list[Person]:
    return [p for p in people if p.is_adult()]

def average_age(people: Iterable[Person]) -> float:
    if not people:
        return 0.0
    return sum(p.age for p in people) / len([p for p in people])

def index_by_name(people: Iterable[Person]) -> dict[str, Person]:
    return {p.name: p for p in people}