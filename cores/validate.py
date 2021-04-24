from cores import argutils
import re
import os.path
import importlib


# regex for validate url
# https://stackoverflow.com/a/7160778/14934923
regex = re.compile(
    r'^(?:http)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def parse_params(data):
    params = {}
    for param in data:
        key, value = param.split("=")
        params.update({key: value})
    return params


def parse_param_from_url(url):
    if "?" not in url:
        return None
    data = url.split("?")[1].split("&")
    # TODO support DOM
    return url.split("?")[0], parse_params(data)

def check_param(point_inject):
    if point_inject:
        point_inject = point_inject.split(",")
    return point_inject


def check_module(module_name):
    try:
        import importlib
        module = importlib.import_module("modules." + module_name)
    except ModuleNotFoundError:
        print(f"[x] Invalid module name {module_name}. Use flag -l or --list for list all modules.")


# TODO check request from file

def check_target(url, list_urls):
    urls = []
    if list_urls:
        if os.path.exists(list_urls):
            try:
                with open(list_urls, 'r') as f:
                    urls = f.readlines()
                    for i in range(len(urls)):
                        if re.match(regex, urls[i]):
                            urls.append(urls[i])
                        else:
                            print("[x] Invalid url: " + urls[
                                i] + " Example: https://www.example.com or http://www.example.com")

            except FileNotFoundError:
                print("[x] File " + str(list_urls) + " does not exist!")
        else:
            print("[x] File " + str(list_urls) + " does not exist!")

    elif url:
            if re.match(regex, url):
                urls.append(url)
            else:
                print("[x] Invalid url. Example: https://www.example.com")

    else:
        print("[x] The following arguments are required: -u/--url or -us/--urls")
    return urls


# TODO check headers
def check_headers(headers, user_agent, cookie):
    if headers:
        if type(headers) != dict:
            print("""[x] Headers invalid format! e.g. "{'X-Forwarded-For': '127.0.0.1', 'projectName': 'zhikovapp', 
                'Authorization': 'Bearer HZCdsf='}" """)
        elif headers["cookie"] or headers["Cookie"]:
            print("[x] Use --cookie for cookie header!")
        elif headers["user-agent"] or headers["User-agent"]:
            print("[x] Use -A or --user-agent for user agent header!")
        else:
            headers.update({"User-agent": user_agent})
            headers.update({"Cookie": cookie})
    else:
        headers = {}
        headers["User-agent"] = user_agent
        if cookie:
            headers["Cookie"] = cookie
        else:
            pass
    return headers


# TODO check data
def check_data(data):
    return parse_params(data)

# check argument -l/--list
def list_modules(list):
    if list:
        from os import listdir
        from os.path import isfile, join
        all_modules = [f for f in listdir("modules") if isfile(join("modules", f))]
        print("List all modules:\n")
        for i in all_modules:
            if "__" in i:
                continue
            elif "_" in i:
                continue
            else:
                print("[+] " + i.replace(".py", ""))

        exit()
    else:
        return

# args = core_args().parse_args()
# a = check_target(args.url, args.list_urls)
