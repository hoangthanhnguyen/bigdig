from argutils import core_args
import re

methods = ["GET", "POST", "PUT", "DELETE"]
args = core_args().parse_args()


# TODO check module
def check_module(module_name):
    try:
        import importlib
        module = importlib.import_module("modules." + module_name)
    except ModuleNotFoundError:
        print(f"[x] Invalid module name {module_name}. Use flag -l or --list for list all modules.")

# TODO check request from file
# TODO check target
def check_target(url, requestfile):
    if requestfile:
        print("Requestfile is exits")
    else:
        if url:
            regex = re.compile(
                r'^(?:http)s?://'  # http:// or https://
                r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
                r'localhost|'  # localhost...
                r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
                r'(?::\d+)?'  # optional port
                r'(?:/?|[/?]\S+)$', re.IGNORECASE)
            if re.match(regex, url):
                return True
            else:
                print("[x] Invalid url. Example: https://www.example.com")


# TODO check method
def check_method(method):
    pass


# TODO check headers
def check_headers(headers):
    pass


# TODO check user agent
def check_user_agent(user_agent):
    pass


# TODO check cookie
def check_cookie(cookie):
    pass


# TODO check data
def check_data(data):
    pass


# TODO check delay
def check_delay(delay):
    pass


a = check_target(args.url, args.requestfile)
