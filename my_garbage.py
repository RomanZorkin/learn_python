some_string = '   London is a capital of Grate Britain'
print(some_string)
simple_list = some_string.split()
print(simple_list)

print(some_string.strip())

for word in simple_list:
    print(word.capitalize())
    print(word.upper())
    print(word.lower())

print(bool(2))
print(simple_list.count('London'))
print(simple_list[3:5])
print(simple_list.index('of'))
del simple_list[0]
simple_list.remove('of')
print(simple_list)

product = {
    "name": "iPhone 12",
    "stock": 24,
    "price": 65432.1
}
print(product.get("purt", 12))

from pprint import pprint  # визуально форматирует вывод

phones = ["Samsung Galaxy S21", "iPhone 12"]
product["recomended"] = phones
pprint(product)
{'name': 'iPhone 12 Plus',
 'price': 65432.1,
 'recomended': ['Samsung Galaxy S21', 'iPhone 12'], 'stock': 24}