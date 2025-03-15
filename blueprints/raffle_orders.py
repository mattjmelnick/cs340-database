from flask import Blueprint, render_template, request, redirect, url_for, g
import database.db_connector as db

raffle_orders_bp = Blueprint('raffle_orders', __name__)

@raffle_orders_bp.route('/raffle_orders', methods=["GET", "POST"])
def raffle_orders():
    db_connection = g.db_connection
    if request.method == "POST":
        order_id = request.form.get("roOrderID")
        raffle_id = request.form.get("roRaffleID")
        # check for selected null value
        if raffle_id == '0':
            query = f"INSERT INTO RaffleOrders (order_id, raffle_id) VALUES ({order_id}, NULL)"
        else:
            query = f"INSERT INTO RaffleOrders (order_id, raffle_id) VALUES ({order_id}, {raffle_id})"
        db.execute_query(db_connection=db_connection, query=query)

        # return to raffle orders page
        return redirect(url_for('raffle_orders.raffle_orders'))

    if request.method == "GET":
        query = """SELECT *, name, raffle_description FROM RaffleOrders
                   LEFT JOIN Raffles
                   ON RaffleOrders.raffle_id = Raffles.raffle_id
                   INNER JOIN Orders
                   ON RaffleOrders.order_id = Orders.order_id
                   INNER JOIN Customers
                   ON Orders.customer_id = Customers.customer_id"""
        cursor = db.execute_query(db_connection=db_connection, query=query)
        raffle_order_data = list(cursor.fetchall())

        # get the list of order ids and customer names from the Orders and Customers tables
        order_query = """SELECT order_id, name FROM Orders
                         INNER JOIN Customers
                         ON Orders.customer_id = Customers.customer_id"""
        cursor = db.execute_query(db_connection=db_connection, query=order_query)
        order_data = list(cursor.fetchall())

        # get the list of raffle ids and raffle descriptions from the Raffles table
        raffle_query = "SELECT raffle_id, raffle_description FROM Raffles"
        cursor = db.execute_query(db_connection=db_connection, query=raffle_query)
        raffle_data = list(cursor.fetchall())
        
        return render_template("raffle_orders.j2", raffle_orders=raffle_order_data,
                        orders=order_data, raffles=raffle_data)

@raffle_orders_bp.route('/edit_raffle_order/<int:raffle_order_id>', methods=["POST"])
def edit_raffle_order(raffle_order_id):
    db_connection = g.db_connection
    order_id = request.form.get("roOrderIDUpdate")
    raffle_id = request.form.get("roRaffleIDUpdate")
    # check for selected null value
    if raffle_id == "0":
        query = f"UPDATE RaffleOrders SET order_id = {order_id}, raffle_id = NULL\
            WHERE raffle_order_id = {raffle_order_id}"
    else:
        query = f"UPDATE RaffleOrders SET order_id = {order_id}, raffle_id = {raffle_id}\
            WHERE raffle_order_id = {raffle_order_id}"
    db.execute_query(db_connection=db_connection, query=query)
    
    # return to raffle orders page
    return redirect(url_for('raffle_orders.raffle_orders'))

@raffle_orders_bp.route('/delete_raffle_order/<int:raffle_order_id>', methods=["POST"])
def delete_raffle_order(raffle_order_id):
    db_connection = g.db_connection
    query = f"DELETE FROM RaffleOrders WHERE raffle_order_id = {raffle_order_id}"
    db.execute_query(db_connection=db_connection, query=query)

    # return to raffle orders page
    return redirect(url_for('raffle_orders.raffle_orders'))
