
class Employee:
    def __init__(self, name="John Doe", employee_id="E001", hourly_wage=20.0, hours_worked=160, bonuses=0.0,
                 deductions=0.0):
        self.name = name
        self.employee_id = employee_id
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.bonuses = bonuses
        self.deductions = deductions

    def calculate_monthly_salary(self):
        base_salary = self.hourly_wage * min(self.hours_worked, 160)
        overtime = max(self.hours_worked - 160, 0) * (self.hourly_wage * 1.5)
        total_salary = base_salary + overtime + self.bonuses - self.deductions
        return total_salary

    def add_bonus(self, amount):
        self.bonuses += amount

    def add_deduction(self, amount):
        self.deductions += amount

    def generate_payslip(self):
        salary = self.calculate_monthly_salary()
        payslip = f"--- Payslip for {self.name} ---\n"
        payslip += f"Employee ID: {self.employee_id}\n"
        payslip += f"Hourly Wage: {self.hourly_wage}\n"
        payslip += f"Hours Worked: {self.hours_worked}\n"
        payslip += f"Bonuses: {self.bonuses}\n"
        payslip += f"Deductions: {self.deductions}\n"
        payslip += f"Total Monthly Salary: {salary}\n"
        return payslip

    def save_to_db(self, cursor, conn, role="Employee", extra_info=""):
        cursor.execute('''
           INSERT OR REPLACE INTO employees (employee_id, name, role, hourly_wage, hours_worked, bonuses, deductions, extra_info)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)
           ''', (self.employee_id, self.name, role, self.hourly_wage, self.hours_worked, self.bonuses, self.deductions,
                 extra_info))
        conn.commit()