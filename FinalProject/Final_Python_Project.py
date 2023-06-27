el_type_list = [
    "phone",
    "tablet", 
    "laptop", 
    "tv",
    "gadgets"
    ]

brand_list = [
    "apple", 
    "samsung", 
    "sony"]

model_list = [
    "iphone10", 
    "iphone11", 
    "iphone12", 
    "iphone13", 
    "galaxy8", 
    "galaxy9", 
    "galaxy10",
     "galaxy20", 
     "galaxy21", 
     "xperia10", 
     "xperia1", 
     "xperia2", 
     "xperia9", 
     "ipad10", 
     "ipad11"]

job = [
"20$", 
"30$", 
"40$",
"50$", 
"60$"
]



el_type = None

brand = None

model = None

ser_number = None

import datetime

import os

current_directory = os.getcwd()


class Electron:

    def __init__(self, el_type, brand, model, ser_number):
        self.el_type = el_type
        self.brand = brand
        self.model = model
        self.__ser_number = ser_number 
        self.__description = ""
        self.__treatment_plan = ""
        if(self.el_type == "phone"):
            self.__description = self.el_type + " will be repaired "  
            self.__treatment_plan = "In order to repair your " + self.el_type + ", you have to wait and pay " + job[0]
        elif(self.el_type == "tablet"):
            self.__description = self.el_type + " will be repaired "  
            self.__treatment_plan = "In order to repair your " + self.el_type + ", you have to wait and pay " + job[1]
        elif(self.el_type == "laptop"):
            self.__description = self.el_type + " will be repaired "  
            self.__treatment_plan = "In order to repair your " + self.el_type + ", you have to wait and pay " + job[2]
        elif(self.el_type == "tv"):
            self.__description = self.el_type + " will be repaired "  
            self.__treatment_plan = "In order to repair your " + self.el_type + ", you have to wait and pay " + job[3]
        elif(self.el_type == "gadgets"):
            self.__description = self.el_type + " will be repaired "  
            self.__treatment_plan = "In order to repair your " + self.el_type + ", you have to wait and pay " + job[4]

        
    def __repr__(self):
        return f'Your Device is("{self.brand}","{self.model}")'
        
    def __fun(self):
        self.__description
        self.__treatment_plan

    def discharge(self):
        time_of_discharge = datetime.datetime.now()
        file_name = (self.el_type
                     + "_" + str(time_of_discharge.year)
                     + "_" + str(time_of_discharge.day)
                     + "_" + str(time_of_discharge.hour)
                     + "_" + str(time_of_discharge.minute)
                     + "_" + str(time_of_discharge.second) + ".txt")
        try:
            write_to_directory = "/Discharge_Files"
            file_loc = os.path.join(current_directory+write_to_directory,file_name)
            file = open(os.path.join(current_directory+write_to_directory,file_name), "a+")
        
            with open(file_loc, "r+") as f:
                f.seek(0)
                f.write(self.__description + "\n" + 
                        self.__treatment_plan)
                f.truncate()
                print("You can find discharge notes in:" + (file_loc))
        except EnvironmentError: #used if the folder cannot be found
            print("An error has occured")
        #do nothing for now
        pass



phone_d = Electron(el_type, brand, model, ser_number)
tablet_d = Electron(el_type, brand, model, ser_number)
laptop_d = Electron(el_type, brand, model, ser_number)
tv_d = Electron(el_type, brand, model, ser_number)
gadgets_d = Electron(el_type, brand, model, ser_number)


def calc_work():


    if el_type == 'phone':
        if 'phone' not in el_type_list:
            print("Sorry, we are not serving")
        else:
            print('------------------------------------------------------')
            phone_d = Electron(el_type, brand, model, ser_number)
            print("This is calculation of your service procedure!")
            print(f"your phone will be cost you with work {job[0]}$")
            print(repr(phone_d))
            phone_d.discharge()

    if el_type == 'tablet':
        if 'tablet' not in el_type_list:
            print("Sorry, we are not serving")
        else:
            print('------------------------------------------------------')
            tablet_d = Electron(el_type, brand, model, ser_number)
            print("This is calculation of your service procedure 1!")
            print(f"your tablet will be cost you with work {job[1]}$")
            print(repr(tablet_d))
            tablet_d.discharge()

    if el_type == 'laptop':
        if 'laptop' not in el_type_list:
            print("Sorry, we are not serving")
        else:
            print('------------------------------------------------------')
            laptop_d = Electron(el_type, brand, model, ser_number)
            print(repr(phone_d))
            print("This is calculation of your service procedure 2!")
            print(f"your laptop will be cost you with work {job[2]}$")
            print(repr(laptop_d))
            laptop_d.discharge()

    if el_type == 'tv':
        if 'tv' not in el_type_list:
            print("Sorry, we are not serving")
        else:
            print('------------------------------------------------------')
            laptop_d = Electron(el_type, brand, model, ser_number)
            print(repr(tv_d))
            print("This is calculation of your service procedure 2!")
            print(f"your laptop will be cost you with work {job[3]}$")
            print(repr(tv_d))
            laptop_d.discharge()

    if el_type == 'gadgets':
        if 'gadgets' not in el_type_list:
            print("Sorry, we are not serving")
        else:
            print('------------------------------------------------------')
            laptop_d = Electron(el_type, brand, model, ser_number)
            print(repr(gadgets_d))
            print("This is calculation of your service procedure 2!")
            print(f"your laptop will be cost you with work {job[4]}$")
            print(repr(gadgets_d))
            gadgets_d.discharge()


   
    
#Welcome message for the program
print("Welcome to the Repair App of electronics")
print("If you want to start app, do 'start', if you want to exit, do 'done' ")
print("If you want help, do 'help', if you want to view the credits, do 'credits'")
while True:
    num = input("Enter cmd word: ")
    if num == "done":
        break
    if num == "start":
        try:
            el_type = str(input("Enter your device type: "))
            if el_type not in el_type_list:
                print("we dont support this type")
                break
            brand = str(input("Enter your brand: "))
            if brand not in brand_list:
                print("we dont support")
                break
            model = str(input("Enter your model: "))
            if model not in model_list:
                print("we won't support")
                break
        except:
            print("Invalid input of type")
        ser_number = input("Enter your serial number:")
        calc_work()
    elif num == "help":
        for a in el_type_list:
            print("Supported type: ",a)
        for b in brand_list:
            print("Supported brand: ",b)
        for c in model_list:
            print("Supported models: ",c)
    elif num == "credits":
        print("Reapir app created by Iztore Kargabayev ")
        print("For MET-CS-521 (Information Structures with Python) at Boston University ")
        print("7th of May, 2022")
    else:
        print("Invalid command, if you don't know any commands, do 'help'")


        











    
    


