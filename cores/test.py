import json


a = {'X-Forwarded-For': '127.0.0.1', 'projectName': 'zhikovapp', 'Authorization':
        'Bearer HZCdsf='}
print(type(a))
if type(a) == dict:
    print("ok")
else:
    print("not ok")