from flask import Flask, render_template
import os

# Configuration

app = Flask(__name__)

# Routes 

@app.route('/', methods=["GET", "POST"])
def root():
    return render_template("index.j2")

@app.route('/customers')
def customers():
    return render_template("customers.j2")

@app.route('/sneakers')
def sneakers():
    return render_template("sneakers.j2")

@app.route('/orders')
def orders():
    return render_template("orders.j2")

@app.route('/raffles')
def raffles():
    return render_template("raffles.j2")

@app.route('/drawings')
def drawings():
    return render_template("drawings.j2")

@app.route('/sneaker_orders')
def sneaker_orders():
    return render_template("sneaker_orders.j2")

@app.route('/raffle_orders')
def raffle_orders():
    return render_template("raffle_orders.j2")

@app.route('/customer_raffles')
def customer_raffles():
    return render_template("customer_raffles.j2")

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9008)) 
    app.run(port=port, debug=True) 