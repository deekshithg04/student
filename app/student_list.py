# app/student_list.py

from app.database import get_connection

def view_all_students_detailed():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            SELECT 
                nfc_id,
                name,
                tuition_total, tuition_paid,
                hostel_total, hostel_paid,
                transport_total, transport_paid
            FROM students
            ORDER BY name ASC
        """
        cursor.execute(query)
        students = cursor.fetchall()

        if not students:
            print("ℹ️ No students enrolled.")
            return

        print("\n📋 Enrolled Students - Full Details")
        print("=" * 100)
        for student in students:
            (
                nfc_id, name,
                tuition_total, tuition_paid,
                hostel_total, hostel_paid,
                transport_total, transport_paid
            ) = student

            tuition_due = tuition_total - tuition_paid
            hostel_due = hostel_total - hostel_paid
            transport_due = transport_total - transport_paid

            print(
                f" NFC ID: {nfc_id} |  Name: {name} | "
                f" Tuition: ₹{tuition_paid:.2f}/₹{tuition_total:.2f} (Due: ₹{tuition_due:.2f}) | "
                f" Hostel: ₹{hostel_paid:.2f}/₹{hostel_total:.2f} (Due: ₹{hostel_due:.2f}) | "
                f" Transport: ₹{transport_paid:.2f}/₹{transport_total:.2f} (Due: ₹{transport_due:.2f})"
            )
            print("-" * 100)

    except Exception as e:
        print(f"❌ Error fetching student list: {e}")
    finally:
        cursor.close()
        conn.close()