from flask import Blueprint, render_template, request, redirect, url_for
import database.db_connector as db

raffles_bp = Blueprint('raffles', __name__)
db_connection = db.connect_to_database()

@raffles_bp.route('/raffles')
def raffles():
    return render_template("raffles.j2")
