def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    threshold = 5

    grades = [
        {"name": "Anna", "grade": 28},
        {"name": "Luca", "grade": 18},
        {"name": "Marco", "grade": 30},
        {"name": "Simona", "grade": 15},
    ]

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

    


def squared_greater_than(numbers, threshold):
    return [n**2 for n in numbers if n > threshold]

def sum_numbers(numbers):
    return sum(numbers)

def sum_squared_numbers_grater_than(numbers, threshold): 
    return sum([n**2 for n in numbers if n > threshold])

def greater_than(numbers, threshold):
    return [n for n in numbers if n > threshold]

'''
In Python:
    - il tipo è una promessa
    - la violazione è una rottura semantica, non tecnica

def sum_numbers_greater_than(numbers: list[int], threshold: int) -> int:
    total = 0

    for n in numbers:
        if n > threshold:
            total += n

    return total
'''

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

if __name__ == "__main__":
    main()
