
import sqlite3


def setup_database():
    conn = sqlite3.connect('employee_management.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        employee_id TEXT PRIMARY KEY,
        name TEXT,
        role TEXT,
        hourly_wage REAL,
        hours_worked REAL,
        bonuses REAL,
        deductions REAL,
        extra_info TEXT
    )
    ''')

    # Create an index for fast lookups on employee_id
    cursor.execute('''
    CREATE INDEX IF NOT EXISTS idx_employee_id ON employees (employee_id)
    ''')

    conn.commit()
    return conn, cursor
