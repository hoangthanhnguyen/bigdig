import requests

def send_request_get(url, header, data):
    """

    :rtype: object
    """
    s = requests.Session()
    response = s.get(url=url, headers=header, data=data)
    return response

def send_request_post(url, header, data):
    s = requests.Session()
    response = s.post(url=url, headers=header, data=data)
    return response
