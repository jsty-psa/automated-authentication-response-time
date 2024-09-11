import requests, time

def authenticate():
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

    print('Initiating Request.....')
    
    start_time = time.time()

    response = requests.get(authentication_url, params=authentication_request_body)
    
    stop_time = time.time()

    minutes, seconds = divmod(stop_time - start_time, 60)

    if not response.json()['errors']:
        print('Success Response Captured.')
        print(f'Time Finished: {minutes} minutes and {int(seconds):02} seconds')
    else:
        print('Failed Response Captured')
        print(f'Time Finished: {minutes} minutes and {int(seconds):02} seconds')

    print('\n\n')

    # sleep
    time.sleep(5)

    # recursion
    authenticate()

authenticate()