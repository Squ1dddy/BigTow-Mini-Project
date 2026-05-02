import datetime
import random
import json

# Generate random ID
def generate_ID():
    order_id = random.randint(0,999999)
    return order_id

def space():
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")

# Fundemental Formula Calculation
def calculate_cost(length):
    wheels = 0
    if length < 3:
        wheel_set = 1
    else: 
        wheel_set = 2
    
    area = length * 2.5
    cost_per_day = (area * 125) + (100 * wheel_set)
    return cost_per_day, area, wheels

# Print Banner
def print_banner():
    print()
    print("  ██████╗ ██╗ ██████╗     ████████╗ ██████╗ ██╗    ██╗")
    print("  ██╔══██╗██║██╔════╝        ██╔══╝██╔═══██╗██║    ██║")
    print("  ██████╔╝██║██║  ███╗       ██║   ██║   ██║██║ █╗ ██║")
    print("  ██╔══██╗██║██║   ██║       ██║   ██║   ██║██║███╗██║")
    print("  ██████╔╝██║╚██████╔╝       ██║   ╚██████╔╝╚███╔███╔╝")
    print("  ╚═════╝ ╚═╝ ╚═════╝        ╚═╝    ╚═════╝  ╚══╝╚══╝ ")
    print("  Trailer Hire System")
    print()


def order_process():
    #Gather Truck Size
    while True:
        date_time = datetime.datetime.now()
        invalid = True
        while invalid:
            try:
                length = float(input("  Length (1–5 metres): "))
                if length < 1 or length > 5:
                    print("Value must be between 1 and 5")
                else:
                    invalid = False
            except ValueError:
                print("Please enter a numeric value")
        
        cost_per_day, area, wheels = calculate_cost(length)
        # Present Truck Size
        print()
        print("  TRAILER SPECIFICATIONS")
        print("  " + "─" * 34)
        print(f"  Length       {length}m           ${area * 125:.2f}")
        print(f"  Wheels       {wheels} sets         ${wheels * 100:.2f}")
        print("  " + "─" * 34)
        print(f"  Cost Per Day              ${cost_per_day:.2f}")
        print()

        # Calculate Hire Days
        invalid = True
        while invalid:
            confirm = input("  Continue? (y/n): ")
            if confirm == 'n':
                break
            if confirm == 'y':
                invalid = True
                while invalid:
                    try:
                        hire_days = int(input("  Number of hire days: "))
                        invalid = False  
                    except ValueError:
                        print("  ! Please enter a numeric value")
            
            customer_id = generate_ID()
            invoice_id = generate_ID()
            order_id = generate_ID()

            total_cost = hire_days * cost_per_day

            #Print Order Suammary
            print()
            print("  ORDER SUMMARY")
            print("  " + "─" * 34)
            print(f"  Order ID       {order_id}")
            print(f"  Hire Period    {hire_days} days")
            print("  " + "─" * 34)
            print(f"  Balance Owing             ${total_cost:.2f}")
            print()

            # Save order
            invalid = False
            save_order(order_id, customer_id, invoice_id, date_time, length, area, wheels, cost_per_day, hire_days, total_cost)
            return customer_id
        break

def customer_detail_collection(customer_id):
    print()
    print("  CUSTOMER DETAILS") # Gather Customer Details
    print("  " + "─" * 34)
    license = int(input("  Drivers Licence    : "))
    first_name = input("  First Name         : ")
    surname = input("  Surname            : ")
    street_name = input("  Street             : ")
    suburb = input("  Suburb             : ")
    post_code = input("  Post Code          : ")
    phone = input("  Phone              : ")
    email = input("  Email              : ")
    print()
    
    # Save Details
    save_customer(customer_id, license, first_name, surname, street_name, suburb, post_code, phone, email)
    print("  ✓ Customer record saved.")
    space()

def save_customer(customer_id, license, first_name, surname, street_name, suburb, post_code, phone, email):
    new_customer = {
        "customer_id" : customer_id,
        "license" : license,
        "first_name": first_name,
        "surname": surname,
        "street_name": street_name,
        "suburb": suburb,
        "post_code": post_code,
        "phone": phone,
        "email": email
    }

    try:
        with open("customers.json", "r") as f:
            customers = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        customers = []

    customers.append(new_customer)
    with open("customers.json", "w") as f:
        json.dump(customers, f, indent=4)

def save_order(order_id, customer_id, invoice_id, date_time, length, area, wheels, cost_per_day, hire_days, total_cost):
    new_order = {
        "order_id": order_id,
        "customer_id": customer_id,
        "invoice_id": invoice_id,
        "date_time": str(date_time),
        "trailer": {
            "length": length,
            "width": 2.5,
            "area": area,
            "wheels": wheels
        },
        "cost_per_day": cost_per_day,
        "hire_days": hire_days,
        "balance_owing": total_cost
    }

    try:
        with open("orders.json", "r") as f:
            orders = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        orders = []

    orders.append(new_order)
    with open("orders.json", "w") as f:
        json.dump(orders, f, indent=4)

def customer_lookup():
    # Grab surname
    search_name = input("Enter Surname: ")
    
    # Open Json
    try:
        with open('customers.json', 'r') as f:
            all_customers = json.load(f) # Load the list
    except (FileNotFoundError, json.JSONDecodeError):
        print("No records found.")
        return

    #Create a flag
    Found = False
    # 2. Iterate through the LIST
    for customer in all_customers:
        if customer['surname'].lower() == search_name.lower():
            print(f"Match Found: {customer['first_name']} {customer['surname']}")
            print(f"Drivers License: {customer['license']}")
            Found = True


    # If not found make new ID and run onboarding process
    if not Found:
        print("Not Found")
        customer_id = generate_ID()
        customer_detail_collection(customer_id)
        
        


def main():
    invalid = True
    while invalid:
        space()
        print_banner()
        print("  1.  Place New Order")
        print("  2.  Customer Lookup")
        print()
        choice = input("  Select an option: ")
        if choice == '1':
            space()
            order_process()
            customer_detail_collection(generate_ID())
        elif choice == '2':
            space()
            customer_lookup()
        else:
            print()
            print("  ! Invalid selection.")


if __name__ == '__main__':
    main()