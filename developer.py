from employee import Employee


class Developer(Employee):
    def __init__(self, name="John Doe", employee_id="D001", hourly_wage=40.0, hours_worked=160,
                 programming_language="Python", bonuses=0.0, deductions=0.0):
        super().__init__(name, employee_id, hourly_wage, hours_worked, bonuses, deductions)
        self.programming_language = programming_language

    def save_to_db(self, cursor, conn):
        super().save_to_db(cursor, conn, 'Developer', self.programming_language)  # Call parent with correct args
