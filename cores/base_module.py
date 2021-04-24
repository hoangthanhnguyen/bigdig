import re
from cores import utils


class Scanner(object):
    def __init__(self):
        self.payload = self.gen_payload()
        self.signatures = self.signature()

    def check(self, url, payload, response, parameter):
        # Run this for auto scan
        for injection_types in self.signatures.keys():
            for sig in self.signatures[injection_types]:
                match = re.findall(re.escape(sig), response)
                if match:
                    # print("[*] [\033[31m%s\033[00m] [\033[4m\033[40m%s\033[00m] [\033[4m\033[31m%s\033[00m: \033[
                    # 4m\033[33;1m%s\033[00m]" % ( injection_types, url, parameter, payload))
                    utils.print_info(sig)
                    return True
        return False

    def fuzz(self, payload, response, method, size, parameter):
        # Run this for fuzzer task
        for injection_types in self.signatures.keys():
            for sig in self.signatures[injection_types]:
                match = re.findall(re.escape(sig), response)
                if match:
                    return injection_types
        return False

    def gen_payload(self):
        return []

    def signature(self):
        return {}
