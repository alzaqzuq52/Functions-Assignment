# Hassan Alzaqzuq - Week 9 Functions Assignment
# This program collects up to 5 employees' information using functions to reduce repetition

# List to store employee data
employees = []

# Characters to block for input validation
bad_name_chars = '!\"@#$%^&*()_=+<>/?;:[]{}\\'
bad_email_chars = '!\"\'#$%^&*()=+<>/?;:[]{}\\'
bad_address_chars = '!\"\'@$%^&*_=+<>?;:[]{}'

# Function to get a valid employee ID (up to 7 digits)
def get_employee_id():
    while True:
        emp_id = input("Enter Employee ID (up to 7 numbers): ")
        if emp_id.isdigit() and len(emp_id) <= 7:
            return emp_id
        

# Function to get a valid employee name
def get_employee_name():
    while True:
        name = input("Enter Employee Name: ")
        if not any(char in bad_name_chars for char in name) and name.replace(" ", "").isalpha():
            return name
        

# Function to get a valid employee email
def get_employee_email():
    while True:
        email = input("Enter Employee Email: ")
        if ("@" in email and "." in email and
            not any(char in bad_email_chars for char in email)):
            return email
        

# Function to get a valid address (optional)
def get_employee_address():
    while True:
        address = input("Enter Employee Address (optional): ")
        if address == "":
            return ""
        elif not any(char in bad_address_chars for char in address):
            return address
        

# Loop to gather info for up to 5 employees
while len(employees) < 5:
    print(f"\nEntering info for employee #{len(employees) + 1}")
    
    # Use functions to get and validate each field
    employee = {
        'employee_id': get_employee_id(),
        'name': get_employee_name(),
        'email': get_employee_email(),
        'address': get_employee_address()
    }

    employees.append(employee)

    # Ask if the user wants to continue
    add_more = input("Would you like to add another employee? (yes/no): ").lower()
    if add_more != "yes":
        break

# Display final employee list
print("\n✅ Final List of Employees:")
for emp in employees:
    print(emp)
