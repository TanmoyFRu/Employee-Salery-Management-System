from employee import Employee
from manager import Manager
from developer import Developer
from database import setup_database

# Setup database connection
conn, cursor = setup_database()


def get_employee_input():
    name = input("Enter employee name (default: John Doe): ") or "John Doe"
    employee_id = input("Enter employee ID (default: E001): ") or "E001"
    try:
        hourly_wage = float(input("Enter hourly wage (default: 20.0): ") or 20.0)
        hours_worked = float(input("Enter hours worked (default: 160): ") or 160)
        bonuses = float(input("Enter bonuses (default: 0): ") or 0)
        deductions = float(input("Enter deductions (default: 0): ") or 0)
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return None
    return name, employee_id, hourly_wage, hours_worked, bonuses, deductions


def add_employee():
    print("1. Add Manager\n2. Add Developer\n3. Add Employee")
    choice = int(input("Choose the type of employee to add: "))

    name, employee_id, hourly_wage, hours_worked, bonuses, deductions = get_employee_input()

    if name is None:
        print("Error: Invalid input. Please try again.")
        return

    if choice == 1:
        team_size = int(input("Enter team size: "))
        manager = Manager(name, employee_id, hourly_wage, hours_worked, team_size, bonuses, deductions)
        manager.save_to_db(cursor, conn)  # Pass both cursor and conn
        print(manager.generate_payslip())
    elif choice == 2:
        programming_language = input("Enter primary programming language: ")
        developer = Developer(name, employee_id, hourly_wage, hours_worked, programming_language, bonuses, deductions)
        developer.save_to_db(cursor, conn)  # Pass both cursor and conn
        print(developer.generate_payslip())
    else:
        employee = Employee(name, employee_id, hourly_wage, hours_worked, bonuses, deductions)
        employee.save_to_db(cursor, conn)  # Pass both cursor and conn
        print(employee.generate_payslip())


def main():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_employee()
        elif choice == 2:
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
