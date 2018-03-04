#Anthony Antognazzi
#Python 2018SP CSC-221-01IN
#Car Class

class Car: #define the class
    __year_model = 0
    __make = ""

    def __init__(self,year,make):
        __year_model = year
        __make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed+=5

    def brake(self):
        self.__speed -=5

    def get_speed(self):
        return self.__speed
