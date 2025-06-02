import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DataBase.Userinfo import Hash_Data
from models.User import User

def check_National(code):
    code = str(code)
    if len(code) == 10:
        for i in code:
            if i.isalpha():
                return False
        else:
            return True
    else:
        return False
def check_Password(Pword):
    count = 0 
    if len(Pword) == 8:
        for i in Pword:
            if i.isalpha():
                count +=1 
        if count == 8 or count == 0:
            return False
        else:
          return True
    else:
        return False
def UserPanel():
    National_code =  int(input('Enter your National Code:\n'))
    if check_National(National_code) == True:
        Search_Natinoal = Hash_Data.search(National_code)
        if Search_Natinoal:
            Pword = input('Enter your Password:\n')
            if Search_Natinoal.Password == Pword:
                print(f'{Search_Natinoal.Name} welcome Back ' )
            else:
                 return False,print('Your Password is wrong')
        else:
            Password_User = input('Enter your Password,Password must have digit and alphabetic and len must be 8:\n')
            if check_Password(Password_User) == True:
                name = input('Enter your name:\n')
                Lname = input('Enter your Lastname:\n')
                Birthday = input('Enter your Birthday:Plese Enter in ZZZZ-XX-HH format\n')
                new_User = User(National_code,name,Lname,Birthday,Password_User)
                Hash_Data.insert(new_User.National,new_User)
                return True,new_User
    else:
        return False,print('Your National code have Problem Please check it')



        



    

