<<<<<<< HEAD
#pip install deep-translator, pip install pynput, pip install pyautogui
from deep_translator import GoogleTranslator
from pynput.keyboard import Key, Controller, Listener
from pyautogui import typewrite
=======
#pip install deep-translator, pip install pynput
from deep_translator import GoogleTranslator
from pynput.keyboard import Key, Controller, Listener
>>>>>>> 3ff60dc (v4)
keyboard = Controller()

phrase = ""
start_traduction = False

<<<<<<< HEAD
def userInputWithDefaultValue(question, default_value):
    print(question)
    typewrite(default_value)
    usersValue = input()
    return usersValue

"""
starting_key : Don't touch to the 'Key'. Only change the alt_gr value with your key.
select_all_the_written_message : you can change ctrl to cmd (if you are on MacOS) for example, or the a key with another letter
"""
usersTranslationDest = userInputWithDefaultValue('What language should you translate your messages into : ', 'en')
usersStartingKey = userInputWithDefaultValue('Choose your stating key : ', 'Key<qlt8gr')
usersSelectTheWrittenMessageKey = userInputWithDefaultValue('Choose your key combination to select your entire message in the chat : ', 'ctrl+q')
usersKeyboardKeys = {'starting_key': usersStartingKey, 'select_all_the_written_message': usersSelectTheWrittenMessageKey }
=======
print('Read the documentation : https://ingame.camillerakoto.fr')
print('\nNote : [...] are the default values')
usersTranslationDest = input('\nWhat language should you translate your messages into [en] : ') or 'en'
usersStartingKey = input('\nChoose your starting key [Key.alt_r] : ') or 'Key.alt_r'
usersSelectTheWrittenMessageKey = input('\nChoose your key combination to select your entire message in the chat [ctrl+a] : ') or 'ctrl+a'
usersKeyboardKeys = {'starting_key': usersStartingKey, 'select_all_the_written_message': usersSelectTheWrittenMessageKey }
print('\nNow, open your game and enjoy !')
>>>>>>> 3ff60dc (v4)

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
            if key == 'Key.shift_r' or key == 'Key.shift' or key == 'Key.backspace' or key == 'Key.ctrl' or key == 'Key.caps_lock':
                key = ''
            if key == "Key.enter":
                key = '\n'
            phrase += key

    else:
        if key == usersKeyboardKeys['starting_key']: 
            start_traduction = True 

def translateThePhrase():
    global phrase, usersTranslationDest

    englishTranslation = GoogleTranslator(source='auto', target=usersTranslationDest).translate(phrase)
    phrase = ""
    return englishTranslation

def deleteAllTextInTchat():
    global usersKeyboardKeys

    letterKeyAfterCtrlOrCmd = usersKeyboardKeys['select_all_the_written_message'].partition('+')[2]

    if 'ctrl' in usersKeyboardKeys['select_all_the_written_message']:

        keyboard.press(Key.ctrl.value)
        keyboard.press(letterKeyAfterCtrlOrCmd)
        keyboard.release(letterKeyAfterCtrlOrCmd)
        keyboard.release(Key.ctrl.value)

    elif 'cmd' in usersKeyboardKeys['select_all_the_written_message']:

        keyboard.press(Key.cmd.value)
        keyboard.press(letterKeyAfterCtrlOrCmd)
        keyboard.release(letterKeyAfterCtrlOrCmd)
        keyboard.release(Key.cmd.value)
    
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)

def enterTheEnglishTranslationOnTchat(translation):
    for char in translation:
        keyboard.press(char)
        keyboard.release(char)

with Listener(on_press=start) as l:
<<<<<<< HEAD
    l.join()
=======
    l.join()
>>>>>>> 3ff60dc (v4)
