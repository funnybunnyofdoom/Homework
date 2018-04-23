#Anthony Antognazzi
#Python 2018SP CSC-221-01IN
#AntognazziA_PatientCharges

import AntognazziA_medical_classes #.Patient #Import the Patient Class
#import AntognazziA_medical_classes.Procedure #Import the Procedure Class

def main():
    Patient_one = AntognazziA_medical_classes.Patient("Bob","Nil","Belcher","5555 Ocean Avenue","Ocean City","NJ","55555","5555555555","Linda Belcher","6666666666")
    procedure_one = AntognazziA_medical_classes.Procedure("Physical Exam","3/8/2018","Dr. Irvine",250)
    procedure_two = AntognazziA_medical_classes.Procedure("X-ray","3/8/2018","Dr. Jamison", 500)
    procedure_three = AntognazziA_medical_classes.Procedure("Blood Test","3/8/2018","Dr. Smith", 200)
    display_patient(Patient_one)

    t = 0 #running total
    t += display_procedure(procedure_one)
    t += display_procedure(procedure_two)
    t += display_procedure(procedure_three)
    print("Total Charges: $",t)
    
    
def display_patient(patient_one):
    firstname = patient_one.get_first_name()
    middlename = patient_one.get_middle_name()
    lastname = patient_one.get_last_name()
    address = patient_one.get_address()
    city = patient_one.get_city()
    zipcode = patient_one.get_zip_code()
    phnum = patient_one.get_phone_number()
    emgcontact = patient_one.get_emg_contact()
    emgnumber = patient_one.get_emg_number()

    print("First Name: ",firstname)
    print("Middle Name: ", middlename)
    print("Last Name: ", lastname)
    print("Address: ", address)
    print("city: ",city)
    print("zipcode: ",zipcode)
    print("phnum: ",phnum)
    print("emgcontact: ",emgcontact)
    print("emgnumber: ",emgnumber)


def display_procedure(procedure):
    name = procedure.get_name()
    date = procedure.get_date()
    practicioner = procedure.get_practicioner()
    charges = procedure.get_charges()

    print("====================")
    print("Procedure: ",name)
    print("Date: ",date)
    print("Practicioner: ",practicioner)
    print("Charges: $",charges)
    print('\n')

    return charges
main()
