# Import the required classes from different files
from appointment import Appointment
from doctor import Doctor
from billing import Billing
from patient import Patient

# Lists to store patients, doctors, appointments, and bills
patients = []
doctors = []
appointments = []
bills = []


def register_patient():  # Function to register a new patient
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = int(input("Enter Patient Age: "))
    gender = input("Enter Patient Gender: ")
    contact_info = int(input("Enter Contact Info: "))
    address = input("Enter the patient's address : ")
    serving_doctor_name = input("Name of the serving doctor : ")
    bed_number = int(input("Enter the Bed Number : "))
    patient = Patient(patient_id, name, age, gender, contact_info, address, serving_doctor_name, bed_number)
    patients.append(patient)
    print("Patient registered successfully!")


def register_doctor():  # Function to register a new doctor
    doctor_id = input("Enter Doctor ID: ")
    doctor_name = input("Enter Doctor Name: ")
    degree = input("Enter Doctor's Degree: ")
    specialization = input("Enter Specialization: ")
    joining_year = int(input("Enter Joining Year: "))
    experience = int(input("Enter Years of Experience: "))
    current_serving_patients = int(input("Enter Current Serving Patients: "))
    doctor = Doctor(doctor_id, doctor_name, degree, specialization, joining_year, experience, current_serving_patients)
    doctors.append(doctor)
    print("Doctor registered successfully!")


def schedule_appointment():  # Function to schedule an appointment
    appointment_id = input("Enter Appointment ID: ")
    patient_name = input("Enter Patient Name: ")
    doctor_name = input("Enter Doctor Name: ")
    date = input("Enter Date (YYYY-MM-DD): ")
    time = input("Enter Time (e.g., 10:30 AM): ")
    reason = input("Enter Reason for Appointment: ")
    appointment_fee = float(input("Enter Appointment Fee: "))
    appointment = Appointment(appointment_id, patient_name, doctor_name, date, time, reason, appointment_fee)
    appointments.append(appointment)
    print("Appointment scheduled successfully!")


def generate_bill():  # Function to generate a bill
    billing_id = input("Enter Billing ID: ")
    patient_name = input("Enter Patient Name: ")
    patient = next((p for p in patients if p.name == patient_name), None)
    if patient is None:
        print("Patient not found!")
        return
    consultation_fee = float(input("Enter Consultation Fee: "))
    medicine_fee = float(input("Enter Medicine Fee: "))
    room_fee = float(input("Enter Room Fee: "))
    bill = Billing(billing_id, patient, consultation_fee, medicine_fee, room_fee)
    bills.append(bill)
    print("Bill generated successfully!")


def view_patients():  # Function to view all registered patients
    if not patients:
        print("No patients registered.")
    else:
        for patient in patients:
            patient.display_info()


def view_doctors():  # Function to view all registered doctors
    if not doctors:
        print("No doctors registered.")
    else:
        for doctor in doctors:
            doctor.display_info()


def view_appointments():  # Function to view all scheduled appointments
    if not appointments:
        print("No appointments scheduled.")
    else:
        for appointment in appointments:
            appointment.display_info()


def view_bills():  # Function to view all bills
    if not bills:
        print("No bills generated.")
    else:
        for bill in bills:
            bill.display_bill()


def main():
    while True:
        print("\nHospital Management System")
        print("1. Register Patient")
        print("2. Register Doctor")
        print("3. Schedule Appointment")
        print("4. Generate Bill")
        print("5. View Patients")
        print("6. View Doctors")
        print("7. View Appointments")
        print("8. View Bills")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register_patient()
        elif choice == '2':
            register_doctor()
        elif choice == '3':
            schedule_appointment()
        elif choice == '4':
            generate_bill()
        elif choice == '5':
            view_patients()
        elif choice == '6':
            view_doctors()
        elif choice == '7':
            view_appointments()
        elif choice == '8':
            view_bills()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()