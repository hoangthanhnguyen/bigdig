# from cores import *
import importlib

from cores import controller
from cores import validate
# from modules import *
from cores.argutils import core_args
# import sys

args = core_args().parse_args()
args.point_inject = validate.check_param(args.point_inject)
args.headers = validate.check_headers(args.headers, args.user_agent, args.cookie)


class UserOpts(object):
    def __init__(self):
        self.module = args.module
        self.method = args.method
        self.urls = validate.check_target(args.url, args.list_urls)
        self.point_inject = args.point_inject
        self.headers = args.headers
        self.data = args.data
        self.proxy = args.proxy
        self.payload = ""


if __name__ == "__main__":
    flags = core_args()
    try:
        # sys.argv[1]
        main = UserOpts()
        if main.module == "sqli":
            response = controller.run(main.module, main.method, main.urls, main.headers, main.data, main.point_inject,
                                  main.proxy)
        elif main.module == "xss":
            module = importlib.import_module("modules." + str(main.module))
            module.create_session(args)
        else:
            print("[x] Module not found!")
    except IndexError:
        flags.print_help()
