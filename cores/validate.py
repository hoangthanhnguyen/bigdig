from cores import argutils
import re
import os.path


# regex for validate url
# https://stackoverflow.com/a/7160778/14934923
regex = re.compile(
    r'^(?:http)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


# TODO check module
def check_module(module_name):
    try:
        import importlib
        module = importlib.import_module("modules." + module_name)
    except ModuleNotFoundError:
        print(f"[x] Invalid module name {module_name}. Use flag -l or --list for list all modules.")


# TODO check request from file
# TODO check target
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

    else:
        if url:
            if re.match(regex, url):
                urls.append(url)
            else:
                print("[x] Invalid url. Example: https://www.example.com")
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
    return data


# args = core_args().parse_args()
# a = check_target(args.url, args.list_urls)
