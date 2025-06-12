from app.database import get_connection

def check_fee_status(nfc_id):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM students WHERE nfc_id = %s", (nfc_id,))
        student = cursor.fetchone()

        if student:
            print(f"\n📘 Fee Status for {student['name']} (NFC: {nfc_id})")
            for section in ['tuition', 'hostel', 'transport']:
                total = student[f"{section}_total"]
                paid = student[f"{section}_paid"]
                due = total - paid
                print(f"🔹 {section.title()} Fee: ₹{paid:.2f} / ₹{total:.2f} (Due: ₹{due:.2f})")
        else:
            print("❌ Student not found.")
    
    except Exception as e:
        print(f"❌ Error checking fee status: {e}")
    
    finally:
        cursor.close()
        conn.close()