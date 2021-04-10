import argparse
from argparse import ArgumentError
import sys


class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        """
        Disable exit on error to get parameters of arguments
        https://stackoverflow.com/a/16942165
        :param message: error message
        :return:
        """
        print(message)


class PluginArgumentParser(argparse.ArgumentParser):
    pass


def core_args():
    parser = ArgumentParser()
    group_core = parser.add_argument_group("Core")
    group_core.add_argument(
        "-m",
        "--module",
        metavar="Module",
        help="Select module"
    )
    group_search = parser.add_argument_group("Search")
    group_search.add_argument(
        "-l",
        "--list",
        action='store_true',
        default=False,
        help="List modules"
    )
    group_target = parser.add_argument_group("Target")
    group_target.add_argument(
        "-u",
        "--url",
        required=True,
        metavar="URL",
        help="""Target URL (e.g. "http://example.com/vuln.php?id=1")"""
    )
    group_target.add_argument(
        "-r",
        metavar="REQUESTFILE",
        help="Load HTTP request from a file"
    )
    group_request = parser.add_argument_group("Request")
    group_request.add_argument(
        "-A",
        "--user-agent",
        metavar="AGENT",
        help="HTTP User-Agent header value (default: bigdig/1.0)",
        default="bigdig/1.0"
    )
    group_request.add_argument(
        "-H",
        "--headers",
        metavar="HEADERS",
        help="""Extra headers (e.g. "X-Forwarded-For: 127.0.0.1")"""
    )
    group_request.add_argument(
        "--method",
        metavar="METHOD",
        help="Force usage of given HTTP method (default: GET)",
        default="GET"
    )
    group_request.add_argument(
        "--data",
        metavar="DATA",
        help="""Data string to be sent through POST (e.g. "id=1")"""
    )
    group_request.add_argument(
        "--cookie",
        metavar="COOKIE",
        help="""HTTP Cookie header value (e.g. "PHPSESSID=a6s8492..")"""
    )
    group_request.add_argument(
        "--delay",
        metavar="DELAY",
        help="Delay in seconds between each HTTP request"
    )

    return parser


if __name__ == "__main__":
    args = core_args()
    args.print_help()
