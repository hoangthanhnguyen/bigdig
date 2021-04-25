from cores import validate
from cores import fuzzer
from cores import argutils
import importlib
from cores import progress
from cores import utils


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
                        full_url = url
                        url, data = url.split("?")
                    except ValueError:
                        print("[x] GET request need parameters!")
                        return
                    data = data.split("&")
                    params = parse_params(data)
                    checking = 0
                    for payload in payloads:
                        checking += 1
                        progress.progress_bar(f"Checking: {checking}/{len(payloads)} payloads")
                        for pos in point_inject:
                            params.update({pos: payload})
                            response = fuzzer.send_request_get(url, headers, params, proxy)
                            if module.check(url, payload, response.text, point_inject):
                                utils.print_vulnerable(full_url, payload, point_inject)
                                exit()
                            else:
                                continue

                elif method == "POST":
                    data = data.split("&")
                    params = parse_params(data)
                    checking = 0
                    for payload in payloads:
                        checking += 1
                        progress.progress_bar(f"Checking: {checking}/{len(payloads)} payloads")
                        for pos in point_inject:
                            params.update({pos: payload})
                            response = fuzzer.send_request_post(url, headers, params)
                            if module.check(url, payload, response.text, point_inject):
                                utils.print_vulnerable(url, payload, point_inject)
                                exit()
                            else:
                                continue
                else:
                    # This statement for request PUT or DELETE
                    # https://stackoverflow.com/a/15367806/14934923
                    response = ""

        except ModuleNotFoundError:
            print("[x] Module not found!")
            return
    else:
        return




