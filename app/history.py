from app.database import get_connection

def view_payment_history(nfc_id=None):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        if nfc_id:
            cursor.execute("SELECT nfc_id, fee_type, amount_paid, timestamp FROM payment_history WHERE nfc_id = %s ORDER BY timestamp DESC", (nfc_id,))
        else:
            cursor.execute("SELECT nfc_id, fee_type, amount_paid, timestamp FROM payment_history ORDER BY timestamp DESC")
        
        results = cursor.fetchall()

        if results:
            print("\n💳 Payment History:")
            print("-" * 60)
            for row in results:
                print(f"NFC ID: {row[0]} | Fee Type: {row[1]} | Amount: ₹{row[2]} | Date: {row[3]}")
            print("-" * 60)
        else:
            print("ℹ️ No payment records found.")
    except Exception as e:
        print(f"❌ Error fetching payment history: {e}")
    finally:
        conn.close()