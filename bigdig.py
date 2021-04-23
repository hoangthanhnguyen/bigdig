# from cores import *
from cores import controller
from cores import validate
# from modules import *
from cores.argutils import core_args
# import sys

args = core_args().parse_args()


class UserOpts(object):
    def __init__(self):
        self.module = args.module
        self.method = args.method
        self.urls = validate.check_target(args.url, args.list_urls)
        self.point_inject = args.point_inject
        self.headers = validate.check_headers(args.headers, args.user_agent, args.cookie)
        self.data = args.data
        self.proxy = args.proxy
        self.payload = ""


if __name__ == "__main__":
    flags = core_args()
    try:
        # sys.argv[1]
        main = UserOpts()
        response = controller.run(main.module, main.method, main.urls, main.headers, main.data, main.point_inject,
                                  main.proxy)
    except IndexError:
        flags.print_help()
