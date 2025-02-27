from flask import Blueprint, render_template, request, redirect, url_for
import database.db_connector as db

customers_bp = Blueprint('customers', __name__)

@customers_bp.route('/customers', methods=["GET", "POST"])
def customers():
    db_connection = db.connect_to_database()
    if request.method == "POST":
        # get the input data from the add customer form
        name = request.form.get("customerName")
        email = request.form.get("customerEmail")
        phone = request.form.get("customerPhone")
        # add the new customer to the database
        query = f"INSERT INTO Customers (name, email, phone_number) VALUES ('{name}', '{email}', '{phone}')"
        db.execute_query(db_connection=db_connection, query=query)

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
    db_connection = db.connect_to_database()
    # get the input data from the update customer form
    name = request.form.get("customerNameUpdate")
    email = request.form.get("customerEmailUpdate")
    phone = request.form.get("customerPhoneUpdate")
    # update the customer in the database using the input data
    query = f"UPDATE Customers SET name = '{name}', email = '{email}',\
        phone_number = '{phone}' WHERE customer_id = {customer_id}"
    db.execute_query(db_connection=db_connection, query=query)

	# return to customers page
    return redirect(url_for('customers.customers'))

@customers_bp.route('/delete_customer/<int:customer_id>', methods=["POST"])
def delete_customer(customer_id):
    db_connection = db.connect_to_database()
    # delete the selected customer from the database
    query = f"DELETE FROM Customers WHERE customer_id = {customer_id}"
    db.execute_query(db_connection=db_connection, query=query)

	# return to customers page
    return redirect(url_for('customers.customers'))
