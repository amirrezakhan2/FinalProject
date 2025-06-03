import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DataBase.CityNumber import Hash_Data
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
def login():
    National = int(input('Enter the National code:\n'))
    if check_National(National) != True:
        return False, print('your National code is on wrong Format')
    else:

        check_Username = Hash_Data.search(National)

        if check_Username:
                User_Password = input('Enter your Password :\n')
                if check_Password(User_Password) == True:

                    if check_Username.Password == User_Password:
                        return True,check_Username
                    else:
                        return False,print('Password dose not match')
                else:
                    return False,print('Password dos not have right Format')
        else:
            return False,print('your National code dose not exist')



