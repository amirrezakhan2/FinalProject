from Data_structure.strucure import DynamicArray
from datetime import datetime

class NodePoint:
    def __init__(self, license, Datelicense, National):
        self.License = license
        self.DateLicense = Datelicense
        self.National = National
        self.Negative = 0
        self.Point = 0 

pointDrive = DynamicArray()


with open('FinalProject/TestFile/drivers.txt', 'r') as File:
    for line in File:
        Nationalcode, serial, Date = line.strip().split(' | ')
        date_object = datetime.strptime(Date, '%Y-%m-%d')
        newNode = NodePoint(serial, date_object, Nationalcode)
        pointDrive.insert(newNode)


with open('FinalProject/TestFile/phase4.txt', 'r') as File:
    for line in File:
        Code, serial, negative = line.strip().split(' | ')
        for i in range(len(pointDrive)):
            if pointDrive[i].National == Code:
                pointDrive[i].Negative = int(negative)
def quick_sort_by_point(arr, low, high):
    if low < high:
        pi = partition_by_point(arr, low, high)
        quick_sort_by_point(arr, low, pi - 1)
        quick_sort_by_point(arr, pi + 1, high)

def partition_by_point(arr, low, high):
    pivot = arr[high].Point
    i = low - 1
    for j in range(low, high):
        if arr[j].Point >= pivot:  
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

for i in range(len(pointDrive)):
    for j in range(i+1,len(pointDrive)):
        if pointDrive[i].DateLicense < pointDrive[j].DateLicense and pointDrive[i].Negative <= pointDrive[j].Negative:
            pointDrive[i].Point += 1
quick_sort_by_point(pointDrive,0,len(pointDrive)-1)
for i in range(len(pointDrive)):
    print(f"License: {pointDrive[i].License}, Negative: {pointDrive[i].Negative}, Point: {pointDrive[i].Point}")

