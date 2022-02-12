"""Tasks of the first week."""

# exercise 1
print('Привет мир!')

# exercise 2
print('Привет программист!')
x_value = 2
y_value = 2
answer = x_value + y_value
print(f'Результат действия {x_value} + {y_value} = {answer}')
divisible = 10
divisor = 3
answer = divisible / divisor
print(f'Результат действия {divisible} / {divisor} = {answer}')

# exercise 3
name = 'Roman'
print(name)
magic_method_format = '{0!s} {0!r}'.format(name)
print(magic_method_format)
shift_format = '{0:10} {1:_<10} {2:_>10} {3:_^10}'.format(
    name, name, name, name,
)
print(shift_format)
