from flask import Flask , jsonify, request


app = Flask(__name__)


@app.route('/add', methods=['GET'])
def add():
    a = request.args.get('a',type=float)
    b = request.args.get('b',type=float)
    if a is None or b is None:
        return josonify({"Errors": "Provide a and b as query params"}), 400
    return jsonify({"result": a + b})

@app.route('/subtract', methods=['GET'])
def subtract():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify({"error": "Provide a and b as query params"}), 400
    return jsonify({"result": a - b})

@app.route('/multiply', methods=['GET'])

@app.route('/multiply', methods=['GET'])
def multiply():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify({"error": "Provide a and b as query params"}), 400
    return jsonify({"result": a * b})

@app.route('/divide', methods=['GET'])
def divide():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify({"error": "Provide a and b as query params"}), 400
    if b == 0:
        return jsonify({"error": "Cannot divide by zero"}), 400
    return jsonify({"result": a / b})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(debug=True)
