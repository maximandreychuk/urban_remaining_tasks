def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    steps = 0

    while steps < len(numbers):
            for i in numbers:
                try:
                    result += i
                    steps += 1
                except TypeError:
                    incorrect_data += 1
                    steps += 1
    return (result, incorrect_data)


def calculate_average(numbers):
    try:
        if not isinstance(numbers, list):
            raise TypeError("В numbers записан некорректный тип данных")
    except TypeError:
        return None
    try:
        result = personal_sum(numbers)[0] / (len(numbers) - personal_sum(numbers)[1])
    except ZeroDivisionError:
        result = 0
    finally:
        return result




test_list = [1,"3", 2, [(3,3)], 2, "2", [1], 2, 4]
test_list_zero = [0, "3", (132,3), 0, [0,0]]
test_no_list = "323"

print("-"*5, "Функция personal_sum", "-"*5)
print(personal_sum(test_list))
print(personal_sum(test_list_zero))

print("-"*5, "Функция calculate_average", "-"*5)
print(calculate_average(test_list))
print(calculate_average(test_no_list))

print(calculate_average(test_list_zero))



