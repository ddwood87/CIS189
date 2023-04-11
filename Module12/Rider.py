"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 12
Topic: 3
Assignment: Abstract Class
Date: 04/10/2023
"""
from abc import ABC, abstractmethod

class Rider(ABC):
    def ride(self):
        raise NotImplementedError
    
    def rider(self):
        raise NotImplementedError
    
class Bicycle(Rider):
    def ride(self):
        print("Human powered, not enclosed")
    def rider(self):
        print("1 or 2 if tandem or a daredevil")

class Motorcycle(Rider):
    def ride(self):
        print("Engine powered, not enclosed")
    def rider(self):
        print("1 or 2")

class Car(Rider):
    def ride(self):
        print("Engine powered, enclosed")
    def rider(self):
        print("1 plus comfortably")

if __name__ == '__main__':
    bicycle = Bicycle()
    motorcycle = Motorcycle()
    car = Car()

    bicycle.ride()
    bicycle.rider()
    print()
    motorcycle.ride()
    motorcycle.rider()
    print()
    car.ride()
    car.rider()