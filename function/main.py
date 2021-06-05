from datetime import datetime
from tiima import Tiima
from flask import abort, jsonify

def tiima_function(request):
    request_params = request.get_json()
    TIIMA_COMPANY_ID = request_params['tiima_company_id']
    TIIMA_API_KEY = request_params['tiima_api_key']
    TIIMA_USERNAME = request_params['tiima_username']
    TIIMA_PASSWORD = request_params['tiima_password']
    TIIMA_ACTION = request_params['action']
    
    if TIIMA_COMPANY_ID and TIIMA_API_KEY and TIIMA_USERNAME and TIIMA_PASSWORD:
        tiima = Tiima(company_id=TIIMA_COMPANY_ID, api_key=TIIMA_API_KEY)
        tiima.login(username=TIIMA_USERNAME, password=TIIMA_PASSWORD)

        status = tiima.user_state()

        if TIIMA_ACTION == 'status':
            return jsonify(tiima.user_state())

        elif TIIMA_ACTION == 'in_out':
            if status['statusCode'] == 'In':
                return jsonify(tiima.user_leave())
            else:
                return jsonify(tiima.user_enter())

        elif TIIMA_ACTION == 'lunch':
            if status['statusCode'] == 'Lunch':
                return jsonify(tiima.user_from_lunch())
            else:
                return jsonify(tiima.user_to_lunch())
    
    return jsonify({'error': 'Missing needed payload.'}), 400

