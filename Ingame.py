# pip install deep-translator, pip install pynput
from deep_translator import GoogleTranslator
from pynput.keyboard import Key, Controller, Listener
keyboard = Controller()

phrase = ""
start_traduction = False

print('Read the documentation : https://ingame.camillerakoto.fr')
print('\nNote : [...] are the default values')
usersTranslationDest = input(
    '\nWhat language should you translate your messages into [en] : ') or 'en'
usersStartingKey = input(
    '\nChoose your starting key. You can find all the keys in the documentation [Key.alt_r] : ') or 'Key.alt_r'
usersKeyboardKeys = {'starting_key': usersStartingKey}
print('\nNow, open your game and enjoy !')


def start(key):
    global phrase, start_traduction, usersKeyboardKeys

    key = str(key).replace("'", "")

    if start_traduction:
        if key == usersKeyboardKeys['starting_key']:
            start_traduction = False
            englishTranslation = translateThePhrase()
            deleteAllTextInTchat()
            enterTheEnglishTranslationOnTchat(englishTranslation)

        else:
            if key == 'Key.space':
                key = ' '
            if key == 'Key.shift_r' or key == 'Key.shift' or key == 'Key.backspace' or key == 'Key.ctrl' or key == 'Key.ctrl_l' or key == 'Key.ctrl_r' or key == 'Key.caps_lock':
                key = ''
            if key == "Key.enter":
                key = '\n'
            phrase += key

    else:
        if key == usersKeyboardKeys['starting_key']:
            start_traduction = True


def translateThePhrase():
    global phrase, usersTranslationDest

    englishTranslation = GoogleTranslator(
        source='auto', target=usersTranslationDest).translate(phrase)
    return englishTranslation


def deleteAllTextInTchat():
    global usersKeyboardKeys, phrase

    for i in range(len(phrase) + 1):
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)

    phrase = ""


def enterTheEnglishTranslationOnTchat(translation):
    for char in translation:
        keyboard.press(char)
        keyboard.release(char)


with Listener(on_press=start) as l:
    l.join()
