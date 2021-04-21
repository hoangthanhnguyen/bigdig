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



def run(module, method, urls, headers, data, point_inject):
    if module:
        try:
            module = importlib.import_module("modules." + str(module))
            module = module.Check()
            payload = module.payload
            for url in urls:
                if method == "GET":
                    try:
                        url, data = url.split("?")
                        data = data.split("&")
                        params = parse_data(data)
                        params.update({point_inject: payload})
                        response = fuzzer.send_request_get(url, headers, params)
                    except ValueError:
                        print("[x] GET request need parameters!")
                        return

                elif method == "POST":
                    data = data.split("&")
                    params = parse_data(data)
                    params.update({point_inject: payload})
                    response = fuzzer.send_request_post(url, headers, params)
                else:
                    # This statement for request PUT or DELETE
                    # https://stackoverflow.com/a/15367806/14934923
                    response = ""

        except ModuleNotFoundError:
            print("[x] Module not found!")
    else:
        pass

    try:
        return response
    except UnboundLocalError:
        print("[x] Do you have url & data?")




