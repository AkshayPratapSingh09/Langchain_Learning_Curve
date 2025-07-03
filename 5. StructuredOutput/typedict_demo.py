from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int

new_person: Person = {'name':'akshay', 'age':20}

print(new_person)
print(type(new_person))