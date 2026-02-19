

class Dog:
    
    def __init__(self,breed, age, colour):
        self.breed = breed
        self.age = age
        self.colour = colour

    def speak(self):
        print("Dog is Barking")


dog1 = Dog("German shepherd",3,"grey")
print(dog1.breed, dog1.age, dog1.colour)

dog2 = Dog("Siberian Husky",4,"blue")
print(dog2.breed, dog2.age, dog2.colour)

dog3 = Dog("Chihuahua",5,"pitch")
print(dog3.breed, dog3.age, dog3.colour)
