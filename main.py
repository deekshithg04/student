from app.enroll import enroll_student
from app.query import check_fee_status
from app.receipt import generate_receipt, export_fee_receipt
from app.auth import admin_login
from app.update import update_fee_payment 
from app.history import view_payment_history

def admin_menu():
    while True:
        print("\n🔐 Admin Panel")
        print("1. Enroll Student")
        print("2. Check Fee Status")
        print("3. Generate Fee Receipt")
        print("4. Update Fee Payment")
        print("5. View Payment History")  # 👈 New Option
        print("6. View Enrolled Students")
        print("7. Logout")
        choice = input("Choose an option: ")

        if choice == "1":
            nfc_id = input("Enter NFC ID: ")
            name = input("Enter student name: ")
            tuition_total = float(input("Enter tuition fee total: "))
            tuition_paid = float(input("Enter tuition fee paid: "))
            hostel_total = float(input("Enter hostel fee total (0 if not applicable): "))
            hostel_paid = float(input("Enter hostel fee paid: "))
            transport_total = float(input("Enter transport fee total (0 if not applicable): "))
            transport_paid = float(input("Enter transport fee paid: "))
            enroll_student(nfc_id, name, tuition_total, tuition_paid, hostel_total, hostel_paid, transport_total, transport_paid)

        elif choice == "2":
            nfc_id = input("Enter NFC ID: ")
            check_fee_status(nfc_id)

        elif choice == "3":
            nfc_id = input("Enter NFC ID: ")
            generate_receipt(nfc_id)

        elif choice == "4":
            nfc_id = input("Enter NFC ID: ")
            print("1. Tuition Fee")
            print("2. Hostel Fee")
            print("3. Transport Fee")
            fee_type = input("Which fee to update? ")
            try:
                new_amount = float(input("Enter new paid amount: "))
                update_fee_payment(nfc_id, fee_type, new_amount)
                print("✅ Fee update process completed.")
            except ValueError:
                print("❌ Invalid amount entered.")

        elif choice == "5":
            print("1. View All Payments")
            print("2. Filter by NFC ID")
            sub = input("Choose an option: ").strip()
            if sub == "1":
              view_payment_history()
            elif sub == "2":
              nfc_id = input("Enter NFC ID to filter: ")
              view_payment_history(nfc_id)
            else:
              print("❌ Invalid option.")

        elif choice == "6":
            from app.student_list import view_all_students_detailed
            view_all_students_detailed()

        elif choice == "7":
            print("🔒 Logged out.")
            break
        else:
            print("❌ Invalid choice!")

def student_menu(nfc_id):
    while True:
        print("\n📘 Student Panel")
        print("1. Check Fee Status")
        print("2. Generate Fee Receipt")
        print("3. View Payment History")
        print("4. Export Fee Receipt to PDF")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            check_fee_status(nfc_id)

        elif choice == "2":
            generate_receipt(nfc_id)  # ONLY prints to terminal

        elif choice == "3":
            view_payment_history(nfc_id)

        elif choice == "4":
            export_fee_receipt(nfc_id)  # ONLY generates PDF if they want

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice!")

# ✅ Only this part is changed:
def main():
    print("Welcome to the Student Fee Management System")
    print("1. Admin Login")
    print("2. Student Login")
    mode = input("Enter your choice (1 or 2): ").strip()

    if mode == "1":
        if admin_login():
            admin_menu()
        else:
            print("❌ Access Denied.")
    elif mode == "2":
        from app.auth import student_login
        nfc_id = student_login()
        if nfc_id:
           student_menu(nfc_id)
    else:
        print("❌ Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()