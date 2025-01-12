from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

api_call = 0

@app.route('/api/', methods=['POST'])
def handle_post():
    global api_call
    
    data = request.get_json()
    phone_number = data.get('phoneNumber')
    print("data z frontendu: ", phone_number)

    
    if not phone_number:
        return jsonify({"error": "Phone number is required"}), 400
    
    # tady  vytvoříš logic pro  telefoní čislo
    response_data = [
        
        {"api_call":api_call,"id": 1, "number": phone_number,"title": "data ze souboru 1"},
        {"api_call":api_call,"id": 2, "number": phone_number,"title": "data ze souboru 2"},
        {"api_call":api_call,"id": 3, "number": phone_number,"title": "data ze souboru 3"}
    ]
    api_call += 1
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
