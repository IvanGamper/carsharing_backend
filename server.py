from flask import Flask, jsonify, request, render_template
import os
app = Flask(__name__)

cars = [
    {"id": 1, "brand": "Tesla", "model": "Model 3", "available": True},
    {"id": 2, "brand": "BMW", "model": "i3", "available": True},
]

template_dir = os.path.abspath("C:/Users/ivang/carsharing_backend/templates")
app = Flask(__name__, template_folder=template_dir)
# Route für die Startseite
@app.route('/')
def home():
    return render_template('index.html')  # Lädt die index.html im templates-Ordner

@app.route('/cars', methods=['GET'])
def get_cars():
    return jsonify(cars)

@app.route('/rent', methods=['POST'])
def rent_car():
    data = request.json
    for car in cars:
        if car["id"] == data["id"] and car["available"]:
            car["available"] = False
            return jsonify({"message": "Car rented successfully!"})
    return jsonify({"message": "Car not available!"}), 400

if __name__ == '__main__':
    app.run(debug=False)

    print(os.getcwd())