import pickle
from flask import Flask
from flask import request
from flask import jsonify
from pickle_script import load

dv = load("dv.bin")
model = load("model2.bin")


app = Flask("card")

@app.route('/card', methods=['POST'])
def predict():
    client = request.get_json()
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    card = y_pred >= 0.5

    result = {
        'card_probability': float(y_pred),
        'card': bool(card)
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port = 9696)