import json


# a = {'X-Forwarded-For': '127.0.0.1', 'projectName': 'zhikovapp', 'Authorization':
#         'Bearer HZCdsf='}
# print(type(a))
# if type(a) == dict:
#     print("ok")
# else:
#     print("not ok")
def a(b, c, *d):
    print(b)
    print(c)
    if d:
        print("okie")
    else:
        print("not okie")

x = a(1,2,2)