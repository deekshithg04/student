from app.database import get_connection
from fpdf import FPDF
import os
from datetime import datetime
def generate_receipt(nfc_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name, tuition_total, tuition_paid, hostel_total, hostel_paid, transport_total, transport_paid, enrollment_date FROM students WHERE nfc_id = %s", (nfc_id,))
        result = cursor.fetchone()
        if result:
            name, t_total, t_paid, h_total, h_paid, tr_total, tr_paid, enroll_date = result
            print("\n📄 Fee Receipt")
            print("---------------")
            print(f"Name: {name}")
            print(f"NFC ID: {nfc_id}")
            print(f"Enrollment Date: {enroll_date}")
            print(f"Tuition Fee Paid: ₹{t_paid} / ₹{t_total}")
            print(f"Hostel Fee Paid: ₹{h_paid} / ₹{h_total}")
            print(f"Transport Fee Paid: ₹{tr_paid} / ₹{tr_total}")
            print("---------------")
        else:
            print("⚠️ No student found with that NFC ID.")
    except Exception as e:
        print(f"❌ Error generating receipt: {e}")
    finally:
        conn.close()
from fpdf import FPDF
from datetime import datetime

def export_fee_receipt(nfc_id):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name, tuition_total, tuition_paid, hostel_total, hostel_paid, transport_total, transport_paid, enrollment_date FROM students WHERE nfc_id = %s", (nfc_id,))
        result = cursor.fetchone()

        if result:
            name, t_total, t_paid, h_total, h_paid, tr_total, tr_paid, enroll_date = result
            
            pdf = FPDF()
            pdf.add_page()
            pdf.add_font("ArialUnicode", "", "/System/Library/Fonts/Supplemental/Arial Unicode.ttf", uni=True)
            pdf.set_font("ArialUnicode", size=12)

            pdf.cell(200, 10, txt="📄 Fee Receipt", ln=True, align="C")
            pdf.ln(10)

            pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
            pdf.cell(200, 10, txt=f"NFC ID: {nfc_id}", ln=True)
            pdf.cell(200, 10, txt=f"Enrollment Date: {enroll_date}", ln=True)
            pdf.ln(5)
            pdf.cell(200, 10, txt=f"Tuition Fee Paid: ₹{t_paid} / ₹{t_total}", ln=True)
            pdf.cell(200, 10, txt=f"Hostel Fee Paid: ₹{h_paid} / ₹{h_total}", ln=True)
            pdf.cell(200, 10, txt=f"Transport Fee Paid: ₹{tr_paid} / ₹{tr_total}", ln=True)

            
            os.makedirs("receipts", exist_ok=True)
            filename = f"receipts/receipt_{nfc_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            pdf.output(filename)
            print(f"✅ Fee receipt exported successfully as {filename}")
        else:
            print("⚠️ No student found with that NFC ID.")
    except Exception as e:
        print(f"❌ Error exporting receipt: {e}")
    finally:
        if conn:
            conn.close()