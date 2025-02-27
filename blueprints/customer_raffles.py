from flask import Blueprint, render_template, request, redirect, url_for, json
import database.db_connector as db

customer_raffles_bp = Blueprint('customer_raffles', __name__)
db_connection = db.connect_to_database()

@customer_raffles_bp.route('/customer_raffles')
def customer_raffles():
    return render_template("customer_raffles.j2")
