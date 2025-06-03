import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DataBase.CityNumber import Hash_Data
from DataBase.CarData import CarBST
def SeeCar(National):
    count = 0
    Carinfo = Hash_Data.search(National).Linklist_Plate
    temp = Carinfo.head
    if temp == None :
        return print('you dont Have any Car')
    else:
        while temp:
            if temp.data.serial == None:
                pass
            else:
                count += 1
                print(CarBST.search(temp.data.serial))
            temp = temp.next
        if count == 0:
                return print('you dont Have any Car')

    
