# doctor.py

class Doctor:
    def __init__(self, doctor_id, doctor_name, degree, specialization, joining_year, experience,
                 current_serving_patients):
        self.doctor_id = doctor_id
        self.doctor_name = doctor_name
        self.degree = degree
        self.specialization = specialization
        self.joining_year = joining_year
        self.experience = experience
        self.current_serving_patients = current_serving_patients

    def display_info(self):
        print("\n---------- Doctor's Details ----------")
        print(f"Doctor ID : {self.doctor_id}")
        print(f"Name : {self.doctor_name}({self.degree})")
        print(f"Specialization : {self.specialization}")
        print(f"Joining Year : {self.joining_year}")
        print(f"Experience : {self.experience}")
        print(f"Patients under care : {self.current_serving_patients}")