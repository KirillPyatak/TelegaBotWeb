import telebot
from telebot import types


TOKEN = '5877590294:AAHP1lANVCByyY7HGXwvCEoXA3DH6YowYRg'
CHAT_ID = '-100691258066'

bot = telebot.TeleBot(TOKEN)


def webAppKeyboard(): #создание клавиатуры с webapp кнопкой
    startbutton = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    openweb = types.WebAppInfo('https://codepen.io/kpyatak/full/yLxmdzv')
    startbutton1 = types.KeyboardButton(text='открыть веб страницу', web_app=openweb)
    startbutton.add(startbutton1)

    return startbutton #возвращаем клаву
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я бот для проверки телеграмм webapps!)', reply_markup=webAppKeyboard())


# Запуск бота
bot.polling(none_stop=True)