import requests

def send_request_get(url, header, data):
    """

    :rtype: object
    """
    response = requests.get(url=url, headers=header, data=data)
    return response

def send_request_post(url, header, data):
    response = requests.post(url=url, headers=header, data=data)
    return response
