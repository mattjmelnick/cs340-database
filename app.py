from flask import Flask, render_template
from blueprints.customers import customers_bp
from blueprints.sneakers import sneakers_bp
from blueprints.orders import orders_bp 
from blueprints.raffles import raffles_bp
from blueprints.drawings import drawings_bp
from blueprints.sneaker_orders import sneaker_orders_bp
from blueprints.raffle_orders import raffle_orders_bp
from blueprints.customer_raffles import customer_raffles_bp
import os

"""
Citation for this file:
Date: 2/24/25
Copied and modified from:
https://github.com/osu-cs340-ecampus/flask-starter-app/blob/master/bsg_people_app/app.py
"""


# Configuration
app = Flask(__name__)

# Routes 
@app.route('/')
def root():
    return render_template("index.j2")

# use blueprints to modularize the different pages
app.register_blueprint(customers_bp)
app.register_blueprint(sneakers_bp)
app.register_blueprint(orders_bp)
app.register_blueprint(raffles_bp)
app.register_blueprint(drawings_bp)
app.register_blueprint(sneaker_orders_bp)
app.register_blueprint(raffle_orders_bp)
app.register_blueprint(customer_raffles_bp)

# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9008)) 
    app.run(port=port, debug=True) 
