from cores import validate
from cores import fuzzer
import importlib


# Control modules
# All modules should be at folder "bigdig/modules/"
MODULE_DIR = "/modules/"

def parse_data(data):
    param = {}
    for i in data:
        section, value = i.split("=")
        param.update({section: value})
    return param



def run(module, method, urls, headers, data, point_inject, *proxy):
    if module:
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
                    params = parse_data(data)
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
                    params = parse_data(data)
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




