class CarShowroom:
    def __init__(self):
        # Initialize the car showroom with some sample data
        self.cars = {
            'Sedan': [
                {'model': 'Toyota Camry', 'price': 30000, 'company': 'Toyota'},
                {'model': 'Honda Accord', 'price': 32000, 'company': 'Honda'},
            ],
            'SUV': [
                {'model': 'Ford Explorer', 'price': 35000, 'company': 'Ford'},
                {'model': 'Chevrolet Tahoe', 'price': 38000, 'company': 'Chevrolet'},
            ],
            'Sports Car': [
                {'model': 'Porsche 911', 'price': 90000, 'company': 'Porsche'},
                {'model': 'Chevrolet Corvette', 'price': 70000, 'company': 'Chevrolet'},
            ]
        }

    def display_categories(self):
        print("Available Car Categories:")
        for category in self.cars.keys():
            print(f"- {category}")

    def display_cars_in_category(self, category):
        if category in self.cars:
            print(f"\nCars in the {category} category:")
            for car in self.cars[category]:
                print(f"{car['model']} | Price: ${car['price']} | Company: {car['company']}")
        else:
            print(f"No cars found in the {category} category.")

    def filter_cars_by_price(self, category, max_price):
        filtered_cars = [car for car in self.cars[category] if car['price'] <= max_price]
        if filtered_cars:
            print(f"\nCars in the {category} category under ${max_price}:")
            for car in filtered_cars:
                print(f"{car['model']} | Price: ${car['price']} | Company: {car['company']}")
        else:
            print(f"No cars found in the {category} category under ${max_price}.")

    def filter_cars_by_company(self, category, selected_company):
    # Convert category and company names to lowercase for case-insensitive matching
        category_lower = category.lower()
        selected_company_lower = selected_company.lower()

        if category_lower in self.cars:
            filtered_cars = [car for car in self.cars[category_lower] if car['company'].lower() == selected_company_lower]
            if filtered_cars:
                print(f"\nCars in the {category} category from {selected_company}:")
                for car in filtered_cars:
                    print(f"{car['model']} | Price: ${car['price']} | Company: {car['company']}")
            else:
                print(f"No cars found in the {category} category from {selected_company}.")
        else:
            print(f"No cars found in the {category} category.")


    def display_companies_with_prices(self, category):
        if category in self.cars:
            print(f"\nCompanies and Prices in the {category} category:")
            companies_prices = {}
            for car in self.cars[category]:
                company = car['company']
                price = car['price']
                if company in companies_prices:
                    companies_prices[company].append(price)
                else:
                    companies_prices[company] = [price]

            for company, prices in companies_prices.items():
                average_price = sum(prices) / len(prices)
                print(f"{company} | Average Price: ${average_price:.2f}")
        else:
            print(f"No cars found in the {category} category.")


def main():
    showroom = CarShowroom()

    while True:
        print("\nCar Showroom Menu:")
        print("1. Display Car Categories")
        print("2. Choose a Category")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            showroom.display_categories()
        elif choice == '2':
            category = input("Enter the category you want to explore: ")
            showroom.display_cars_in_category(category)

            filter_choice = input("\nDo you want to filter by price, company, or view all companies with prices? (P for Price / C for Company / V for View All Companies / Enter for None): ").lower()

            if filter_choice == 'p':
                max_price = float(input("Enter the maximum price you are willing to pay: "))
                showroom.filter_cars_by_price(category, max_price)
            elif filter_choice == 'c':
                selected_company = input("Enter the company you are interested in: ")
                showroom.filter_cars_by_company(category, selected_company)
            elif filter_choice == 'v':
                showroom.display_companies_with_prices(category)

        elif choice == '3':
            print("Exiting the Car Showroom. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()



"""import tkinter as tk
from tkinter import ttk

class CarShowroomApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Showroom App")

        # Create a Treeview widget to display car information
        self.car_tree = ttk.Treeview(root, columns=('Model', 'Make', 'Year', 'Price'))
        self.car_tree.heading('#0', text='ID')
        self.car_tree.heading('Model', text='Model')
        self.car_tree.heading('Make', text='Make')
        self.car_tree.heading('Year', text='Year')
        self.car_tree.heading('Price', text='Price')
        self.car_tree.pack(pady=10)

        # Sample car data
        car_data = [
            ('1', 'Civic', 'Honda', '2022', '$25,000'),
            ('2', 'Accord', 'Honda', '2022', '$30,000'),
            ('3', 'Camry', 'Toyota', '2022', '$28,000'),
            # Add more cars as needed
        ]

        # Insert sample car data into the Treeview
        for car in car_data:
            self.car_tree.insert('', 'end', values=car)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CarShowroomApp(root)
    app.run()
"""
