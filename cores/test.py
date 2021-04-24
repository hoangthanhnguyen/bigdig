# import urllib
#
#
# with open("../resources/sqli_payloads", "r") as f:
#     mylist = f.readlines()
# for i in mylist:
#     i.replace("\n", "")
# mylist = list(dict.fromkeys(mylist))
# mylist1 = mylist.copy()
# mylist2 = []
# for i in mylist1:
#     mylist.append(urllib.parse.quote(i))
#     mylist2.append(urllib.parse.quote(i))
# for i in mylist2:
#     mylist.append(urllib.parse.quote(i))
# for i in mylist:
#     if i == "\n":
#         continue
#     print(i)
# print(len(mylist))