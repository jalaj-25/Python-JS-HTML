def display_available_cars(cars):
    if not cars:
        print("No cars available.")
    else:
        print("Available Cars:")
        for car in cars:
            print(f"{car['company']} {car['model']} - Price: ${car['price']}")


def main():
    cars = []

    while True:
        print("\nWhat type of car are you looking for?")
        car_type = input("Enter 'luxury sedan' or 'SUV': ").lower()

        price = float(input("Enter maximum price you're willing to pay: $"))

        company = input("Enter preferred car company: ")

        # Search for cars matching the criteria
        available_cars = [car for car in cars if
                          car['type'] == car_type and car['price'] <= price and car['company'] == company]

        display_available_cars(available_cars)

        if input("\nDo you want to continue searching for cars? (yes/no): ").lower() != 'yes':
            break

    print("\nThank you for using the car showroom!")


if __name__ == "__main__":
    # Pre-defined list of cars
    cars = [
        {'type': 'luxury sedan', 'company': 'Mercedes', 'model': 'S-Class', 'price': 80000},
        {'type': 'luxury sedan', 'company': 'BMW', 'model': '7 Series', 'price': 85000},
        {'type': 'SUV', 'company': 'Toyota', 'model': 'RAV4', 'price': 35000},
        {'type': 'SUV', 'company': 'Honda', 'model': 'CR-V', 'price': 32000},
        {'type': 'luxury sedan', 'company': 'Audi', 'model': 'A8', 'price': 90000},
    ]

    main()
