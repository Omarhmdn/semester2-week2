import sqlite3

# ==================================================
# Section 1 – Summaries
# ==================================================

def total_customers(conn):
    query = '''
            SELECT COUNT(customers.customer_id) AS Total_Customers FROM customers
            '''
    cursor = conn.execute(query)
    Total_Customers = cursor.fetchone()
    print(f"\nTotal Number of Customers: {Total_Customers[0]}")

def customer_signup_range(conn):

    query = '''
            SELECT customers.customer_name, DATE(customers.signup_date) AS Signup_Date FROM customers GROUP BY Signup_Date
            '''
    cursor = conn.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x[0], x[1])


def order_summary_stats(conn):
    query = '''
            SELECT COUNT(orders.order_id) AS Total_Orders, AVG(orders.order_total) AS Average_Order_Value, MAX(orders.order_total) AS Max_Order_Value, MIN(orders.order_total) AS Min_Order_Value
            FROM orders;
            '''
    cursor = conn.execute(query)
    result = cursor.fetchone()
    print(f"Total Orders: {result[0]} , Average Order Value: {result[1]}, Maximum Order Value: {result[2]}, Minimum Order Value: {result[3]}")


def driver_summary(conn):
    query = '''
            SELECT drivers.driver_id, drivers.hire_date 
            FROM drivers GROUP BY drivers.driver_id;
            '''
    cursor = conn.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(f"Driver ID: {x[0]}, Driver Hire Date: {x[1]}")
    print(f"Total Number of drivers: {len(result)}")


# ==================================================
# Section 2 – Key Statistics
# ==================================================

def orders_per_customer(conn):
    pass


def driver_workload(conn):
    pass


def delivery_lookup_by_id(conn, order_id):
    pass


# ==================================================
# Section 3 – Time-based Summaries
# ==================================================

def orders_per_date(conn):
    pass


def deliveries_per_date(conn):
    pass


def customer_signups_per_month(conn):
    pass


# ==================================================
# Section 4 – Performance and Rankings
# ==================================================

def top_customers_by_spend(conn, limit=5):
    pass


def rank_drivers_by_deliveries(conn):
    pass


def high_value_orders(conn, threshold):
    pass


# ==================================================
# Menus - You should not need to change any code below this point until the stretch tasks.
# ==================================================

def section_1_menu(conn):
    while True:
        print("\nSection 1 – Summaries")
        print("1. Total number of customers")
        print("2. Customer signup date range")
        print("3. Order summary statistics")
        print("4. Driver summary")
        print("0. Back to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            total_customers(conn)
        elif choice == "2":
            customer_signup_range(conn)
        elif choice == "3":
            order_summary_stats(conn)
        elif choice == "4":
            driver_summary(conn)
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")


def section_2_menu(conn):
    while True:
        print("\nSection 2 – Key Statistics")
        print("1. Orders per customer")
        print("2. Driver workload")
        print("3. Order delivery overview")
        print("0. Back to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            orders_per_customer(conn)
        elif choice == "2":
            driver_workload(conn)
        elif choice == "3":
            order_id = input("Enter order ID: ").strip()
            if not order_id.isdigit():
                print("Please enter a valid integer order ID.")
                continue
            delivery_lookup_by_id(conn, int(order_id))
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")


def section_3_menu(conn):
    while True:
        print("\nSection 3 – Time-based Summaries")
        print("1. Orders per date")
        print("2. Deliveries per date")
        print("3. Customer signups per month")
        print("0. Back to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            orders_per_date(conn)
        elif choice == "2":
            deliveries_per_date(conn)
        elif choice == "3":
            customer_signups_per_month(conn)
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")


def section_4_menu(conn):
    while True:
        print("\nSection 4 – Performance and Rankings")
        print("1. Top 5 customers by total spend")
        print("2. Rank drivers by deliveries completed")
        print("3. High-value orders")
        print("0. Back to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            top_customers_by_spend(conn)
        elif choice == "2":
            rank_drivers_by_deliveries(conn)
        elif choice == "3":
            try:
                threshold = float(input("Enter order value threshold (£): "))
                high_value_orders(conn, threshold)
            except:
                print("Please enter a valid numerical value.")
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")


def main_menu(conn):
    while True:
        print("\n=== Delivery Service Management Dashboard ===")
        print("1. Section 1 – Summaries")
        print("2. Section 2 – Key Statistics")
        print("3. Section 3 – Time-based Summaries")
        print("4. Section 4 – Performance and Rankings")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            section_1_menu(conn)
        elif choice == "2":
            section_2_menu(conn)
        elif choice == "3":
            section_3_menu(conn)
        elif choice == "4":
            section_4_menu(conn)
        elif choice == "0":
            print("Exiting dashboard.")
            break
        else:
            print("Invalid option. Please try again.")

def get_connection(db_path="food_delivery.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

if __name__ == "__main__":
    conn = get_connection()
    main_menu(conn)
    conn.close()