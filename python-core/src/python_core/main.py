from .person import Person
from .stats import adults, average_age, index_by_name


def main():
    people = [
        Person("Anna", 30),
        Person("Luca", 17),
        Person("Marco", 22),
    ]

    adult_people = adults(people)

    for p in adult_people:
        print(p)

    print("Average adult people age:", average_age(adult_people))

    people_by_name = index_by_name(people)
    
    for p in people_by_name.values():
        print(p)

    print("Anna:", people_by_name["Anna"])


if __name__ == "__main__":
    main()



'''
def main():

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    threshold = 5

    grades = [
        {"name": "Anna", "grade": 28},
        {"name": "Luca", "grade": 18},
        {"name": "Marco", "grade": 30},
        {"name": "Simona", "grade": 15},
    ]

    print(type(grades))
    print(type(grades[0]))

    people = [
        {"name": "Anna", "age": 30},
        {"name": "Luca", "age": 17},
        {"name": "Marco", "age": 22},
    ]

    result = sum_numbers(squared_greater_than(numbers, threshold))
    print("Total:", result)
    print("Total type:", type(result))
    
    result = sum_squared_numbers_grater_than(numbers, threshold)
    print("Total:", result)
    print("Total type:", type(result))

    result = build_dictionary_from_list(grades, "name", "grade")
    print_dictionary(result)
    print("Result type:", type(result))

    result = build_dictionary_from_list_with_threshold(grades, 18, "name", "grade")
    print_dictionary(result)
    print("Result type:", type(result))

    result = build_dictionary_from_list(people, "name", "age")
    print_dictionary(result)
    print("Result type:", type(result))

    print(f"result['Anna'] = {result['Anna']}")
    print(f"result['Anna'] = {result.get('Anna')}")
    print(f"result['Mario'] = {result.get('Mario')}")


    senior_people_dict = build_dictionary_from_list_with_threshold(people, 18, "name", "age")
    print_dictionary(senior_people_dict)
    print("Result type:", type(senior_people_dict))

    result = average(senior_people_dict.values())
    print("Average age of senior people:", result)
    print("Result type:", type(result))
    
    
    people = [
        Person("Anna", 30),
        Person("Luca", 17),
        Person("Marco", 22),
    ]

    for p in people:
        print(p)

    adult_people = [p for p in people if p.is_adult()]
    for p in adult_people:
        print(p)
    print(type(adult_people))
    
    
    adults_ages_by_name = {p.name: p.age for p in adult_people}
    print(type(adults_ages_by_name))
    print_dictionary(adults_ages_by_name)

    average_adults_age = average(adults_ages_by_name.values())
    print("Average age of adult people:", average_adults_age)

    average_age = average([p.age for p in people])
    print("Average age of people:", average_age)

    index_people_by_name = {
        p.name: p
        for p in people
    }
    print(index_people_by_name.get("Luca"))

    
def squared_greater_than(numbers, threshold):
    return [n**2 for n in numbers if n > threshold]

def sum_numbers(numbers):
    return sum(numbers)

def sum_squared_numbers_grater_than(numbers, threshold): 
    return sum([n**2 for n in numbers if n > threshold])

def greater_than(numbers, threshold):
    return [n for n in numbers if n > threshold]


In Python:
    - il tipo è una promessa
    - la violazione è una rottura semantica, non tecnica

def sum_numbers_greater_than(numbers: list[int], threshold: int) -> int:
    total = 0

    for n in numbers:
        if n > threshold:
            total += n

    return total


def build_dictionary_from_list(items, key_field, value_field):
    return {
        item[key_field]: item[value_field] 
        for item in items
    }

def print_dictionary(d):
    for key, value in d.items():
        print(f"{key}: {value}")

def build_dictionary_from_list_with_threshold(
        item: list[dict], 
        threshold: int, 
        key_field: str, 
        value_field: str
) -> dict[str, int]:
    return {
        p[key_field]: p[value_field]
        for p in item
        if p[value_field] >= threshold
    }

def average(values):
    total = sum(values)
    count = len(values)
    return total / count if count > 0 else 0.0

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def is_adult(self) -> bool:
        return self.age >= 18
    def __str__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"
    def __repr__(self) -> str:
        return self.__str__()

if __name__ == "__main__":
    main()
'''