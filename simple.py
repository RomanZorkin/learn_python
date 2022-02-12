"""Tasks of the first week."""

# exercise 1
a_value = 2
b_value = 0.5
print(a_value + b_value)

# exercise 2
name = 'Roman'
print(f'Привет, {name}!')

# exercise 3
input_value = int(input('Введите число от 1 до 10: '))
new_value = input_value + 10
print(f'Число на десять больше введенного : {new_value}')

# exercise 3
name = input('Введите ваше имя: ').upper()
print(f'Привет, {name}!  Как дела?')

# exercise 4
print(float('1'))
print(int(float('2.5')))
print(bool(1))
print(bool(''))
print(bool(0))

# exercise 4 lists & dicts
simple_list = [3, 5, 7, 9, 10.5]
print(f'содержимое списка {simple_list}')
simple_list.append('Python')
curent_len = len(simple_list)
print(f'длина списка {curent_len}')

# exercise 4 lists & dicts
print(f'начальный элемент списка {simple_list[0]}')
print(f'последний элемент списка {simple_list[curent_len - 1]}')
print(f'элементы списка со второго по четвертый включительно {simple_list[1:4]}')
del_index = simple_list.index('Python')
del simple_list[del_index]
# alternative
# simple_list.remove('Python')

# exercise 5 lists & dicts
simple_dict = {"city": "Москва", "temperature": "20"}
print(simple_dict['city'])
temp_int = int(simple_dict['temperature']) - 5
simple_dict['temperature'] = str(temp_int)
print(simple_dict)
print(simple_dict.get('country', 'Россия'))
simple_dict['date'] = '27.05.2019'
print(len(simple_dict))
print(simple_dict)
