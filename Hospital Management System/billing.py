# billing.py

class Billing:
    def __init__(self, billing_id, patient, consultation_fee, medicine_fee, room_fee):
        self.billing_id = billing_id
        self.patient = patient
        self.consultation_fee = consultation_fee
        self.medicine_fee = medicine_fee
        self.room_fee = room_fee

    def calculate_total(self):
        return self.consultation_fee + self.medicine_fee + self.room_fee

    def display_bill(self):
        total = self.calculate_total()
        print("\n--- Billing Information ---")
        print(f"Billing ID: {self.billing_id}")
        print(f"Patient: {self.patient.name} (ID: {self.patient.patient_id})")
        print(f"Consultation Fee: ${self.consultation_fee:.2f}")
        print(f"Medicine Fee: ${self.medicine_fee:.2f}")
        print(f"Room Fee: ${self.room_fee:.2f}")
        print(f"Total Amount: ${total:.2f}")
