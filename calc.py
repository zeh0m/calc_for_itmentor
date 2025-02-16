

def calc(input_str: str):

    parts = input_str.split() # разбиваем принятые данные на элементы

    if len(parts) != 3: # проверяем верное кол-во элементов
        raise Exception("Ошибка: неверное количество элементов.")

    try:
        a = int(parts[0]) # проверяем целое ли число
        b = int(parts[2]) # проверяем целое ли число
    except ValueError:
        raise Exception("Ошибка: числа должны быть целыми от 1 до 10.")

    if not (1 <= a <= 10 and 1 <= b <= 10): # задаем ограничения
        raise Exception("Ошибка: числа должны быть целыми от 1 до 10.")

    operator = parts[1] # переменная оператора

    if operator == '+': # определяем операцию
        return str(a + b)
    elif operator == '-':
        return str(a - b)
    elif operator == '*':
        return str(a * b)
    elif operator == '/':

        return str(a // b)
    else:
        raise Exception("Ошибка: недопустимый оператор.")

try: # обработка исключения
    result = calc(input("Введите выражение: "))
    print("Результат:", result)
except Exception as error:
    print(error)
