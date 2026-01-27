from dataclasses import dataclass

'''
A simple data class representing a person with a name and age.
Provides a method to check if the person is an adult (age >= 18) and a string representation method.

Hai appena ottenuto gratis:
__init__
__repr__
confronto (==)
leggibilità

'''
@dataclass
class Person:
    name: str
    age: int

    def is_adult(self) -> bool:
        return self.age >= 18

    def __str__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"