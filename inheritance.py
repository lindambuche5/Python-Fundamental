
#Parent/Base/Super Class
class Animal:
    def sound(self):
        print("I'm Animal making a sound")

#Child/Derived/Sub Class
class Cat(Animal):
    def climb(self):
        print("I'm a Cat climbing")

class Dog(Animal):
    def chew(self):
        print("I'm a Dog chewing")

a = Animal()


mycat = Cat()


mydog = Dog()