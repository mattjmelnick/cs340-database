from flask import Flask, render_template, request, redirect, url_for, json
import database.db_connector as db
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
        query = f"INSERT INTO Customers (name, email, phone_number) VALUES ('{name}', '{email}', '{phone}');"
        db.execute_query(db_connection=db_connection, query=query)

        return redirect(url_for('customers'))

    if request.method == "GET":
        query = "SELECT * FROM Customers;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = json.dumps(cursor.fetchall())
        results = json.loads(results)

        return render_template("customers.j2", customers=results)

@app.route('/delete_customer/<int:customer_id>', methods=["POST"])
def delete_customer(customer_id):
    query = f"DELETE FROM Customers WHERE customer_id = {customer_id}"
    db.execute_query(db_connection=db_connection, query=query)

    return redirect(url_for('customers'))

@app.route('/edit_customer/<int:customer_id>', methods=["POST"])
def edit_customer(customer_id):
    name = request.form.get("customerNameUpdate")
    email = request.form.get("customerEmailUpdate")
    phone = request.form.get("customerPhoneUpdate")
    query = f"UPDATE Customers SET Customers.name = '{name}', Customers.email = '{email}',\
        Customers.phone_number = '{phone}' WHERE Customers.customer_id = {customer_id};"
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

@app.route('/raffle_orders')
def raffle_orders():
    return render_template("raffle_orders.j2")

@app.route('/customer_raffles')
def customer_raffles():
    return render_template("customer_raffles.j2")

# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9008)) 
    app.run(port=port, debug=True) 