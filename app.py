from flask import Flask, render_template, request, redirect, url_for, json
import database.db_connector as db
import MySQLdb
import os

# Configuration
app = Flask(__name__)
db_connection = db.connect_to_database()

# Routes 
@app.route('/')
def root():
    return render_template("index.j2")

@app.route('/customers', methods=["GET", "POST"])
def customers():
    if request.method == "POST":
        name = request.form.get("customerName")
        email = request.form.get("customerEmail")
        phone = request.form.get("customerPhone")
        query = f"INSERT INTO Customers (name, email, phone_number) VALUES ('{name}', '{email}', '{phone}')"
        db.execute_query(db_connection=db_connection, query=query)

        return redirect(url_for('customers'))

    if request.method == "GET":
        query = "SELECT * FROM Customers"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = json.dumps(cursor.fetchall())
        results = json.loads(results)

        return render_template("customers.j2", customers=results)

@app.route('/edit_customer/<int:customer_id>', methods=["POST"])
def edit_customer(customer_id):
    name = request.form.get("customerNameUpdate")
    email = request.form.get("customerEmailUpdate")
    phone = request.form.get("customerPhoneUpdate")
    query = f"UPDATE Customers SET name = '{name}', email = '{email}',\
        phone_number = '{phone}' WHERE customer_id = {customer_id}"
    db.execute_query(db_connection=db_connection, query=query)

    return redirect(url_for('customers'))

@app.route('/delete_customer/<int:customer_id>', methods=["POST"])
def delete_customer(customer_id):
    query = f"DELETE FROM Customers WHERE customer_id = {customer_id}"
    db.execute_query(db_connection=db_connection, query=query)

    return redirect(url_for('customers'))

@app.route('/sneakers')
def sneakers():
    return render_template("sneakers.j2")

@app.route('/orders')
def orders():
    return render_template("orders.j2")

@app.route('/raffles')
def raffles():
    return render_template("raffles.j2")

@app.route('/drawings')
def drawings():
    return render_template("drawings.j2")

@app.route('/sneaker_orders')
def sneaker_orders():
    return render_template("sneaker_orders.j2")

@app.route('/raffle_orders', methods=["GET", "POST"])
def raffle_orders():
    if request.method == "POST":
        cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)
        order_id = request.form.get("roOrderID")
        raffle_id = request.form.get("roRaffleID")
        if raffle_id == '0':
            query = f"INSERT INTO RaffleOrders (order_id, raffle_id) VALUES ({order_id}, NULL)"
        else:
            query = f"INSERT INTO RaffleOrders (order_id, raffle_id) VALUES ({order_id}, {raffle_id})"
        db.execute_query(db_connection=db_connection, query=query)

        return redirect(url_for('raffle_orders'))

    if request.method == "GET":
        query = "SELECT * FROM RaffleOrders"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = json.dumps(cursor.fetchall())
        raffle_order_data = json.loads(results)

        order_query = "SELECT order_id FROM Orders"
        cursor = db.execute_query(db_connection=db_connection, query=order_query)
        results = json.dumps(cursor.fetchall())
        order_data = json.loads(results)

        raffle_query = "SELECT raffle_id FROM Raffles"
        cursor = db.execute_query(db_connection=db_connection, query=raffle_query)
        results = json.dumps(cursor.fetchall())
        raffle_data = json.loads(results)
        
        return render_template("raffle_orders.j2", raffle_orders=raffle_order_data,
                           order_ids=order_data, raffle_ids=raffle_data)

@app.route('/edit_raffle_order/<int:raffle_order_id>', methods=["POST"])
def edit_raffle_order(raffle_order_id):
    order_id = request.form.get("roOrderIDUpdate")
    raffle_id = request.form.get("roRaffleIDUpdate")
    if raffle_id == "0":
        query = f"UPDATE RaffleOrders SET order_id = '{order_id}', raffle_id = NULL\
            WHERE raffle_order_id = {raffle_order_id}"
    else:
        query = f"UPDATE RaffleOrders SET order_id = '{order_id}', raffle_id = '{raffle_id}'\
            WHERE raffle_order_id = {raffle_order_id}"
    
    db.execute_query(db_connection=db_connection, query=query)
    
    return redirect(url_for('raffle_orders'))

@app.route('/delete_raffle_order/<int:raffle_order_id>', methods=["POST"])
def delete_raffle_order(raffle_order_id):
    query = f"DELETE FROM RaffleOrders WHERE raffle_order_id = {raffle_order_id}"
    db.execute_query(db_connection=db_connection, query=query)

    return redirect(url_for('raffle_orders'))

@app.route('/customer_raffles')
def customer_raffles():
    return render_template("customer_raffles.j2")

# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9008)) 
    app.run(port=port, debug=True) 