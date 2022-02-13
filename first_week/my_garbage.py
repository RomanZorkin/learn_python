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

price = 100
discount = 5

price_with_discount = price - price * discount / 100

print(price_with_discount)


def discounted(price, discount, max_discount=20):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)


discounted(price, discount)

price1 = 100
discount1 = 10
discounted(price1, discount1)

discounted(200, 5)
discounted(100, 101)
print(discounted(-100, 101))

product = {'name': 'Samsung Galaxy S21', 'price': 50000.0, 'discount': 5}
product['price_discounted'] = discounted(product['price'], product['discount'])
print(product)

print(discounted(100, 50))
print(discounted(100, 50, max_discount=60))