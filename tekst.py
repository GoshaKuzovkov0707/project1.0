from collections import Counter

with open("tekst.txt") as file:
    text = file.read()


# list123 = text.split()

# for w in list123:
#     print(w)

list123_list = []
banned = [' ', '.', ',', '!']
list123_word = ''

for w in text:
    w = w.lower()
    if w == '\n':
        if list123_word:
            list123_list.append(list123_word)
            list123_word = ''
    elif w not in banned:
        list123_word += w
    else:
        if list123_word:
            list123_list.append(list123_word)
        list123_word = ''

if list123_word :
    list123_list.append(list123_word)
    list123_word = ''

copies = {}

for w in list123_list:
    w = w.lower()
    if w not in copies:
        copies[w] = 1
    else:
        copies[w] += 1

c = Counter(copies)
print(c.most_common(4))
