#Class is a blueprint of an object
#An object is an instance of a class

class student:

    #Attributes
    name = "Mbuche"
    age = 18
    gender = ("Female")

    #Behaviour/Functions/Methods
    def study(self):
        print("The student is studying")

    def jokes(self):
        print("The student is joking")

#creating Objects
student1 = student()
print(student1.name)


student2 = student()
student3 = student()
