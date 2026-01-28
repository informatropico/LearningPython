from typing import Iterable
from collections.abc import Sequence
from .person import Person

def adults_only(people: list[Person]) -> list[Person]:
    if not people:
        return []
    return [p for p in people if p.is_adult()]

def average_age(people: Sequence[Person]) -> float:
    if not people:
        return 0.0
    return sum(p.age for p in people) / len(people)

def index_by_name(people: Iterable[Person]) -> dict[str, Person]:
    return {p.name: p for p in people}