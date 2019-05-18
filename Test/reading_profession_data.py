import re


def read_file():
    lines = []
    with open('/static/ResultsTexts/Lesson_5/professions_final.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if line != '\n':
                lines.append(line.strip().lower())
    return lines


def profession_list(lines):
    professions = []
    profession_pattern = '\d\. ([\w ]*)'
    for line in lines:
        profession = re.findall(profession_pattern, line)
        if len(profession) != 0:
            professions.append(profession[0].lower())
    return professions


def find_slice(lines, current_profession, next_profession):
    first_line = 0
    last_line = 0

    for index, line in enumerate(lines):
        if current_profession in line:
            first_line = index
            break

    for index, line in enumerate(lines):
        if next_profession in line and index > first_line:
            last_line = index
            break

    return lines[first_line + 1:last_line]


def collect_answers(test_slice):
    answers = []
    for line in test_slice:
        if line == 'не учитывается':
            line = "NTUD"
        answers.append(line.lower())
    return answers


def answers_for_one_profession(line_slice, current_profession):
    profession = {}
    for test_number in range(1, 17):
        current_test_index = 0
        next_test_index = 0
        if test_number != 11 and test_number != 12 and test_number != 16:
            current_test = 'тест ' + str(test_number)
            next_test = 'тест ' + str(test_number + 1)
        if test_number == 11 or test_number == 12:
            current_test = 'тест 11 и 12'
            next_test = 'тест 13'
        if test_number == 16:
            current_test = 'тест 16'
        key = "Test" + str(test_number)
        for index, line in enumerate(line_slice):
            if current_test in line:
                current_test_index = index
            if next_test in line:
                next_test_index = index
                break
        if test_number == 16:
            next_test_index = current_test_index + 3
        test_slice = line_slice[current_test_index + 1:next_test_index]

        answers = collect_answers(test_slice)
        profession.update({key: answers})
    profession.update({'profession': current_profession})
    return profession


def collect_all_professions():
    lines = read_file()
    professions = profession_list(lines)
    all_professions = []
    for index in range(len(professions) - 1):
        line_slice = find_slice(lines, professions[index], professions[index + 1])
        _profession_answers = answers_for_one_profession(line_slice, professions[index])
        all_professions.append(_profession_answers)
    return all_professions


def profession_answers(profession):
    prof_answers = []
    for test_number in range(1, 17):
        key = "Test" + str(test_number)
        prof_answers.append(profession.get(key))
    prof_answers.append(profession.get('profession'))
    return prof_answers


def choose_appropriate_professions(user_answers, all_professions):
    appropriate_professions = []
    for profession in all_professions:
        appropriate_answers = profession_answers(profession)
        points = 0
        for test_index, test_answer in enumerate(user_answers):
            try:
                if appropriate_answers[test_index][0] == 'ntud':
                    points += 1
                else:
                    if user_answers[test_index].lower() in '-'.join(appropriate_answers[test_index]):
                        points += 1
                    else:
                        break
            except:
                break

        if points == 16:
            appropriate_professions.append(appropriate_answers[16])

    return appropriate_professions
