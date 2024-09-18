# patient.py

class Patient:
    def __init__(self, patient_id, name, age, gender, contact_info, address, serving_doctor_name, bed_number):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_info = contact_info
        self.address = address
        self.serving_doctor_name = serving_doctor_name
        self.bed_number = bed_number

    def display_info(self):
        print("\n---------- Patient Information ----------")
        print(f"Patient ID : {self.patient_id}")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Contact Information : {self.contact_info}")
        print(f"Address : {self.address}")
        print(f"Serving Doctor Name : Mr/Mrs/Ms.{self.serving_doctor_name} ")
        print(f"Bed Number : {self.bed_number}")