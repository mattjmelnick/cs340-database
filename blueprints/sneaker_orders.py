from flask import Blueprint, render_template, request, redirect, url_for
import database.db_connector as db

sneaker_orders_bp = Blueprint('sneaker_orders', __name__)
db_connection = db.connect_to_database()

@sneaker_orders_bp.route('/sneaker_orders')
def sneaker_orders():
    return render_template("sneaker_orders.j2")
