import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Data_structure.strucure import Hash
from models.User import User
Hash_Data = Hash()
with open('FinalProject/TestFile/users.txt','r') as info:
    for line in info:
        national,name,lname,date,password = line.rstrip().split(' | ')
        new_User =User(national,name,lname,date,password)
        Hash_Data.insert(new_User.National,new_User)

with open('FinalProject/TestFile/drivers.txt','r') as driver:
    for line in driver:
        national,DriverID,Date = line.rstrip().split(' | ')
        Nodedriver  = Hash_Data.search(national)
        Nodedriver.license = DriverID
        Nodedriver.Datelicense = date 
        Nodedriver.StatusDriver = True
with open('FinalProject/TestFile/phase4.txt','r') as point:
    for line in point:
        national,DriverID,Negative = line.rstrip().split(' | ')
        Nodedriver = Hash_Data.search(national)
        Nodedriver.negative = int(Negative)
        if int(Negative) >= 500:
            Nodedriver.StatusDriver = False





