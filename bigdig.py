# from cores import *
import importlib
from pyfiglet import Figlet
import shutil



from cores import controller
from cores import validate
# from modules import *
from cores.argutils import core_args
import sys

def show_banner():
    f = Figlet(font='standard')
    print(*[x.center(shutil.get_terminal_size().columns) for x in f.renderText("b1gdIg").split("\n")],sep="\n")
    print("\033[91m--------\033[32m\033[32mAuthor:\033[0m \033[96mNguyễn Hoàng Thành\033[91m--------\033[0m")
    print("\033[91m---\033[32mEmail: \033[96msmith.nguyenhoangthanh@gmail.com\033[91m---\033[0m")
    # print("-----[ Gitlab:\033[94m https://nest.parrotsec.org/packages/tools/pxss/\033[0m ]---")


args = core_args().parse_args()
args.point_inject = validate.check_param(args.point_inject)
args.headers = validate.check_headers(args.headers, args.user_agent, args.cookie)
validate.list_modules(args.list)


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
    show_banner()
    flags = core_args()
    try:
        sys.argv[1]
        main = UserOpts()
        if main.module == "sqli":
            response = controller.run(main.module, main.method, main.urls, main.headers, main.data, main.point_inject,
                                  main.proxy)
        elif main.module == "xss":
            module = importlib.import_module("modules." + str(main.module))
            module.create_session(args)
        elif main.module != None:
            print("[x] Module not found!")
        else:
            print("[x] The following arguments are required: -m/--module")
    except IndexError:
        flags.print_help()
