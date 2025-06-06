MAX_SEAT = 15
passenger_count = 0
ids = []
security_clearances = []
names = []
passport_numbers = []

def add_passenger():
    global passenger_count
    if passenger_count >= 100:
        print("Cannot add more passengers.")
        return
    name = input("Enter the name of the passenger: ")
    passport_number = input("Enter the passport number: ")
    class_choice = int(input("Choose the class:\n1. Economy\n2. Premium Economy\nEnter choice: "))
    seat_choice = int(input("Enter the seat number: "))
    if seat_choice < 1 or seat_choice > 12:
        print("No vacant seats available.")
        return
    ids.append(passenger_count + 1)
    security_clearances.append(0)
    names.append(name)
    passport_numbers.append(passport_number)
    print(f"Passenger added successfully with ID: {ids[passenger_count]}")
    passenger_count += 1

def check_security(id):
    if id in ids:
        index = ids.index(id)
        if security_clearances[index] == 1:
            print(f"Passenger {names[index]} with ID {id} has cleared security.")
        else:
            print(f"Passenger {names[index]} with ID {id} has not cleared security.")
    else:
        print(f"Passenger with ID {id} not found.")

def update_security(id, clearance):
    if id in ids:
        index = ids.index(id)
        security_clearances[index] = clearance
        print(f"Passenger {names[index]} with ID {id} security clearance updated.")
    else:
        print(f"Passenger with ID {id} not found.")