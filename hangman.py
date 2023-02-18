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

def welcome_speech (t):
    print(f'''Добро пожаловать в hangman 2314!
    Загаданное слово состоит из (len(t)) букв [t]
    ''')

def start_template(w):
    t = []
    for f in w:
        t.append
    return t

def list_to_spring_convert(t):
    s = ' '
    return s.join(t)

def get_word(w):
    return w[0]


