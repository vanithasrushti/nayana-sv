class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.transactions = []
        self.lifespan_years = 1  # default lifespan

    def add_transaction(self, amount):
        self.transactions.append(amount)

    def set_lifespan(self, years):
        self.lifespan_years = years

    def average_order_value(self):
        if not self.transactions:
            return 0
        return sum(self.transactions) / len(self.transactions)

    def purchase_frequency(self):
        if self.lifespan_years == 0:
            return 0
        return len(self.transactions) / self.lifespan_years

    def clv(self):
        return self.average_order_value() * self.purchase_frequency() * self.lifespan_years

    def __str__(self):
        return (f"{self.customer_id}. {self.name} | Orders: {len(self.transactions)} | "
                f"CLV: ₹{self.clv():.2f}")


class CLVSystem:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer_id, name):
        if customer_id in self.customers:
            print("❌ Customer ID already exists.")
            return
        self.customers[customer_id] = Customer(customer_id, name)
        print(f"✅ Customer '{name}' added.")

    def add_transaction(self, customer_id, amount):
        customer = self.customers.get(customer_id)
        if not customer:
            print("❌ Customer not found.")
            return
        customer.add_transaction(amount)
        print(f"✅ ₹{amount} transaction added for {customer.name}.")

    def set_lifespan(self, customer_id, years):
        customer = self.customers.get(customer_id)
        if not customer:
            print("❌ Customer not found.")
            return
        customer.set_lifespan(years)
        print(f"✅ Lifespan set to {years} year(s) for {customer.name}.")

    def show_customers(self):
        print("\n📋 Customer List:")
        if not self.customers:
            print("No customers found.")
            return
        for customer in self.customers.values():
            print(customer)


# ---------------- APP SIMULATION ----------------

system = CLVSystem()

while True:
    print("\n====== CUSTOMER LIFETIME VALUE PROGRAM ======")
    print("1. Add Customer")
    print("2. Add Transaction")
    print("3. Set Customer Lifespan")
    print("4. Show All Customers and CLV")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        try:
            cid = input("Enter Customer ID: ")
            name = input("Enter Customer Name: ")
            system.add_customer(cid, name)
        except:
            print("❌ Error adding customer.")

    elif choice == '2':
        try:
            cid = input("Enter Customer ID: ")
            amount = float(input("Enter Transaction Amount (₹): "))
            system.add_transaction(cid, amount)
        except ValueError:
            print("❌ Invalid amount.")

    elif choice == '3':
        try:
            cid = input("Enter Customer ID: ")
            years = float(input("Enter Customer Lifespan in Years: "))
            system.set_lifespan(cid, years)
        except ValueError:
            print("❌ Invalid lifespan.")

    elif choice == '4':
        system.show_customers()

    elif choice == '5':
        print("👋 Exiting program. Thank you!")
        break

    else:
        print("❌ Invalid choice. Please enter 1-5.")
