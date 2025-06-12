from app.database import get_connection

def update_fee_payment(nfc_id, fee_type, new_amount):
    try:
        fee_map = {
            "1": "tuition_paid",
            "2": "hostel_paid",
            "3": "transport_paid"
        }

        if fee_type not in fee_map:
            print("❌ Invalid fee type.")
            return

        column_name = fee_map[fee_type]

        conn = get_connection()
        cursor = conn.cursor()

        # Get current paid value
        cursor.execute(f"SELECT {column_name} FROM students WHERE nfc_id = %s", (nfc_id,))
        result = cursor.fetchone()

        if result is None:
            print("❌ Student not found.")
            return

        current_paid = float(result[0]) if result[0] else 0
        updated_paid = current_paid + float(new_amount)

        # Update the student record
        cursor.execute(f"""
            UPDATE students SET {column_name} = %s
            WHERE nfc_id = %s
        """, (updated_paid, nfc_id))

        # Insert into payment history
        cursor.execute("""
            INSERT INTO payment_history (nfc_id, fee_type, amount_paid)
            VALUES (%s, %s, %s)
        """, (nfc_id, column_name.replace("_paid", ""), new_amount))

        conn.commit()
        print(f"✅ {column_name.replace('_', ' ').title()} updated successfully to ₹{updated_paid}.")

    except Exception as e:
        print(f"❌ Update failed: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()