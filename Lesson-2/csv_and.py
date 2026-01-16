import csv
with open('data.csv', 'r', encoding='utf-8') as file:
   reader = csv.reader(file)
   for row in reader:
       print(row)
# ['Name', 'Age', 'City']
# ['Alice', '30', 'New York']
# ['Bob', '25', 'Los Angeles']
# ['Charlie', '35', 'Chicago']

data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]
with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

import json
with open('example.json', mode='r', encoding='utf-8') as file:
    data = json.load(fp=file)
print("type(data): ",type(data))
# <class 'dict'>
print("data: ", data)
# {'catalogs': [{'conditions': 'Действительно для Москвы', 'date': '2020-06-12', 'id': 1234, 'is_main': True, 'offers': ['11111', '22222', '33333']}, {'conditions': 'Предложения действительны в магазине по адресу: Владимир, улица Куйбышева, 26К', 'date': '2020-06-12', 'id': 5678, 'is_main': True, 'offers': ['22222', '33333']}], 'offers': [{'barcode': '7501031311309', 'date': '2020-06-10', 'discount_label': '1+1', 'id': 11111, 'price_is_from': False, 'price_new': 50}, {'barcode': '3113097501031', 'id': 22222, 'price_is_from': False, 'price_new': 70}, {'barcode': '1097501031133', 'id': 33333, 'price_is_from': True, 'price_new': 10}], 'version': 2}

import json

data = {
    "Name": "Bob",
    "Age": 30,
    "Skills": ["Python", "Data Analysis"]
}
with open('example_out.json', mode='w', encoding='utf-8') as file:
    json.dump(
        obj=data,
        fp=file,
        indent=4
    )

import json

data = {
    "Name": "John",
    "Age": 30,
    "Skills": ["Python", "Data Analysis"]
}

json_string = json.dumps(data, indent=4)
print("type(json_string): ", type(json_string))
print("json_string: ", json_string)
# {
#     "Name": "Alice",
#     "Age": 30,
#     "Skills": [
#         "Python",
#         "Data Analysis"
#     ]
# }

print("json_string_data: ", type(json.loads(json_string)))
print("json_string_data: ", json.loads(json_string))