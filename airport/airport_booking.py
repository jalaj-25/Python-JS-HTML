class Passenger:
    def __init__(self, name, age, gender, destination, cost):
        self.name = name
        self.age = age
        self.gender = gender
        self.destination = destination
        self.cost = cost 

def get_passenger_details(num):
    passengers = []
    for i in range(num):
        name = input(f"Enter the name of Passenger {i + 1}: ")
        age = int(input("Enter age: "))
        gender = input("Enter gender: ")
        destination = choose_destination()
        cost = calculate_cost(destination)
        passengers.append(Passenger(name, age, gender, destination, cost))
    return passengers

def choose_destination():
    choice = int(input("\nChoose your destination:\n1. DEHRADUN\n2. JAIPUR\n3. BANGALORE\n4. HYDERABAD\nEnter choice: "))
    return choice

def calculate_cost(destination):
    prices = {1: 7200, 2: 8200, 3: 92000, 4: 10000}
    print(f"Price: {prices[destination]}/-")
    return prices[destination]

def display_bookings(passengers):
    for i, p in enumerate(passengers):
        print(f"\nPassenger {i + 1}:")
        print(f"Name: {p.name}")
        print(f"Age: {p.age}")
        print(f"Gender: {p.gender}")
        print(f"Destination: {['Dehradun', 'Jaipur', 'Bangalore', 'Hyderabad'][p.destination - 1]}")
        print(f"Cost: {p.cost}/-")

def process_payment(total_cost):
    while True:
        amount = int(input(f"Total cost is {total_cost}/-. Enter payment amount: "))
        if amount < total_cost:
            print("Insufficient payment. Please pay the full amount.")
        else:
            print("Payment successful!")
            break
