import os
import re
import sys

# Список погодных условий и соответствующих им названий
weather_conditions = [
    'blizzard', 'clear', 'clearing', 'clouds', 
    'extrasunny', 'foggy', 'halloween', 'neutral', 'overcast', 'rain', 'smog',
    'snow', 'snowlight', 'thunder', 'xmas'
]

# Функция для замены значения атрибута name в теге cycle
def replace_name_tag(content, new_name):
    # Используем регулярное выражение для замены значения name в теге cycle
    new_content = re.sub(r'(<cycle name=")(.*?)(")', f'\\1{new_name.upper()}\\3', content)
    return new_content

# Проверка, был ли файл перетащен на скрипт
if len(sys.argv) > 1:
    # Получение пути к файлу из аргументов командной строки
    base_file = sys.argv[1]
    
    # Проверка существования файла и его расширения
    if os.path.exists(base_file) and base_file.endswith('.xml'):
        try:
            # Чтение содержимого базового XML-файла
            with open(base_file, 'r', encoding='utf-8') as file:
                base_content = file.read()
            
            # Проходим по списку погодных условий и создаем соответствующие XML-файлы
            for weather in weather_conditions:
                new_file = f'w_{weather}.xml'
                # Изменяем содержимое базового файла под нужное погодное условие
                new_content = replace_name_tag(base_content, weather)
                
                # Записываем измененное содержимое в новый XML-файл
                with open(new_file, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f'Сгенерирован: {new_file}')
        except Exception as e:
            print(f'Ошибка при работе с файлом {base_file}: {e}')
    else:
        print('Файл не найден или не является XML. Пожалуйста, перенесите правильный файл.')
else:
    print('Пожалуйста, перетащите файл w_extrasunny.xml на скрипт.')
