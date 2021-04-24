

def print_vulnerable(uri, payload="", point_inject=""):
    # Bright Magenta
    print(f"  [\033[96m*\033[0m] \033[96m{uri}\033[0m is\033[91m vulnerable\033[0m")
    if payload:
        print(f"  Payload: \033[95m{payload}\033[0m")
    if point_inject:
        print(f"  Parameter: \033[96m{point_inject}\033[0m")


def print_not_vulnerable(url):
    # Bright yellow
    print(f"  [\033[93m!\033[0m] \033[93m{url}\033[0m is\033[37m not vulnerable\033[0m")


def print_debug(message, payload, res_payload):
    print(f"  [\033[97m*\033[0m] \033[97m{message}\033[0m")
    print(f"  Payload: \033[35m{payload}\033[0m")
    print(f"  Response: \033[95m{res_payload}\033[0m")


def print_info(message):
    print(f"  [\033[97m*\033[0m] \033[97m{message}\033[0m")


def print_heuristic(payload):
    print("  [\033[93m!\033[0m] Server didn't encode HTML tag. It is still exploitable.")
    print(f"  Payload: \033[35m{payload}\033[0m")


def print_blocked():
    print("  [\033[91m!\033[0m] Payload is blocked by server.")


def print_verbose(message):
    print(f"[+] {message}")
