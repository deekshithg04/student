import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="192.168.119.107",      # your remote laptop IP
        user="deekshith",         # your MySQL user
        password="Cherry@0826", # your MySQL password
        database="student",
        port=3306
    )