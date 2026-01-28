from python_core.person import Person

class PeopleStats:
    def __init__(self, people: list[Person]):
        self.people = people
    
    def adults_only(self) -> list[Person]:
        return [p for p in self.people if p.is_adult()]
    
    def average_age(self) -> float:
        if not self.people:
            return 0.0
        return sum(p.age for p in self.people) / len(self.people)
    
    def oldest_person(self) -> Person | None:
        if not self.people:
            return None
        return max(self.people, key=lambda p: p.age)