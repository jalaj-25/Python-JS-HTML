MAX_EMPLOYEES = 100

def add_employee(employees, count):
    num_employees = int(input("Enter the number of employees you want to add: "))
    if count[0] + num_employees > MAX_EMPLOYEES:
        print("Can't add more employees.")
        return
    for _ in range(num_employees):
        name = input("Enter the name of the employee: ").strip()
        employees.append(name)
        count[0] += 1
    print("Employee(s) added successfully.")

def view_employees(employees):
    if len(employees) == 0:
        print("No employees to display.")
    else:
        print("List of Employees:")
        for i, employee in enumerate(employees, 1):
            print(f"{i}. {employee}")