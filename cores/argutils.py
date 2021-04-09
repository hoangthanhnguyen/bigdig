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

