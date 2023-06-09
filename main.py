from functions import load_students, load_professions, get_student_by_pk, get_profession_by_title, check_fitness, show_result
#импорт всех функций в файле from functions import *

'''Обозначаем файлы students и professions в качестве переменных'''
file_students = 'students.json'
file_professions = 'professions.json'

#Тестируем работу функций load_students и load_professions (должны получиться списки словарей)
#print(load_students(file_students))
#print(load_professions(file_professions))

data_students = load_students(file_students)
data_professions = load_professions(file_professions)

#Тестируем работу функций get_student_by_pk и get_profession_by_title (получатся словари)
pk = int(input('Введите номер студента: '))
#print(get_student_by_pk(pk, data_students))
student = get_student_by_pk(pk, data_students)

'''Если такой студент есть – выведите информацию о пользователе, если нет - завершение программы'''
if student:
    print(f'Студент {student["full_name"]}')
    str_skills = ', '.join(student['skills']) #в строку через запятую и пробел
    print(f'Знает {str_skills}')
else:
    print(f'Нет такого студента')
    quit()   #завершение программы


title = input('Выберите специальность для оценки студента: ')
#print(get_profession_by_title(title, data_professions))
profession = get_profession_by_title(title, data_professions)

'''Если профессия есть – проверяем пригодность студента get_profession_by_title, если нет - завершение программы'''
if not profession:
    print(f'Нет такой специальности')
    quit()

data = check_fitness(student, profession)
#name = student['full_name']

print(show_result(data, student['full_name']))
