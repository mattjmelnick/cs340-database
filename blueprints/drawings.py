from flask import Blueprint, render_template, request, redirect, url_for
import database.db_connector as db

drawings_bp = Blueprint('drawings', __name__)
db_connection = db.connect_to_database()

@drawings_bp.route('/drawings')
def drawings():
    return render_template("drawings.j2")
