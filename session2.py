class Car:
    def __init__(self,name,brand,color):
        self.name= name
        self.brand= brand
        self.color= color
    def country(self,country):
        self.country= country
    

car1=Car("toyota","vanguard","black")
car1.country("Japan")
car2=Car("forestor","subaru","silver")
car2.country("China")


print(car1.name,car1.brand,car1.color,car1.country)
print(car2.name,car2.brand,car2.color,car2.country)


class Continent:
    def even_two():
        num = 0

        while num <= 10:
            num += 1
            if num % 2 ==0:
                print(str(num) + ' Is Even')
            else:
                print(str(num) + ' Is Odd')


c1=Continent
c1.even_two()

class Animal:
    def __init__(self,name,family,color):
        self.name=name
        self.family=family
        self.color=color
    
class Domestic(Animal):
    def domestic(self):
        return True
    

a1=Animal("Lion","cat","brown")
print(a1.name)
print(a1.family)
print(a1.color)
a2=Domestic("dog","pet","black")
a2.domestic()

print(a2.name)
print(a2.family)
print(a2.color)