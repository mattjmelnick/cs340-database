from flask import Blueprint, render_template, request, redirect, url_for, g
import database.db_connector as db

"""
Citation for this file:
Date: 3/1/25 
All blueprint pages are modified from:
https://github.com/osu-cs340-ecampus/flask-starter-app/blob/master/bsg_people_app/app.py

Additional resource used:
https://realpython.com/flask-blueprint/
"""


sneakers_bp = Blueprint('sneakers', __name__)

@sneakers_bp.route('/sneakers', methods=["GET", "POST"])
def sneakers():
    db_connection = g.db_connection
    if request.method == "POST":
        # get the input data from the add sneaker form
        brand = request.form.get("sneakerBrand")
        model_name = request.form.get("sneakerModel")
        size = request.form.get("sneakerSize")
        colorway = request.form.get("sneakerColorway")
        price = request.form.get("sneakerPrice")
        stock_count = request.form.get("sneakerStock")
        # add the new sneaker to the database
        query = """INSERT INTO Sneakers (brand, model_name, size, colorway, price, stock_count) 
                    VALUES (%s, %s, %s, %s, %s, %s)"""
        db.execute_query(db_connection=db_connection,
                                    query=query,
                                    query_params=(brand, model_name, size, colorway, price, stock_count))
        
        # return to sneakers page
        return redirect(url_for('sneakers.sneakers'))

    if request.method == "GET":
        # display the data from the database in the table
        query = "SELECT * FROM Sneakers"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()

        return render_template("sneakers.j2", sneakers=results)

@sneakers_bp.route('/edit_sneaker/<int:sneaker_id>', methods=["POST"])
def edit_sneaker(sneaker_id):
    db_connection = g.db_connection
    # get the input data from the add sneaker form
    brand = request.form.get("sneakerBrandUpdate")
    model_name = request.form.get("sneakerModelUpdate")
    size = request.form.get("sneakerSizeUpdate")
    colorway = request.form.get("sneakerColorwayUpdate")
    price = request.form.get("sneakerPriceUpdate")
    stock_count = request.form.get("sneakerStockUpdate")
    # add the new sneaker to the database
    query = """UPDATE Sneakers SET brand = %s, model_name = %s, size = %s,
                colorway = %s, price = %s, stock_count = %s WHERE sneaker_id = %s"""
    db.execute_query(db_connection=db_connection,
                                query=query,
                                query_params=(brand, model_name, size, colorway, price, stock_count, sneaker_id))
    
    # return to sneakers page
    return redirect(url_for('sneakers.sneakers'))

@sneakers_bp.route('/delete_sneaker/<int:sneaker_id>', methods=["POST"])
def delete_sneaker(sneaker_id):
    db_connection = g.db_connection
    # delete the selected sneaker from the database
    query = f"DELETE FROM Sneakers WHERE sneaker_id = {sneaker_id}"
    db.execute_query(db_connection=db_connection, query=query)

    # return to sneakers page
    return redirect(url_for('sneakers.sneakers'))
