# Employee Salary Calculation and Management

A Python-based employee management system that calculates monthly salaries, processes bonuses and deductions, and generates payslips for different employee roles like Managers and Developers. The project is designed with modular components, optimized for maintainability and efficiency, and uses SQLite for database storage.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Modules](#modules)
- [Database Setup](#database-setup)
- [Future Improvements](#future-improvements)
- [License](#license)

## Project Overview
This project manages employee data for salary calculations, including:
- Employee roles and unique identifiers
- Hourly wages, total hours worked, bonuses, and deductions
- Overtime pay handling for hours exceeding 160 per month
- Custom reports for managers to view and calculate the total salaries of team members

The application follows an object-oriented approach with separate classes for employees, managers, and developers, utilizing inheritance to avoid redundancy.

## Features
- **Employee Classes**: Supports different employee roles (Managers and Developers).
- **Salary Calculations**: Calculates monthly salaries with overtime, bonuses, and deductions.
- **Payslip Generation**: Produces detailed payslips for each employee.
- **Database Integration**: Stores employee information in an SQLite database.
- **Error Handling and Logging**: Ensures stability and ease of debugging.

## Installation

### Prerequisites
- Python 3.7 or higher
- SQLite (comes pre-installed with Python's `sqlite3` library)

### Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/employee-management-system.git
   cd employee-management-system
2. **Install required packages (if any additional packages are needed in future updates)**:
   pip install -r requirements.txt
3. **Initialize the Database: Run the database setup script to create necessary tables**:
   python setup_database.py
## Usage
1. **Run the Application**:
python main.py

3. **Menu Options**:

Add Employee: Add new employees, specifying their role as Manager, Developer, or generic Employee.
Calculate Salary: Input hours worked, bonuses, and deductions to calculate the monthly salary.
Generate Payslip: Generate a detailed payslip with a breakdown of salary components.
View Team Salary: For managers, view the total salary expense of team members.
3. Input Examples: When adding an employee, the system will prompt for:

Name, Employee ID, Role (Manager/Developer), Hourly Wage, Hours Worked, Bonuses, and Deductions.

### Example Payslip Output:
After inputting employee details, the payslip may look like this:

Payslip for Employee ID: E001
Name: John Doe
Role: Developer
Hourly Wage: $30.00
Total Hours Worked: 170
Overtime Pay: $150.00
Bonuses: $100.00
Deductions: $20.00
Total Monthly Salary: $5300.00

### Project Structure
The project is organized into several components:

employee-management-system/
│
├── main.py                 # Main application runner
├── setup_database.py       # Script to initialize the database
├── employee.py             # Defines the Employee base class
├── manager.py              # Defines the Manager class (inherits Employee)
├── developer.py            # Defines the Developer class (inherits Employee)
├── database_utils.py       # Database operations and utility functions
├── utils.py                # Helper functions for input validation, logging, etc.
└── README.md               # Project documentation

## Modules

- **`employee.py`**: Contains the `Employee` class with attributes for name, ID, hourly wage, bonuses, and methods for salary calculation, adding bonuses, and deductions.
- **`manager.py`**: Extends `Employee` for managers, adding team size functionality and team salary calculations.
- **`developer.py`**: Extends `Employee` for developers, adding a primary programming language attribute.
- **`database_utils.py`**: Includes functions for database connectivity, saving, retrieving, and updating employee data.
- **`utils.py`**: General helper functions for error handling, logging, and input validation.

## Database Setup

The SQLite database stores employee data in the `employees` table:

### Table Schema:
- `employee_id` (TEXT, Primary Key)
- `name` (TEXT)
- `role` (TEXT)
- `hourly_wage` (REAL)
- `hours_worked` (REAL)
- `bonuses` (REAL)
- `deductions` (REAL)
- `extra_info` (TEXT)

Run `setup_database.py` to initialize the database and create necessary indexes for efficient querying.

## Future Improvements
- **Role-based Access Control**: Add permissions for managers and other roles.
- **Enhanced Reporting**: Add more reporting options, including yearly summaries.
- **GUI Integration**: Implement a graphical interface for better user experience.
- **Email Payslip**: Enable payslip generation and emailing directly from the application.






