import config
import telebot
import pickle
import datetime

bot = telebot.TeleBot(config.token)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('/start', 'Hi!', 'Bye!')

help_keyboard = telebot.types.ReplyKeyboardMarkup(True)
help_keyboard.row('I can not see a command keyboard.', 'Other...')

@bot.message_handler(commands=['start'])
def start_command(message):
        try:
            bot.send_message(message.chat.id, 'I am ready to start!!!', reply_markup=keyboard1)
        except OSError:
            bot.send_message(message.chat.id, 'I am ready to start!!!', reply_markup=keyboard1)

@bot.message_handler(commands=['help'])
def help_command(message):
    try:
        bot.send_message(message.chat.id, 'What questions do you have?', reply_markup=help_keyboard)
    except OSError:
        bot.send_message(message.chat.id, 'What questions do you have?', reply_markup=help_keyboard)

@bot.message_handler(content_types=["text"])
def anwser_message(message):
    if message.text == 'Hi!':
        try:
            bot.send_message(message.chat.id, 'Hello!')
        except OSError:
            bot.send_message(message.chat.id, 'Hello!')
    elif message.text == 'Bye!':
        try:
            bot.send_message(message.chat.id, 'Bye, Bye!')
        except OSError:
            bot.send_message(message.chat.id, 'Bye, Bye!')
    elif message.text == 'I can not see a command keyboard.':
        try:
            bot.send_message(message.chat.id, """Try to write /start again. If that will not help, reset the  bot. To reset the bot, press bot's name, scroll down to Stop Bot, press
Stop Bot, Press Restart Bot""", reply_markup=keyboard1)
        except OSError:
            bot.send_message(message.chat.id, """Try to write /start again. If that will not help, reset the  bot. To reset the bot, press bot's name, scroll down to Stop Bot, press
Stop Bot, Press Restart Bot""", reply_markup=keyboard1)
    elif message.text == 'Other...':
        try:
            bot.send_message(message.chat.id, """Try to write /start again. If that will not help, reset the  bot. To reset the bot, press bot's name, scroll down to Stop Bot, press
Stop Bot, Press Restart Bot""", reply_markup=keyboard1)
        except OSError:
            bot.send_message(message.chat.id, """Try to write /start again. If that will not help, reset the  bot. To reset the bot, press bot's name, scroll down to Stop Bot, press
Stop Bot, Press Restart Bot""", reply_markup=keyboard1)
    else:
        try:
            bot.send_message(message.chat.id, 'Your message was to smart for me. Try sending some of messages from the command keyboard.')
        except OSError:
            bot.send_message(message.chat.id, 'Your message was to smart for me. Try sending some of messages from the command keyboard.')
    username = str(message.from_user.username)
    file = open('messages.txt', 'a')
    file.write(username)
    file.write(', ')
    file.write(message.text)
    file.write(', ')
    now = str(datetime.datetime.now())
    file.write(now)
    file.write('''
''')
    file.close()

bot.polling()