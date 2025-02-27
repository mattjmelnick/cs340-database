from flask import Blueprint, render_template, request, redirect, url_for, json
import database.db_connector as db

customers_bp = Blueprint('customers', __name__)
db_connection = db.connect_to_database()

@customers_bp.route('/customers', methods=["GET", "POST"])
def customers():
    if request.method == "POST":
        name = request.form.get("customerName")
        email = request.form.get("customerEmail")
        phone = request.form.get("customerPhone")
        query = f"INSERT INTO Customers (name, email, phone_number) VALUES ('{name}', '{email}', '{phone}')"
        db.execute_query(db_connection=db_connection, query=query)

        return redirect(url_for('customers.customers'))

    if request.method == "GET":
        query = "SELECT * FROM Customers"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        # results = json.dumps(cursor.fetchall())
        # results = json.loads(results)

        return render_template("customers.j2", customers=results)

@customers_bp.route('/edit_customer/<int:customer_id>', methods=["POST"])
def edit_customer(customer_id):
    name = request.form.get("customerNameUpdate")
    email = request.form.get("customerEmailUpdate")
    phone = request.form.get("customerPhoneUpdate")
    query = f"UPDATE Customers SET name = '{name}', email = '{email}',\
        phone_number = '{phone}' WHERE customer_id = {customer_id}"
    db.execute_query(db_connection=db_connection, query=query)

    return redirect(url_for('customers.customers'))

@customers_bp.route('/delete_customer/<int:customer_id>', methods=["POST"])
def delete_customer(customer_id):
    query = f"DELETE FROM Customers WHERE customer_id = {customer_id}"
    db.execute_query(db_connection=db_connection, query=query)

    return redirect(url_for('customers.customers'))
