from flask import Blueprint, flash, render_template, request, redirect, url_for
import database.db_connector as db

orders_bp = Blueprint('orders', __name__)


@orders_bp.route('/orders', methods=["GET", "POST"])
def orders():
    db_connection = db.connect_to_database()
    try:
        if request.method == "POST":
            # get the input data from the add order form
            customer_id = request.form.get("orderCustomerID")
            purchase_date = request.form.get("orderDate")
            total_price = request.form.get("orderPrice")
            entered_raffle = request.form.get("orderEnteredRaffle")
            # add the new order to the database
            query = "INSERT INTO Orders (customer_id, purchase_date, total_price, entered_raffle) VALUES (%s, %s, %s, %s)"
            db.execute_query(db_connection=db_connection, query=query, query_params=(customer_id, purchase_date, total_price, entered_raffle))

            # return to orders page
            return redirect(url_for('orders.orders'))

        if request.method == "GET":
            # display the data from the database in the table
            query = "SELECT * FROM Orders"
            cursor = db.execute_query(db_connection=db_connection, query=query)
            results = cursor.fetchall()

            customer_query = "SELECT * FROM Customers"
            customer_cursor = db.execute_query(db_connection=db_connection, query=customer_query)
            customer_results = customer_cursor.fetchall()
            return render_template("orders.j2", orders=results, customers=customer_results)
    finally:
        db_connection.close()

@orders_bp.route('/edit_order/<int:order_id>', methods=["POST"])
def edit_order(order_id):
    db_connection = db.connect_to_database()
    try:
        # get the input data from the update order form
        customer_id = request.form.get("orderCustomerIDUpdate")
        purchase_date = request.form.get("orderDateUpdate")
        total_price = request.form.get("orderPriceUpdate")
        entered_raffle = request.form.get("orderEnteredRaffleUpdate")
        # update the order in the database using the input data
        query = """UPDATE Orders SET customer_id = %s, purchase_date = %s, total_price = %s,
            entered_raffle = %s WHERE order_id = %s"""
        db.execute_query(db_connection=db_connection, query=query, query_params=(customer_id, purchase_date, total_price, entered_raffle, order_id))

        # return to customers page
        return redirect(url_for('orders.orders'))
    finally:
        db_connection.close()

@orders_bp.route('/delete_order/<int:order_id>', methods=["POST"])
def delete_order(order_id):
    db_connection = db.connect_to_database()
    print(order_id)
    try:
        # Check if the order exists
        order_check = db.execute_query(db_connection, "SELECT * FROM Orders WHERE order_id = %s", (order_id,))
        order_check = order_check.fetchall()

        if not order_check:
            print(f"Error: Order {order_id} does not exist.")
            flash("Error: Order does not exist.")
            return redirect(url_for("orders.orders"))

        # Check if the customer still exists
        customer_check_query = "SELECT customer_id FROM Orders WHERE order_id = %s"
        customer_check = db.execute_query(db_connection, customer_check_query, (order_id,))
        customer_check = customer_check.fetchall()

        if not customer_check:
            print(f"Error: Customer for order {order_id} does not exist.")
            flash("Error: Customer for this order does not exist.")
            return redirect(url_for("orders.orders"))

        # Delete dependent records in SneakerOrders and RaffleOrders first
        db.execute_query(db_connection, "DELETE FROM SneakerOrders WHERE order_id = %s", (order_id,))
        db.execute_query(db_connection, "DELETE FROM RaffleOrders WHERE order_id = %s", (order_id,))

        # Now delete the order
        db.execute_query(db_connection, "DELETE FROM Orders WHERE order_id = %s", (order_id,))

        print(f"Order {order_id} deleted successfully.")
        flash("Order deleted successfully.")
        return redirect(url_for('orders.orders'))

    except Exception as e:
        print(f"Database error: {str(e)}")
        flash(f"Database error: {str(e)}")
        return redirect(url_for("orders.orders"))

    finally:
        db_connection.close()