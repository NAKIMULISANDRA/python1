class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"The name is {self.name}"   
person1 = person('john',70)
the_second_person = person('Jane Doe',15)
print(person1)

    