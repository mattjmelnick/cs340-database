from flask import Blueprint, render_template, request, redirect, url_for
import database.db_connector as db

orders_bp = Blueprint('orders', __name__)
db_connection = db.connect_to_database()

@orders_bp.route('/orders')
def orders():
    return render_template("orders.j2")
