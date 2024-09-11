from datetime import datetime

import os, requests, time

def initiate_authentication():
    demographic_basic_authentication()
    demographic_ekyc_authentication()

    time.sleep(3600)
    initiate_authentication()

def demographic_basic_authentication():
    authentication_request_body = {}

    authentication_request_body['individual_id'] = "5872130947327698"
    authentication_request_body['individual_id_type'] = "VID"
    authentication_request_body['input_bio'] = "off"
    authentication_request_body['input_otp'] = "off"
    authentication_request_body['input_demo'] = "on"
    authentication_request_body['input_ekyc'] = "off"
    authentication_request_body['input_otp_value'] = None
    authentication_request_body['input_demo_value'] = '{"age": 0}'

    authentication_url = "http://10.10.20.121:8000/authenticate"

    start_time = time.time()

    response = requests.get(authentication_url, params=authentication_request_body)
    response = response.json()
    
    stop_time = time.time()

    minutes, seconds = divmod(stop_time - start_time, 60)

    now = datetime.now()
    file_name = f'logs/log_{now.strftime('%Y-%m-%d')}'
    date_time = now.strftime('%Y-%m-%d %I:%M:%S')
    result = f"[{date_time}]\n"

    if not 'errors' in response:
        result += f"\tDemographic Basic Authentication Success Response Captured\n"
        result += f"\tResponse: {response}\n\n"
    else:
        result += f"\tDemographic Basic Authentication Failed Response Captured\n"
        result += f"\tResponse: {response['errors']['errorCode']} - {response['errors']['errorMessage']}\n"

    result += f'\tTime Finished: { format(seconds, '.2f') } seconds\n\n'

    print(f"Authentication request has been initiated. as of {date_time}\n")

    if not os.path.isdir('logs'):
        os.makedirs('logs')

    if not os.path.isfile(file_name):
        with open(file_name, 'x') as file:
            file.write(result)
    else:
        with open(file_name, 'a') as file:
            file.write(result)

def demographic_ekyc_authentication():
    authentication_request_body = {}

    authentication_request_body['individual_id'] = "5872130947327698"
    authentication_request_body['individual_id_type'] = "VID"
    authentication_request_body['input_bio'] = "off"
    authentication_request_body['input_otp'] = "off"
    authentication_request_body['input_demo'] = "on"
    authentication_request_body['input_ekyc'] = "on"
    authentication_request_body['input_otp_value'] = None
    authentication_request_body['input_demo_value'] = '{"age": 0}'

    authentication_url = "http://10.10.20.121:8000/authenticate"

    start_time = time.time()

    response = requests.get(authentication_url, params=authentication_request_body)
    response = response.json()
    
    stop_time = time.time()

    minutes, seconds = divmod(stop_time - start_time, 60)

    now = datetime.now()
    file_name = f'logs/log_{now.strftime('%Y-%m-%d')}'
    date_time = now.strftime('%Y-%m-%d %I:%M:%S')
    result = f"[{date_time}]\n"

    if not 'errors' in response:
        result += f"\tDemographic eKYC Authentication Success Response Captured\n"
        result += f"\tResponse: {response}\n\n"
    else:
        result += f"\tDemographic eKYC Authentication Failed Response Captured\n"
        result += f"\tResponse: {response['errors']['errorCode']} - {response['errors']['errorMessage']}\n"

    result += f'\tTime Finished: { format(seconds, '.2f') } seconds\n\n'

    print(f"Authentication request has been initiated. as of {date_time}\n")

    if not os.path.isdir('logs'):
        os.makedirs('logs')

    if not os.path.isfile(file_name):
        with open(file_name, 'x') as file:
            file.write(result)
    else:
        with open(file_name, 'a') as file:
            file.write(result)


initiate_authentication()