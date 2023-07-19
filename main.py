def tempate_opration(_operation):
    if operation == '+':
        return lambda _number1, _number2: f'{_number1} + {_number2} = {_number1 + _number2}'
    if operation == '-':
        return lambda _number1, _number2: f'{_number1} - {_number2} = {_number1 - _number2}'
    if operation == '*':
        return lambda _number1, _number2: f'{_number1} * {_number2} = {_number1 * _number2}'
    if operation == '**':
        return lambda _number1, _number2: f'{_number1}  в степени {_number2} = {_number1 ** _number2}'
    if operation == '/' and number2 == 0:
        print('На ноль делить нельзя')
    else:
        return lambda _number1, _number2: f'{_number1} / {_number2} = {_number1 / _number2}'

operation = input('Введите операцию +,-,*,/, ** возведение в степень \n')
number1 = int(input('Введите первое число\n'))
number2 = int(input('Введите второе число либо степень\n'))

func_calc = tempate_opration(operation)
result = func_calc(number1, number2)
print(result)