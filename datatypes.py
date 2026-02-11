
age = 18   #Integer
temperature = 36.89   #Float
greeting = "Hello!"  #string
isMarried = True  #Boolean

print("I'm",age,"years old")
print("The body temperature of the patient is",temperature)
print(greeting,"Mbuche")
print("Are you married? ;",isMarried)


#data structures - multiple values stored in a single variable
cars = ["Toyota", "Mercedes", "Audi", "BMW"] #List Ordered and changeable
languages = ["Python","Java","C++"]


fruits = ("Aple","Cherry","Grapes", "pineapple") #Tuple - ordered and unchangeable
countries = {"Italy","Germany","Germany","Spain","France"} #set - Unordered and unchangeable
student = {
    "firstname" : "Eric Kanai",
    "age" : 20,
    "course" : "fullstack",
    "gender" : "Male",
}#Dictionary


print(cars)
print(countries)
print(fruits)
print(student)
print(student["firstname"])
print(student["age"])
print(student["course"])

#Typecasting - Converting from one datatype to another
print(int(temperature))

x = int(1)
y = int(2.8)
z = int("3")

l = float(3)
m = float("3")

e = str(2)



