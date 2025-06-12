# app/auth.py

import mysql.connector
import getpass
from app.database import get_connection

def admin_login():
    username = input("Admin username: ")
    password = getpass.getpass("Admin password: ")

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admins WHERE username=%s AND password=%s", (username, password))
        admin = cursor.fetchone()
        cursor.close()
        conn.close()
        return admin is not None

    except mysql.connector.Error as err:
        print(f"❌ Login failed: {err}")
        return False
def student_login():
    conn = None  # ✅ initialize conn to avoid UnboundLocalError
    try:
        username = input("Enter username: ").strip()
        password = getpass.getpass("Enter password: ").strip()

        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT nfc_id FROM student_accounts WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            print("✅ Login successful.")
            return result[0]
        else:
            print("❌ Invalid username or password.")
            return None

    except Exception as e:
        print(f"❌ Login error: {e}")
        return None

    finally:
        if conn:  # ✅ only close if connection was successful
            conn.close()