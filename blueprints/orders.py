from flask import Blueprint, render_template, request, redirect, url_for, g
import database.db_connector as db

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/orders', methods=["GET", "POST"])
def orders():
    db_connection = g.db_connection
    if request.method == "POST":
        # get the input data from the add order form
        customer_id = request.form.get("orderCustomerID")
        purchase_date = request.form.get("orderDate")
        total_price = request.form.get("orderPrice")
        entered_raffle = request.form.get("orderEnteredRaffle")
        # add the new order to the database
        query = "INSERT INTO Orders (customer_id, purchase_date, total_price, entered_raffle) VALUES (%s, %s, %s, %s)"
        db.execute_query(db_connection=db_connection, query=query,
                        query_params=(customer_id, purchase_date, total_price, entered_raffle))

        # return to orders page
        return redirect(url_for('orders.orders'))

    if request.method == "GET":
        # display the data from the database in the table
        query = """SELECT *, name FROM Orders
                   INNER JOIN Customers
                   ON Orders.customer_id = Customers.customer_id""" 
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()

        # get the customer_ids and names from the Customers table
        customer_query = "SELECT customer_id, name FROM Customers" 
        customer_cursor = db.execute_query(db_connection=db_connection, query=customer_query)
        customer_results = customer_cursor.fetchall()

        return render_template("orders.j2", orders=results, customers=customer_results)

@orders_bp.route('/edit_order/<int:order_id>', methods=["POST"])
def edit_order(order_id):
    db_connection = g.db_connection
    # get the input data from the update order form
    customer_id = request.form.get("orderCustomerIDUpdate")
    purchase_date = request.form.get("orderDateUpdate")
    total_price = request.form.get("orderPriceUpdate")
    entered_raffle = request.form.get("orderEnteredRaffleUpdate")
    # update the order in the database using the input data
    query = """UPDATE Orders SET customer_id = %s, purchase_date = %s, total_price = %s,
                entered_raffle = %s WHERE order_id = %s"""
    db.execute_query(db_connection=db_connection, query=query,
                    query_params=(customer_id, purchase_date, total_price, entered_raffle, order_id))

    # return to orders page
    return redirect(url_for('orders.orders'))

@orders_bp.route('/delete_order/<int:order_id>', methods=["POST"])
def delete_order(order_id):
    db_connection = g.db_connection
    query = f"DELETE FROM Orders WHERE order_id = {order_id}"
    db.execute_query(db_connection=db_connection, query=query)

    return redirect(url_for('orders.orders'))
