#Anthony Antognazzi
#Python 2018SP CSC-221-01IN
#AntognazziA_medical_classes

class Patient: #Define the class to hold the patient info
    def __init__(self,first_name,middle_name,last_name,address,city,state,zip_code,phone_number,emg_contact,emg_number): #Initialize the class and accept arguments
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__phone_number = phone_number
        self.__emg_contact = emg_contact
        self.__emg_number = emg_number


#Acessor methods for each of the values
    def get_first_name(self):
        return self.__first_name
    def get_middle_name(self):
        return self.__middle_name
    def get_last_name(self):
        return self.__last_name
    def get_address(self):
        return self.__address
    def get_city(self):
        return self.__city
    def get_state(self):
        return self.__state
    def get_zip_code(self):
        return self.__zip_code
    def get_phone_number(self):
        return self.__phone_number
    def get_emg_contact(self):
        return self.__emg_contact
    def get_emg_number(self):
        return self.__emg_number

#Mutator methods for each of the values
    def set_first_name(self,value):
        self.__first_name = value
    def set_middle_name(self,value):
        self.__middle_name = value
    def set_last_name(self,value):
        self.__last_name = value
    def set_address(self,value):
        self.__address = value
    def set_city(self,value):
        self.__city = value
    def set_state(self,value):
        self.__state = value
    def set_zip_code(self,value):
        self.__zip_code = value
    def set_phone_number(self,value):
        self.__phone_number = value
    def set_emg_contact(self,value):
        self.__emg_contact = value
    def set_emg_number(self,value):
        self.__emg_number = value


class Procedure: #Create the class to hold the procedures
    def __init__(self,name,date,practicioner,charges): #initialize and accept arguments
        self.__name = name
        self.__date = date
        self.__practicioner = practicioner
        self.__charges = charges

#Acessor methods:
    def get_name(self):
        return self.__name
    def get_date(self):
        return self.__date
    def get_practicioner(self):
        return self.__practicioner
    def get_charges(self):
        return self.__charges

#Mutator methods:
    def set_name(self,value):
        self.__name = value
    def set_date(self,value):
        self.__date = value
    def set_practicioner(self,value):
        self.__practicioner = value
    def set_charges(self,value):
        self.__charges = value
