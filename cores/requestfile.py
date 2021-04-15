file_get = "get"
file_post = "post"

print("Debug: Get file")
print(open(file_get).read().split("\n"))
print("\nDebug: Post file")
print(open(file_post).read().split("\n"))


def parse_proto(line):
    # Try return except raise(invalid format)
    http_method, path, http_ver = line.split(" ")
    return http_method, path, http_ver


def parse_req(data):
    header = {}
    body = ""
    for i, line in enumerate(data):
        if not line:
            break
        section, value = line.split(": ")
        header.update({section: value})
    for line in data[i:]:
        if line:
            body = line
            break
    return header, line


def parse_body(data):
    pass


def handle(data):
    print("\nDebug: Getting HTTP protocol information")
    http_method, http_path, http_ver = parse_proto(data[0])
    print("Debug: http method: " + http_method)
    print("Debug: path: " + http_path)
    print("Debug: version: " + http_ver)
    print("Debug: Getting header and request")
    header, body = parse_req(data[1:])
    print("Debug: header")
    print(header)
    print("Debug: body")
    print(body)


def run():
    data_get = open(file_get).read().split("\n")
    data_post = open(file_post).read().split("\n")
    handle(data_get)
    handle(data_post)


if __name__ == "__main__":
    run()
