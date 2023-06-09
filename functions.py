import json

# data - список словарей
# pk - номер студента
# title - специальность

'''Загружает список студентов из файла students.json'''
def load_students(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


'''Загружает список профессий из файла professions.json'''
def load_professions(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


'''Получает словарь с данными студента по его pk'''
def get_student_by_pk(pk, data):
    for item in data:
        if pk == item['pk']:
           return item


'''Получает словарь с инфо о профе по названию'''
def get_profession_by_title(title, data):
    for item in data:
        if title == item['title']:
           return item


'''Получив студента и профессию возвращает словарь'''
'''{
  "has": ["Python", "Linux"],
  "lacks": ["Docker, SQL"],
  "fit_percent": 50
}'''
def check_fitness(student, professions):
    set_students = set(student['skills'])  #во множество, чтобы не было повторов
    set_professions = set(professions['skills'])

    has_skills = set_students.intersection(set_professions) #какие skills повторяются в списках (вернет словарь)
    lacks_skills = set_professions.difference(set_students) #каких skills не хватает set_students (вернет словарь)
    fit_percent = round(len(has_skills)/len(lacks_skills) * 100)  # в процентах

    dict_result = {
         'has': has_skills,
         'lacks': lacks_skills,
         'fit_percent': fit_percent,}

    return dict_result

'''Вывод статистики'''
'''Программа: Пригодность 50%
Программа: Jane Snake знает Python, Linux
Программа: Jane Snake не знает Docker, SQL'''

def show_result(data, name):
    str_has = ', '.join(data['has'])  #в строку из словаря data по ключу "has"
    str_lacks = ', '.join(data['lacks'])  #в строку из словаря data по ключу "lacks"
    str_output = f'Пригодность {data["fit_percent"]} \n' \
                 f'{name} знает {str_has} \n' \
                 f'{name} не знает {str_lacks} \n'

    return str_output










