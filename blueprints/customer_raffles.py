from flask import Blueprint, render_template, request, redirect, url_for, g
import database.db_connector as db

customer_raffles_bp = Blueprint('customer_raffles', __name__)

@customer_raffles_bp.route('/customer_raffles', methods=["GET", "POST"])
def customers_raffles():
    db_connection = g.db_connection
    if request.method == "POST":
        # get the input data from the add customer raffle form
        raffle_id = request.form.get("customerRaffleID")
        customer_id = request.form.get("customerCustomerID")
        won_raffle = request.form.get("customerWonRaffle")
        # add the new customer raffle to the database
        query = "INSERT INTO CustomerRaffles (raffle_id, customer_id, won_raffle) VALUES (%s, %s, %s)"
        db.execute_query(db_connection=db_connection, query=query,
                            query_params=(raffle_id, customer_id, won_raffle))

        # return to customer raffles page
        return redirect(url_for('customer_raffles.customers_raffles'))

    if request.method == "GET":
        # display the data from the database in the table
        query = "SELECT * FROM CustomerRaffles"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()

        # get the customer attributes
        customer_query = "SELECT * FROM Customers"
        customer_cursor = db.execute_query(db_connection=db_connection, query=customer_query)
        customer_results = customer_cursor.fetchall()

        # get the raffle attributes
        raffle_query = "SELECT * FROM Raffles"
        raffle_cursor = db.execute_query(db_connection=db_connection, query=raffle_query)
        raffle_results = raffle_cursor.fetchall()

        return render_template("customer_raffles.j2", customers_raffles=results,
                                customers=customer_results, raffles=raffle_results)

@customer_raffles_bp.route('/edit_customer_raffles/<int:customer_raffle_id>', methods=["POST"])
def edit_customer_raffles(customer_raffle_id):
    db_connection = g.db_connection
    # Get the input data from the form
    raffle_id = request.form.get("crRaffleIDUpdate")
    customer_id = request.form.get("crCustomerIDUpdate")
    won_raffle = request.form.get("crWonRaffleUpdate")

    print(f"DEBUG: raffle_id={raffle_id}, customer_id={customer_id}, won_raffle={won_raffle}")

    # Ensure all values are provided
    if not raffle_id or not customer_id or won_raffle is None:
        print("Error: Missing form data.")
        return redirect(url_for("customer_raffles.customers_raffles"))

    # Validate if raffle_id exists
    check_raffle_query = "SELECT raffle_id FROM Raffles WHERE raffle_id = %s"
    existing_raffle = db.execute_query(db_connection, check_raffle_query, (raffle_id,))
    existing_raffle = existing_raffle.fetchall()  # Fetch results

    if not existing_raffle:
        print(f"Error: raffle_id {raffle_id} does not exist.")
        return redirect(url_for("customer_raffles.customers_raffles"))

    # Validate if customer_id exists
    check_customer_query = "SELECT customer_id FROM Customers WHERE customer_id = %s"
    existing_customer = db.execute_query(db_connection, check_customer_query, (customer_id,))
    existing_customer = existing_customer.fetchall()  # Fetch results

    if not existing_customer:
        print(f"Error: customer_id {customer_id} does not exist.")
        return redirect(url_for("customer_raffles.customers_raffles"))

    # Convert won_raffle to integer
    won_raffle = int(won_raffle)

    # Update the customer raffle in the database
    query = """UPDATE CustomerRaffles 
                SET raffle_id = %s, customer_id = %s, won_raffle = %s 
                WHERE customer_raffle_id = %s"""
    db.execute_query(
        db_connection=db_connection, 
        query=query, 
        query_params=(raffle_id, customer_id, won_raffle, customer_raffle_id)
    )
    print("Customer raffle updated successfully.")

    return redirect(url_for("customer_raffles.customers_raffles"))

@customer_raffles_bp.route('/delete_customer_raffles/<int:customer_raffle_id>', methods=["POST"])
def delete_customer(customer_raffle_id):
    db_connection = g.db_connection
    # delete the selected customer raffle from the database
    query = f"DELETE FROM CustomerRaffles WHERE customer_raffle_id = {customer_raffle_id}"
    db.execute_query(db_connection=db_connection, query=query)

    # return to customers page
    return redirect(url_for('customer_raffles.customers_raffles'))
