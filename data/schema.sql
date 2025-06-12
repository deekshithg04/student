CREATE TABLE IF NOT EXISTS students (
    nfc_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    tuition_total DECIMAL(10, 2) DEFAULT 0,
    tuition_paid DECIMAL(10, 2) DEFAULT 0,
    hostel_total DECIMAL(10, 2) DEFAULT 0,
    hostel_paid DECIMAL(10, 2) DEFAULT 0,
    transport_total DECIMAL(10, 2) DEFAULT 0,
    transport_paid DECIMAL(10, 2) DEFAULT 0,
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE payment_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nfc_id VARCHAR(20),
    fee_type ENUM('tuition', 'hostel', 'transport'),
    amount_paid DECIMAL(10,2),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE student_accounts (
    nfc_id VARCHAR(20) PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
