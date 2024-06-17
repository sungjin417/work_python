import json

# customer = {
#     "id": 12345,
#     "name": "장원영",
#     "history": [
#     {"date" : "2024-06-07", "product" : "iPhone 14 Pro"},
#     {"date" : "2024-06-18", "product" : "Galaxy S24 Ultra"},
#     ]
# }
#
# json_string = json.dumps(customer)
# print((json_string))

# jsonString = '''{"name" : "KH", "id" : 123456, "history" : [
#     {"date" : "2023-05-10", "item" : "iPhone 14 Pro"},
#     {"date" : "2023-05-24", "item" : "Galuxy S23 Ultra"}
# ]}'''
#
# dict = json.loads(jsonString)
#
# print(dict["name"])
# for h in dict["history"]:
#     print(h["date"], h["item"])

import csv
f = open('output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow([1, "안유진", False])
wr.writerow([2, "장원영", True])
f.close()