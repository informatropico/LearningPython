from python_core.people_stats import PeopleStats
from python_core.person import Person

def test_people_stats():
    people = [
        Person("Anna", 30),
        Person("Luca", 17),
        Person("Marco", 22),
    ]

    stats = PeopleStats(people)
    oldest = stats.oldest_person()

    assert len(stats.adults_only()) == 2
    assert stats.average_age() == (30 + 17 + 22) / 3
    assert oldest is not None
    assert oldest.name == "Anna"