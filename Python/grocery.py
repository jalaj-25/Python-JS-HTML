class Store:
    def __init__(self):
        self.stock = {}

    def add_product(self, product_name, quantity):
        if product_name in self.stock:
            self.stock[product_name] += quantity
        else:
            self.stock[product_name] = quantity

    def purchase_product(self, product_name, quantity):
        if product_name in self.stock:
            if self.stock[product_name] >= quantity:
                self.stock[product_name] -= quantity
                print(f"{quantity} {product_name}(s) purchased successfully.")
            else:
                print("Insufficient stock.")
        else:
            print("Product not found.")

    def display_stock(self):
        print("Current Stock:")
        for product, quantity in self.stock.items():
            print(f"{product}: {quantity}")


def main():
    store = Store()

    while True:
        print("\n1. Add Product to Stock")
        print("2. Purchase Product")
        print("3. Display Current Stock")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            store.add_product(product_name, quantity)
        elif choice == '2':
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity to purchase: "))
            store.purchase_product(product_name, quantity)
        elif choice == '3':
            store.display_stock()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
