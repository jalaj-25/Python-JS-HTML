import airport_booking as ab
import airport_security as asy
import airport_employee as em

def main():
    employees = []
    employee_count = [0]
    passengers = []
    security_password = "password123" 
    while True:
        print("\nMain Menu:")
        print("1. Airport Seat Booking System")
        print("2. Airport Security System")
        print("3. Employee Management System")
        print("4. EXIT")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            num = int(input("Enter the number of passengers: "))
            passengers = ab.get_passenger_details(num)
            ab.display_bookings(passengers)
            total_cost = sum(p.cost for p in passengers)
            ab.process_payment(total_cost)

        elif choice == 2:
            entered_password = input("Enter the security password: ")
            if entered_password == security_password:
                while True:
                    print("\nAirport Security System:")
                    print("1. Add Passenger")
                    print("2. Check Security")
                    print("3. Update Security Clearance")
                    print("4. BACK")
                    sec_choice = int(input("Enter your choice: "))

                    if sec_choice == 1:
                        asy.add_passenger()
                    elif sec_choice == 2:
                        id = int(input("Enter Passenger ID to check: "))
                        asy.check_security(id)
                    elif sec_choice == 3:
                        id = int(input("Enter Passenger ID to update clearance: "))
                        clearance = int(input("Enter clearance (0 for not cleared, 1 for cleared): "))
                        asy.update_security(id, clearance)
                    elif sec_choice == 4:
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Incorrect password. Access denied.")

        elif choice == 3:
            while True:
                print("\nEmployee Management System:")
                print("1. Add Employee")
                print("2. View Employees")
                print("3. BACK")
                emp_choice = int(input("Enter your choice: "))

                if emp_choice == 1:
                    em.add_employee(employees, employee_count)
                elif emp_choice == 2:
                    em.view_employees(employees)
                elif emp_choice == 3:
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == 4:
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
