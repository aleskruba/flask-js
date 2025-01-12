from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime


app = Flask(__name__)
CORS(app)  

request_count = {}

# Define the request limit per day
REQUEST_LIMIT = 5

# Helper function to get today's date as a string
def get_today_date():
    return datetime.today().strftime('%Y-%m-%d')

@app.route('/api/', methods=['POST'])
def handle_post():
    global request_count

    # Get the current date
    today_date = get_today_date()

    # Retrieve data from the frontend
    data = request.get_json()
    phone_number = data.get('phoneNumber')
    print("Data from frontend:", phone_number)

    if not phone_number:
        return jsonify({"error": "Nesnmí být prázdné"})

    # Check if the request count for today exceeds the limit
    if today_date in request_count and request_count[today_date] >= REQUEST_LIMIT:
        return jsonify({"error": f"Můžeš poslat pouze {REQUEST_LIMIT} requestů za den"})

    # Increment the request count for today
    if today_date in request_count:
        request_count[today_date] += 1
    else:
        request_count[today_date] = 1

    # Respond with the data
    response_data = [
        {"api_call": request_count[today_date], "id": 1, "number": phone_number, "title": "data from file 1"},
        {"api_call": request_count[today_date], "id": 2, "number": phone_number, "title": "data from file 2"},
        {"api_call": request_count[today_date], "id": 3, "number": phone_number, "title": "data from file 3"}
    ]
    
    return jsonify(response_data)
if __name__ == '__main__':
    app.run(debug=True)
