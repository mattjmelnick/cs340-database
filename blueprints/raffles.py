from flask import Blueprint, render_template, request, redirect, url_for
import database.db_connector as db

raffles_bp = Blueprint('raffles', __name__)


@raffles_bp.route('/raffles', methods=["GET", "POST"])
def raffles():
    db_connection = db.connect_to_database()
    try:
        if request.method == "POST":
            # get the input data from the add raffle form
            sneaker_id= request.form.get("raffleSneakerID")
            raffle_description= request.form.get("raffleDescription")
            entry_cost= request.form.get("raffleEntryCost")
            # add the new raffle to the database
            query = "INSERT INTO Raffles (sneaker_id, raffle_description, entry_cost) VALUES (%s, %s, %s)"
            db.execute_query(db_connection=db_connection, query=query, query_params=(sneaker_id, raffle_description, entry_cost))

            # return to raffle page
            return redirect(url_for('raffles.raffles'))

        if request.method == "GET":
            # display the data from the database in the table
            query = "SELECT * FROM Raffles"
            cursor = db.execute_query(db_connection=db_connection, query=query)
            results = cursor.fetchall()
            fetch_sneaker_query = "SELECT * FROM Sneakers"
            fetch_sneaker_cursor = db.execute_query(db_connection=db_connection, query=fetch_sneaker_query)
            sneaker_result = fetch_sneaker_cursor.fetchall()

            return render_template("raffles.j2", raffles=results, sneakers=sneaker_result)
    finally:
        db_connection.close()


@raffles_bp.route('/edit_raffle/<int:raffle_id>', methods=["POST"])
def edit_raffle(raffle_id):
    db_connection = db.connect_to_database()
    try:
        # get the input data from the update raffle form
        sneaker_id = request.form.get("raffleSneakerIDUpdate")
        raffle_description = request.form.get("raffleDescriptionUpdate")
        entry_cost = request.form.get("raffleEntryCostUpdate")
        # update the raffe in the database using the input data
        query = """UPDATE Raffles SET sneaker_id = %s, raffle_description = %s,
            entry_cost = %s WHERE raffle_id = %s"""
        db.execute_query(db_connection=db_connection, query=query, query_params=(sneaker_id, raffle_description, entry_cost, raffle_id))

        # return to raffles page
        return redirect(url_for('raffles.raffles'))
    finally:
        db_connection.close()

@raffles_bp.route('/delete_raffle/<int:raffle_id>', methods=["POST"])
def delete_raffle(raffle_id):
    db_connection = db.connect_to_database()
    try:
        # delete the selected raffle from the database
        query = f"DELETE FROM Raffles WHERE raffle_id = {raffle_id}"
        db.execute_query(db_connection=db_connection, query=query)

        # return to raffles page
        return redirect(url_for('raffles.raffles'))
    finally:
        db_connection.close()