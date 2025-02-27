from flask import Blueprint, render_template, request, redirect, url_for
import database.db_connector as db

sneakers_bp = Blueprint('sneakers', __name__)
db_connection = db.connect_to_database()

@sneakers_bp.route('/sneakers')
def sneakers():
    return render_template("sneakers.j2")
