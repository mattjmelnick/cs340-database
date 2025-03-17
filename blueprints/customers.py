from flask import Blueprint, render_template, request, redirect, url_for, g
import database.db_connector as db

"""
Citation for this file:
Date: 2/26/25 
All blueprint pages are modified from:
https://github.com/osu-cs340-ecampus/flask-starter-app/blob/master/bsg_people_app/app.py

Additional resource used:
https://realpython.com/flask-blueprint/
"""


customers_bp = Blueprint('customers', __name__)

@customers_bp.route('/customers', methods=["GET", "POST"])
def customers():
    db_connection = g.db_connection
    if request.method == "POST":
        # get the input data from the add customer form
        name = request.form.get("customerName")
        email = request.form.get("customerEmail")
        phone = request.form.get("customerPhone")
        # add the new customer to the database
        query = "INSERT INTO Customers (name, email, phone_number) VALUES (%s, %s, %s)"
        db.execute_query(db_connection=db_connection, query=query, query_params=(name, email, phone))

        # return to customers page
        return redirect(url_for('customers.customers'))

    if request.method == "GET":
        # display the data from the database in the table
        query = "SELECT * FROM Customers"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()

        return render_template("customers.j2", customers=results)

@customers_bp.route('/edit_customer/<int:customer_id>', methods=["POST"])
def edit_customer(customer_id):
    db_connection = g.db_connection
    # get the input data from the update customer form
    name = request.form.get("customerNameUpdate")
    email = request.form.get("customerEmailUpdate")
    phone = request.form.get("customerPhoneUpdate")
    # update the customer in the database using the input data
    query = """UPDATE Customers SET name = %s, email = %s,
        phone_number = %s WHERE customer_id = %s"""
    db.execute_query(db_connection=db_connection, query=query, query_params=(name, email, phone, customer_id))

    # return to customers page
    return redirect(url_for('customers.customers'))

@customers_bp.route('/delete_customer/<int:customer_id>', methods=["POST"])
def delete_customer(customer_id):
    db_connection = g.db_connection
    # delete the selected customer from the database
    query = f"DELETE FROM Customers WHERE customer_id = {customer_id}"
    db.execute_query(db_connection=db_connection, query=query)

    # return to customers page
    return redirect(url_for('customers.customers'))
