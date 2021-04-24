import sys


def progress_bar(message):
    sys.stdout.write(message)
    sys.stdout.flush()
    sys.stdout.write("\r")
