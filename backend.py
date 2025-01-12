from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route('/api/', methods=['POST'])
def handle_post():
    
    data = request.get_json()
    phone_number = data.get('phoneNumber')
    print("data z frontendu: ", phone_number)

    
    if not phone_number:
        return jsonify({"error": "Phone number is required"}), 400
    
    # tady  vytvoříš logic pro  telefoní čislo
    response_data = [
        {"id": 1, "number": phone_number,"title": "data ze souboru 1"},
        {"id": 2, "number": phone_number,"title": "data ze souboru 2"},
        {"id": 3, "number": phone_number,"title": "data ze souboru 3"}
    ]
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
