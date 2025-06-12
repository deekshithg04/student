# app/enroll.py

from app.database import get_connection
import mysql.connector

def enroll_student(nfc_id, name, tuition_total, tuition_paid, hostel_total, hostel_paid, transport_total, transport_paid):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO students (nfc_id, name, tuition_total, tuition_paid, hostel_total, hostel_paid, transport_total, transport_paid)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (nfc_id, name, tuition_total, tuition_paid, hostel_total, hostel_paid, transport_total, transport_paid))
        conn.commit()
        print("✅ Student enrolled successfully.")
    except mysql.connector.Error as err:
        print(f"❌ Failed to enroll student: {err}")
    finally:
        cursor.close()
        conn.close()

def update_fee_payment(nfc_id, fee_type, new_paid):
    fee_column = {
        "1": "tuition_paid",
        "2": "hostel_paid",
        "3": "transport_paid"
    }.get(fee_type)

    if not fee_column:
        print("❌ Invalid fee type.")
        return

    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = f"UPDATE students SET {fee_column} = %s WHERE nfc_id = %s"
        cursor.execute(query, (new_paid, nfc_id))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Updated {fee_column.replace('_', ' ').title()} for NFC ID {nfc_id}.")
        else:
            print("❌ Student not found.")
    except mysql.connector.Error as err:
        print(f"❌ Update failed: {err}")
    finally:
        cursor.close()
        conn.close()