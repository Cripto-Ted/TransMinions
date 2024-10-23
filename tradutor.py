import difflib
version = "1.0"
words_given = {
    'привет': 'bello', 
    'спасибо': 'Tank yu', 
    'прости': 'Bi-do', 
    'мы можем начать': 'Pwede na?', 
    'для тебя': 'Para tu',
    'как ты смеешь': 'Sa la ka', 
    'я ненавижу тебя': 'Tatata bala tu',
    'клянусь!': 'Underwear!', 
    'я голоден.': 'Me want banana.',
    'посмотри на себя': 'Luk at tu', 
    'мы тебя любим': 'Tulaliloo ti amo',
    'пока': 'Poopaye',
}

while True:
    print("Добро пожаловать в бот для перевода слов с русского на язык BANANA!")
    print("Количество слов будет увеличиваться по мере времени.")
    print("1. Переводчик")
    print("2. Выход")
    print("3. О проекте")

    chose = int(input('Введите число для выбора: '))
    except ValueError:
        print('Некорректный ввод. Пожалуйста, введите число 1, 2 или 3.')
        continue
    if chose == 1:
        chose_1 = input('Введите слово для перевода: ').lower().strip()
        print('Вы ввели: ', chose_1)
        if chose_1 in words_given:
            print('Перевод: ', words_given[chose_1])
        else:
            # Поиск похожего слова
            closest_matches = difflib.get_close_matches(chose_1, words_given.keys(), n=1, cutoff=0.6)

            if closest_matches:
                print(f'Возможно, вы имели в виду: {closest_matches[0]}? Перевод: {words_given[closest_matches[0]]}')
            else:
                print('Слово не найдено')
    elif chose == 2:
        print("Выход...")
        break
    elif chose == 3:
        print("Автор: Марк Павлов\n\n")
        print("О проекте:\nЭтот проект представляет собой переводчик с русского языка на язык BANANA. Он позволяет пользователям вводить русские слова и получать их забавные переводы на язык BANANA. Программа включает в себя возможность предлагать похожие слова, если введенное слово не найдено в словаре, и постепенно будут добавлятся новые слова. Исли жи вы сами хотите добавить слова проросто напишите мне в телеграмм или дискорд\n")
        print("Связи с автором:\nTelegram: @HubKodLand_bot\nDiscord: @tedking007_23317")
        print("Версия проекта: ",version)
    else:
        print('Некорректный выбор, попробуйте снова.')
