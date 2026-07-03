from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    crops = ["WHEAT", "MILLET", "MAIZE"]

    result = []
    for crop in crops:
        yield_val = round(random.uniform(55, 80), 2)
        price = random.randint(1800, 2600)
        profit = int(yield_val * price)

        result.append({
            "crop": crop,
            "yield": yield_val,
            "price": price,
            "profit": profit
        })

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)