def custom_write(file_name, strings):
    file_name = open('custom_write.txt', 'w', encoding = 'utf-8')
    strings_positions = {}

    for i, string in enumerate(strings, 1):
        strings_positions[(i, file_name.tell())] = string
        file_name.write(string + '\n')

    return strings_positions



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('custom_write.txt', info)
for elem in result.items():
  print(elem)
