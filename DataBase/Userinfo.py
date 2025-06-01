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
# for i in range(len(Hash_Data)):
#     if Hash_Data[i] != None:
#         print(Hash_Data[i])

