from flask import Blueprint, render_template, request, redirect, url_for
import database.db_connector as db

sneaker_orders_bp = Blueprint('sneaker_orders', __name__)

@sneaker_orders_bp.route('/sneaker_orders', methods=["GET", "POST"])
def sneaker_orders():
    db_connection = db.connect_to_database()
    try:
        if request.method == "POST":
            # get the input data from the add sneaker_order form
            order_id = request.form.get("soOrderID")
            sneaker_id = request.form.get("soSneakerID")
            quantity = request.form.get("soQuantity")

            # add the new order to the database
            query = "INSERT INTO SneakerOrders (order_id, sneaker_id, quantity) VALUES (%s, %s, %s)"
            db.execute_query(db_connection=db_connection, query=query, query_params=(order_id, sneaker_id, quantity))

            # return to sneaker orders page
            return redirect(url_for('sneaker_orders.sneaker_orders'))

        if request.method == "GET":
            # display the data from the database in the table
            query = "SELECT * FROM SneakerOrders"
            cursor = db.execute_query(db_connection=db_connection, query=query)
            results = cursor.fetchall()

            sneaker_query = "SELECT * FROM Sneakers"
            sneaker_cursor = db.execute_query(db_connection=db_connection, query=sneaker_query)
            sneaker_results = sneaker_cursor.fetchall()

            order_query = "SELECT * FROM Orders"
            order_cursor = db.execute_query(db_connection=db_connection, query=order_query)
            order_results = order_cursor.fetchall()

            return render_template("sneaker_orders.j2", sneaker_orders=results, sneakers=sneaker_results, orders=order_results)
        
                # return to sneaker orders page
        return redirect(url_for('sneaker_orders.sneaker_orders'))
        
    finally:
        db_connection.close()


@sneaker_orders_bp.route('/edit_sneaker_orders/<int:sneaker_order_id>', methods=["POST"])
def edit_sneaker_order(sneaker_order_id):
    db_connection = db.connect_to_database()
    try:
        # get the input data from the update sneaker order form

        order_id = request.form.get("soOrderIDUpdate")
        sneaker_id = request.form.get("soSneakerIDUpdate")
        quantity = request.form.get("soQuantityUpdate")

        # update the order in the database using the input data
        query = """UPDATE SneakerOrders SET order_id = %s, sneaker_id = %s, quantity = %s
            WHERE sneaker_order_id = %s"""
        db.execute_query(db_connection=db_connection, query=query, query_params=(order_id, sneaker_id, quantity, sneaker_order_id))

        # return to sneaker orders page
        return redirect(url_for('sneaker_orders.sneaker_orders'))
    finally:
        db_connection.close()

@sneaker_orders_bp.route('/delete_sneaker_order/<int:sneaker_order_id>', methods=["POST"])
def delete_sneaker_order(sneaker_order_id):
    db_connection = db.connect_to_database()

    try:
        # delete the selected sneaker order from the database
        query = f"DELETE FROM SneakerOrders WHERE sneaker_order_id = {sneaker_order_id}"
        db.execute_query(db_connection=db_connection, query=query)

        # return to sneaker orders page
        return redirect(url_for('sneaker_orders.sneaker_orders'))
    finally:
        db_connection.close()