
from employee import Employee


class Manager(Employee):
    def __init__(self, name="John Doe", employee_id="M001", hourly_wage=50.0, hours_worked=160, team_size=5,
                 bonuses=0.0, deductions=0.0):
        super().__init__(name, employee_id, hourly_wage, hours_worked, bonuses, deductions)
        self.team_size = team_size

    def save_to_db(self, cursor, conn):
        super().save_to_db(cursor, conn, 'Manager', str(self.team_size))
