CREATE TABLE IF NOT EXISTS student (
    nfc_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    total_fee DECIMAL(10,2) NOT NULL,
    fee_paid DECIMAL(10,2) NOT NULL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
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
