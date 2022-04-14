# Задан файл с зарплатами администрации Белого дома на 2017 год
# С помощью скриптов на питоне определить:
# 1. Кто зарабатывает меньше всего.                           2. Кто зарабатывает больше всего.
# 3. Средний заработок всех сотрудников.                      4. Какие 10 сотрудников зарабатывают больше всех.
# 5. Сколько людей временно назначены на другую должность?    6. Сколько платят людям из пункта 5?
# 7. Сколько людей в должности "STAFF ASSISTANT"              8. Среднюю зарплату всех "STAFF ASSISTANT"
# 9. Есть ли люди, которым не платят зарплату вообще?
# Взяв за образец задачу по Белому дому модифицировать ее так, чтобы скрипт читал первую строчку файла
# (где перечислены поля данных: ФИО, статус, и т.д.), делал из нее словарь и по нему последовательно запрашивал
# пользователя информацию о новом сотруднике
# (в формате: "NAME?", ...), а потом добавлял эту информацию в исходный файл.

while True:
    whouse_file = open('white_house_2017_salaries_com.csv', 'r', encoding='utf-8')
    wh_file = whouse_file.readlines()
    whouse_file.close()

    wh_workers = []
    wh_file_header = wh_file[0].split(';')
    wh_file_header = [item.replace('\xa0', ' ').strip() for item in wh_file_header]

    for line in wh_file[1:]:
        line_parsed = line.split(';')
        person_dict = {}
        for index, mean in enumerate(wh_file_header):
            if mean == 'SALARY':
                person_dict[mean] = float(line_parsed[index].replace('$', '').replace(',', ''))
            else:
                person_dict[mean] = line_parsed[index].strip()
        wh_workers.append(person_dict)
    user_choise = input("\n\n\n\t\tW H I T E   H O U S E  D A T A B A S E \n"
                        "What would you like to do? Please enter the number in folowing menu: \n"
                        "1 - Кто из сотрудников зарабатывает больше всего?\n"
                        "2 - Кто из сотрудников зарабатывает меньше всего?\n"
                        "3 - Средний заработок всех сотрудников?\n"
                        "4 - Какие 10 сотрудников зарабатывают больше всех?\n"
                        "5 - Сколько людей временно назначены на другую должность?\n"
                        "6 - Сколько платят людям из пункта 5?\n"
                        "7 - Сколько людей в должности STAFF ASSISTANT?\n"
                        "8 - Средняя зарплата всех STAFF ASSISTANT?\n"
                        "9 - Есть ли люди, которым не платят зарплату вообще?\n"
                        "10 - Внести в базу данных нового работника\n"
                        "\tНажмите любую клавишу для выхода из программы\n")
    # 1. Кто зарабатывает больше всего.
    if user_choise == "1":
        max_salary = 0
        for item in wh_workers:
            if item['SALARY'] > max_salary:
                max_salary = item['SALARY']
        # How many people and who earn max salary
        whogetmax = [item['NAME'] for item in wh_workers if max_salary == item['SALARY']]
        print(f'\nPeople get max salary ${max_salary} are:')
        for item in whogetmax:
            print('\t' * 9, f'{item}')
        input("Push enter to continue.")
    # 2. Кто зарабатывает меньше всего.
    elif user_choise == "2":
        min_salary = 180000
        for item in wh_workers:
            if 0 < item['SALARY'] < min_salary:
                min_salary = item['SALARY']
        # How many people and who earn min salary
        whogetmin = [item['NAME'] for item in wh_workers if min_salary == item['SALARY']]
        print(f'\nPeople get min salary ${min_salary} are:')
        for item in whogetmin:
            print('\t' * 9, f'{item}')
        input("Push enter to continue.")

    # 3. Средний заработок всех сотрудников.
    elif user_choise == "3":
        av_salary = sum([item['SALARY'] for item in wh_workers]) / len([item['SALARY'] for item in wh_workers])
        print(f"\n\nThe average salary for all co-workers is: ${av_salary}")
        input("Push enter to continue.")

    #4. Какие 10 сотрудников зарабатывают больше всех.
    elif user_choise == "4":
        sorted_salary = sorted(wh_workers, key=lambda x: x['SALARY'], reverse=True)
        print("\n\nThese are 10 the most paid emloyees:")
        for item in sorted_salary[0:10]:
            print(f"{item['NAME']} earns: ${item['SALARY']}")
        input("Push enter to continue.")

    # 5. Сколько людей временно назначены на другую должность?
    elif user_choise == "5":
        temp_posit = [(item['NAME'], item['SALARY']) for item in wh_workers if item['STATUS'] == 'Detailee']
        print(f"\nThe quantity of people who have Detailee status : {len(temp_posit)}")
        input("Push enter to continue.")

    # 6. Сколько платят людям из пункта 5?
    elif user_choise == "6":
        temp_posit = [(item['NAME'], item['SALARY']) for item in wh_workers if item['STATUS'] == 'Detailee']
        print('These people are:')
        for item in temp_posit:
            print(f"{item[0]} earns {item[1]}")
        input("Push enter to continue.")

    # 7. Сколько людей в должности "STAFF ASSISTANT"
    elif user_choise == "7":
        staf_assis = [item['SALARY'] for item in wh_workers if item['POSITION TITLE'] == 'STAFF ASSISTANT']
        print(f"\n\nThe quantity of people who in STAFF ASSISTANT position: {len(staf_assis)}")
        input("Push enter to continue.")

    # 8. Среднюю зарплату всех "STAFF ASSISTANT"
    elif user_choise == "8":
        staf_assis = [item['SALARY'] for item in wh_workers if item['POSITION TITLE'] == 'STAFF ASSISTANT']
        print(
            f"\nThe average salary for people in STAFF ASSISTANT position is: ${sum(staf_assis) / len(staf_assis):.2f}")
        input("Push enter to continue.")

    # 9. Есть ли люди, которым не платят зарплату вообще?
    elif user_choise == "9":
        nopaid_people = [item['NAME'] for item in wh_workers if item['SALARY'] == 0]
        print("\nPeople who work for free (doesn't get salary for their job) are:")
        for item in nopaid_people:
            print(item)
        input("Push enter to continue.")
    #10 Внести в базу нового работника
    elif user_choise == "10":
        new_worker = ""
        for item in wh_file_header:
            new_worker += input(f"Enter the {item}: ") + '; '
        new_worker = new_worker[0:-2]+'\n'
        print(new_worker)
        with open('white_house_2017_salaries_com.csv','a') as wh:
            wh.write(new_worker)
    else:
        quit()





