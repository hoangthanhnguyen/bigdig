from cores import *
from cores import controller
from cores import validate
from modules import *
from cores.argutils import core_args
import importlib

args = core_args().parse_args()

class main(object):
    def __init__(self):
        self.module = args.module
        self.method = args.method
        self.urls = validate.check_target(args.url, args.list_urls)
        self.point_inject = args.point_inject
        self.headers = validate.check_headers(args.headers, args.user_agent, args.cookie)
        self.data = args.data
        self.payload = ""

if __name__ == "__main__":
    flags = core_args()
    if args:
        main = main()
        response = controller.run(main.module, main.method, main.urls, main.headers, main.data, main.point_inject)
    else:
        flags.print_help()