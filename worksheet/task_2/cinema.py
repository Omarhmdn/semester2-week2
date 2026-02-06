"""
This is where you should write your code and this is what you need to upload to Gradescope for autograding.

You must NOT change the function definitions (names, arguments).

You can run the functions you define in this file by using test.py (python test.py)
Please do not add any additional code underneath these functions.
"""

import sqlite3


def customer_tickets(conn, customer_id):
    """
    Return a list of tuples:
    (film_title, screen, price)

    Include only tickets purchased by the given customer_id.
    Order results by film title alphabetically.

    """
    query = '''
    SELECT films.title AS film_title, screenings.screen AS screen, tickets.price AS price
    FROM customers JOIN tickets ON customers.customer_id=tickets.customer_id JOIN screenings ON tickets.screening_id=screenings.screening_id JOIN films ON screenings.film_id=films.film_id 
    WHERE customers.customer_id = ?
    GROUP BY film_title;
    '''

    customer_tickets = []
    cursor = conn.execute(query, (customer_id,))
    result = cursor.fetchall()
    for x in result:
        grouped_data = x[0], x[1], x[2]
        customer_tickets.append(grouped_data)
    return customer_tickets
    

def screening_sales(conn):
    """
    Return a list of tuples:
    (screening_id, film_title, tickets_sold)

    Include all screenings, even if tickets_sold is 0.
    Order results by tickets_sold descending.
    """
    query = '''
    SELECT screenings.screening_id AS screening_id, films.title AS film_title, COUNT(tickets.ticket_id) AS tickets_sold
    FROM films LEFT JOIN screenings ON films.film_id=screenings.film_id LEFT JOIN tickets ON screenings.screening_id=tickets.screening_id
    GROUP BY screenings.screening_id
    ORDER BY tickets_sold DESC;
    '''

    screening_sales = []
    cursor = conn.execute(query)
    result = cursor.fetchall()
    for x in result:
        grouped_data = x[0], x[1], x[2]
        screening_sales.append(grouped_data)
    return screening_sales


def top_customers_by_spend(conn, limit):
    """
    Return a list of tuples:
    (customer_name, total_spent)

    total_spent is the sum of ticket prices per customer.
    Only include customers who have bought at least one ticket.
    Order by total_spent descending.
    Limit the number of rows returned to `limit`.
    """
    query = f'''
    SELECT customers.customer_name AS customer_name, SUM(tickets.price) AS total_spent
    FROM customers JOIN tickets ON customers.customer_id=tickets.customer_id
    GROUP BY customers.customer_name
    ORDER BY total_spent DESC
    LIMIT {limit};
    '''

    top_customers_by_spend = []
    cursor = conn.execute(query)
    result = cursor.fetchall()
    for x in result:
        grouped_data = x[0], x[1]
        top_customers_by_spend.append(grouped_data)
    return top_customers_by_spend