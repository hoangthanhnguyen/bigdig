import requests

def send_request_get(url, header, data, *proxy):
    """

    :rtype: object
    """
    s = requests.Session()
    # s.proxies.update({list(proxy.keys())[0]: list(proxy.values())[0]})
    response = s.get(url=url, headers=header, params=data)
    return response

def send_request_post(url, header, data):
    s = requests.Session()
    response = s.post(url=url, headers=header, data=data)
    return response
