def custom_write(file_name: str, strings: list) -> dict[tuple, str]:

    strings_positions ={}
    f = open(file_name, 'w', encoding='utf-8')
    for index, string in enumerate(strings):
        position = f.tell()
        f.write(string + 'n')
        strings_positions[(index + 1, position)] = string
    f.close()

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

print(custom_write("1", strings=info))
