from cores import validate
from cores import fuzzer
from cores import argutils
import importlib


# Control modules

def parse_params(data):
    param = {}
    for i in data:
        section, value = i.split("=")
        param.update({section: value})
    return param

def parse_param_from_url(url):
    if "?" not in url:
        return None
    data = url.split("?")[1].split("&")
    # TODO support DOM
    return url.split("?")[0], parse_params(data)


def run(module, method, urls, headers, data, point_inject, *proxy):
    if module == "sqli":
        try:
            module = importlib.import_module("modules." + str(module))
            module = module.Check()
            payloads = module.gen_payload()
            for url in urls:
                if method == "GET":
                    try:
                        url, data = url.split("?")
                    except ValueError:
                        print("[x] GET request need parameters!")
                        return
                    data = data.split("&")
                    params = parse_params(data)
                    for payload in payloads:
                        params.update({point_inject: payload})
                        response = fuzzer.send_request_get(url, headers, params, proxy)
                        if module.check(url, payload, response.text, point_inject):
                            print("Yes")
                            break
                        else:
                            print("No")

                elif method == "POST":
                    data = data.split("&")
                    params = parse_params(data)
                    for payload in payloads:
                        params.update({point_inject: payload})
                        response = fuzzer.send_request_post(url, headers, params)
                else:
                    # This statement for request PUT or DELETE
                    # https://stackoverflow.com/a/15367806/14934923
                    response = ""

        except ModuleNotFoundError:
            print("[x] Module not found!")
            return
    else:
        return
    try:
        return response
    except UnboundLocalError:
        print("[x] Do you have url & data?")




