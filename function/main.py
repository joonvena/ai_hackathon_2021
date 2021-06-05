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
        
        if TIIMA_ACTION == 'enter':
            return jsonify(tiima.user_enter())
    
    return jsonify({'error': 'Missing needed payload.'}), 400

