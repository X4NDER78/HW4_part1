#HW4 part 1

exceptions_vowels = ('e', 'y', 'u', 'o', 'a', 'е', 'а', 'о', 'э', 'я', 'и', 'у', 'ы', 'ё', 'ю')
string = input('Введите слова ->').split(' ')

for element in exceptions_vowels:
    counter = 0
    while not counter > len(string) - 1:
        if string[counter].find(element) != -1:
            try:
                string[counter] = string.replace(element, 'i')
            except Exception as error_list:
                print(f'Я сломался , когда пытался заменить {element} на i в слове {string[counter]}')
                print(error_list)
                counter += 1
            continue
        else:
            counter += 1

counter_i = 0

for word in string:
    counter_i = counter_i + 1 if word.find('ii') != -1 else counter

print(counter_i)




