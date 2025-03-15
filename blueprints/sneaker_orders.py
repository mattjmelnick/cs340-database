from flask import Blueprint, render_template, request, redirect, url_for, g
import database.db_connector as db

sneaker_orders_bp = Blueprint('sneaker_orders', __name__)

@sneaker_orders_bp.route('/sneaker_orders', methods=["GET", "POST"])
def sneaker_orders():
    db_connection = g.db_connection
    if request.method == "POST":
        # get the input data from the add sneaker_order form
        order_id = request.form.get("soOrderID")
        sneaker_id = request.form.get("soSneakerID")
        quantity = request.form.get("soQuantity")
        # check for NULL value
        if sneaker_id == '0':
            query = f"INSERT INTO SneakerOrders (order_id, sneaker_id, quantity) VALUES ({order_id}, NULL, {quantity})"
        else:
            query = f"INSERT INTO SneakerOrders (order_id, sneaker_id, quantity) VALUES ({order_id}, {sneaker_id}, {quantity})"
        db.execute_query(db_connection=db_connection, query=query)
        
        # return to sneaker orders page
        return redirect(url_for('sneaker_orders.sneaker_orders'))

    if request.method == "GET":
        # display the data from the database in the table
        query = """SELECT *, brand, model_name, name FROM SneakerOrders
                   INNER JOIN Sneakers
                   ON SneakerOrders.sneaker_id = Sneakers.sneaker_id
                   INNER JOIN Orders
                   ON SneakerOrders.order_id = Orders.order_id
                   INNER JOIN Customers
                   ON Orders.customer_id = Customers.customer_id"""
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()

        # get sneaker_ids from the Sneakers table
        sneaker_query = "SELECT sneaker_id, brand, model_name FROM Sneakers"
        sneaker_cursor = db.execute_query(db_connection=db_connection, query=sneaker_query)
        sneaker_results = list(sneaker_cursor.fetchall())

        # get order_ids from the Orders table
        order_query = """SELECT order_id, name FROM Orders
                         INNER JOIN Customers
                         ON Orders.customer_id = Customers.customer_id"""
        order_cursor = db.execute_query(db_connection=db_connection, query=order_query)
        order_results = list(order_cursor.fetchall())

        return render_template("sneaker_orders.j2", sneaker_orders=results,
                                sneakers=sneaker_results, orders=order_results)

@sneaker_orders_bp.route('/edit_sneaker_order/<int:sneaker_order_id>', methods=["POST"])
def edit_sneaker_order(sneaker_order_id):
    db_connection = g.db_connection
    # get the input data from the update sneaker order form
    order_id = request.form.get("soOrderIDUpdate")
    sneaker_id = request.form.get("soSneakerIDUpdate")
    quantity = request.form.get("soQuantityUpdate")
    # check for selected null value
    if sneaker_id == '0':
        query = f"UPDATE SneakerOrders SET order_id = {order_id}, sneaker_id = NULL, quantity = {quantity}\
            WHERE sneaker_order_id = {sneaker_order_id}"
    else:
        query = f"UPDATE SneakerOrders SET order_id = {order_id}, sneaker_id = {sneaker_id}, quantity = {quantity}\
            WHERE sneaker_order_id = {sneaker_order_id}"
    db.execute_query(db_connection=db_connection, query=query)

    # return to sneaker orders page
    return redirect(url_for('sneaker_orders.sneaker_orders'))

@sneaker_orders_bp.route('/delete_sneaker_order/<int:sneaker_order_id>', methods=["POST"])
def delete_sneaker_order(sneaker_order_id):
    db_connection = g.db_connection
    # delete the selected sneaker order from the database
    query = f"DELETE FROM SneakerOrders WHERE sneaker_order_id = {sneaker_order_id}"
    db.execute_query(db_connection=db_connection, query=query)

    # return to sneaker orders page
    return redirect(url_for('sneaker_orders.sneaker_orders'))
