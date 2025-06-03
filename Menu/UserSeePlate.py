import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DataBase.CityNumber import Hash_Data
def SeePlate(Natinal):
    PlateInfo = Hash_Data.search(Natinal).Linklist_Plate 
    temp = PlateInfo.head 
    if temp == None:
        return print('you do not have any plate')
    while temp :
        print(temp.data)
        temp = temp.next


