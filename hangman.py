def game():
    word = ['turtle']
    lifes = 5
    progress = True


    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcome_speech(list_to_spring_convert(template))

    while progress:
        user_guess = input('Введите букву - ')
        template = build_template(template, word_in_play, user_guess)
        guessed = list_to_spring_convert(template)
        print(f'Результат {guessed}')
        progress = check_win(guessed)

        if not check_mistake(word_in_play, user_guess):
            lifes -= 1 
            print(f'У вас осталось {lifes} жизней')

        if lifes == 0:
            print('Вы проиграли!')
            break

        if not progress:
            print('!!!Вы победили!!!')

def check_win(g):
    if '_' in g:
        return True
    return False

def welcome_speech (t):
    print(f'''Добро пожаловать в hangman 1.0!
    Загаданное слово состоит из {len(t)} букв {t}
    ''')

def start_template(w):
    t = []
    for f in w:
        t.append('_')
    return t

def list_to_spring_convert(t):
    s = ''
    return s.join(t)

def get_word(w):
    return w[0]

def build_template(t, w, g=''):
    for a in range(len(w)):
        if t[a] == '_':
            if w[a] == g:
                t[a] = w[a]
            else:
                t[a] = '_'
    return t

def check_mistake(w, g):
    if g not in w:
        return False
    return True

game()
