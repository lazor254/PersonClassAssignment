class person:
    def __init__(self, name, age, gender):
        self.name = name 
        self.age = age 
        self.gender = gender 

    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old and  I identify as {self.gender}")

#instance of the person
person = person("Lazor", 25, "male")

person.introduce()