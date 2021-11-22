"""Flie where clases are stored"""

class Person():
    def __init__(self, name: str, age: int) -> None:
        """Person Class representing a name and an age
        
        Args:
            name: Name of the person.
            age: Number of years the person has
        """
        
        self.name = name
        self.age = age

    def say_hi(self, new_person: str = "stranger"):
        """Says hi to someone and it's name
        
        Args:
            new_person: Name of the person to greet. Defaults to ``stranger``

        """
        return f"Hi {new_person}, this is {self.name}"


