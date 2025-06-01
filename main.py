from DataBase.CityNumber import City_Array
from Data_structure.strucure import Array
from models.Plate import PlateNode
import random
import string

class MakePlate:
    def __init__(self):
        pass
    def plateMaker(self):
        letter = random.choice(string.ascii_uppercase)
        while True:
            if letter == 'P' or letter == 'D':
                letter = random.choice(string.ascii_uppercase) 
            else:
                break
        if letter == 'X':
            odd = Array(5)
            for i in range(10):
                if i % 2 != 0:
                    odd.insert(i)
            number = ''
            for i in range(len(odd)):
                c = random.randint(0,4)
                number += str(odd[c])
            while self.checkPlate(number) == False:
                number = ''
                for i in range(len(odd)):
                     c = random.randint(0,4)
                     number += str(odd[c])
            else:
                key = number[0:2] + str(ord(letter)) + number[2:5]
                plate_that_make = number[0:2] + (letter) + number[2:5]

                return key,plate_that_make
            
        number = str(random.randint(10000, 99999))
        while self.checkPlate(number) == False:
            number = str(random.randint(10000, 99999))
        else:
            key = number[0:2] + str(ord(letter)) + number[2:5]
            plate_that_make = number[0:2] + (letter) + number[2:5]
            return key,plate_that_make
        

    def checkPlate(self,number):
        number_array = Array(5)
        difference = 0
        for i in number:
            number_array.insert(int(i))
        for i in range(1,len(number_array)):
            difference += number_array[i-1]-number_array[i]
        if difference == 4 or difference == -4 or difference == 0:
            return False
        else:
            return True
 






 