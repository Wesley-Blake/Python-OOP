class Person:
    hair = "Brown"
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        print(f"Name: {self._name}")

class Father(Person):
    def __init__(self, name):
        self._gender = "Male"
        super().__init__(name)
    @property
    def gender(self):
        print(self._gender)
    def speak(self, input: str) -> str:
        print(f"Yo! {input}")
    
class Mother(Person):
    def __init__(self, name):
        self._gender = "Female"
        super().__init__(name)
    @property
    def hair_color(self):
        print(f"Hair color: {self.hair}")
    @property
    def gender(self):
        print(self._gender)
    def speak(self, input: str) -> str:
        print(f"Hi! {input}")

class Child(Mother, Father):
    def __init__(self, name):
        super().__init__(name)

if __name__ == '__main__':
    print("Person test!")
    person = Person("guy")
    print(person.hair)
    person.name
    print("Done")
    print()
    print("Father test!")
    father = Father("John")
    print(father.hair)
    father.name
    father.gender
    father.speak("Nice!")
    print("Done")
    print()
    print("Mother test!")
    mother = Mother("Julie")
    mother.hair_color
    mother.name
    mother.gender
    mother.speak("This is nice!")
    print("Done")
    print()
    print("Child diomand problem!")
    child = Child("Heather")
    child.hair_color
    child.name
    child.gender
    child.speak("This should be Hi!")
    print()
    print("Changing hair for classes.")
    mother.hair = "Blonde"
    print(person.hair)
    print(father.hair)
    print(mother.hair)
    print()
    print("Changing hair for classes.")
    person.hair = "Blonde"
    print(person.hair)
    print(father.hair)
    print(mother.hair)
