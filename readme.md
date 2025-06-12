# 🎓 Student Fee Management via NFC

A simple Python-based system to enroll students, check fee status, and generate receipts — backed by MySQL.

## 🚀 Features

- NFC ID-based student enrollment
- Admin and student login
- Fee status check (tuition, hostel, transport)
- Payment history tracking
- PDF receipt generation and export

## 🛠 Tech Stack

- Python 3
- MySQL
- mysql-connector-python
- fpdf2 (for generating PDF receipts)

## 📂 Folder Structure

student/
├── app/
│   ├── auth.py
│   ├── database.py
│   ├── enroll.py
│   ├── history.py
│   ├── query.py
│   ├── receipt.py
│   ├── student_list.py
│   └── update.py
│
├── data/
│   └── schema.sql
│
├── receipts/                 # 📄 Stores exported PDF fee receipts
│
├── LICENSE
├── main.py
├── README.md
├── requirements.txt


## 📦 Setup Instructions

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt


2. **Creating database**:
     ---

## 📥 How to Import SQL Schema

To set up the database with the required tables:

### 🔸 Method 1: Using MySQL CLI

```bash
# Log in to MySQL
mysql -u root -p

# Inside MySQL prompt
CREATE DATABASE student_fee;
USE student_fee;

# Exit and import the schema
exit
mysql -u root -p student_fee < data/schema.sql

3. **run the system**:

   python3 main.py
   