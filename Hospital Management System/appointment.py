# appointment.py

class Appointment:
    def __init__(self, appointment_id, patient_name, doctor_name, date, time, reason, appointment_fee):
        self.appointment_id = appointment_id
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.date = date
        self.time = time
        self.reason = reason
        self.appointment_fee = appointment_fee

    def display_info(self):
        print("\n---------- Appointment Details ---------")
        print(f"Appointment ID : {self.appointment_id}")
        print(f"Patient Name : {self.patient_name}")
        print(f"Doctor Name : {self.doctor_name}")
        print(f"Date : {self.date}")
        print(f"Time : {self.time}")
        print(f"Reason : {self.reason}")
        print(f"Appointment Fee : ;{self.appointment_fee}")