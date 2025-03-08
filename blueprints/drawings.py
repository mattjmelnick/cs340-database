from flask import Blueprint, render_template, request, redirect, url_for
import database.db_connector as db

drawings_bp = Blueprint('drawings', __name__)
db_connection = db.connect_to_database()

@drawings_bp.route('/drawings', methods=["GET", "POST"])
def drawings():
    db_connection = db.connect_to_database()
    try:
        if request.method == "POST":
            # get the input data from the add drawing form
            raffle_id= request.form.get("drawingRaffleID")
            draw_date= request.form.get("drawingDate")
            draw_day= request.form.get("drawingDay")
            # add the new drawing to the database
            query = "INSERT INTO Drawings (raffle_id, draw_date, draw_day) VALUES (%s, %s, %s)"
            db.execute_query(db_connection=db_connection, query=query, query_params=(raffle_id, draw_date, draw_day))

            # return to drawing page
            return redirect(url_for('drawings.drawings'))

        if request.method == "GET":
            # display the data from the database in the table
            query = "SELECT * FROM Drawings"
            cursor = db.execute_query(db_connection=db_connection, query=query)
            results = cursor.fetchall()
            fetch_raffle_query = "SELECT * FROM Raffles"
            fetch_raffle_cursor = db.execute_query(db_connection=db_connection, query=fetch_raffle_query)
            raffle_result = fetch_raffle_cursor.fetchall()

            return render_template("drawings.j2", drawings=results, raffles=raffle_result)
    finally:
        db_connection.close()

@drawings_bp.route('/edit_drawing/<int:drawing_id>', methods=["POST"])
def edit_drawing(drawing_id):
    db_connection = db.connect_to_database()
    try:
        # get the input data from the update drawing form
        raffle_id = request.form.get("drawingRaffleIDUpdate")
        draw_date = request.form.get("drawingDateUpdate")
        draw_day = request.form.get("drawingDayUpdate")
        # update the drawing in the database using the input data
        query = """UPDATE Drawings SET raffle_id = %s, draw_date = %s,
            draw_day = %s WHERE drawing_id = %s"""
        db.execute_query(db_connection=db_connection, query=query, query_params=(raffle_id, draw_date, draw_day, drawing_id))

        # return to drawings page
        return redirect(url_for('drawings.drawings'))
    finally:
        db_connection.close()

@drawings_bp.route('/delete_drawing/<int:drawing_id>', methods=["POST"])
def delete_drawing(drawing_id):
    db_connection = db.connect_to_database()
    try:
        # delete the selected drawing from the database
        query = f"DELETE FROM Drawings WHERE drawing_id = {drawing_id}"
        db.execute_query(db_connection=db_connection, query=query)

        # return to customers page
        return redirect(url_for('drawings.drawings'))
    finally:
        db_connection.close()

