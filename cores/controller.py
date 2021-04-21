import validate
import fuzzer
import importlib
from argutils import core_args


# Control modules
# All modules should be at folder "bigdig/modules/"
MODULE_DIR = "/modules/"

def parse_data(data):
    param = {}
    for i in data:
        section, value = i.split("=")
        param.update({section: value})
    return param

# args = core_args().parse_args()

def run(module, method, urls, headers, data, point_inject, payload):
    try:
        importlib.import_module(module)
        for url in urls:
            url, data = url.split("?")
            data = data.split("&")
            params = parse_data(data)
            params.update({point_inject: payload})
            if method == "GET":
                response = fuzzer.send_request_get(url=url, header=headers, params=params)
            elif method == "POST":
                pass
            else:
                pass
    except ModuleNotFoundError:
        print("[x] Module not found!")


