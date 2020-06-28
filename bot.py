import telebot, config, datetime,pyautogui
from io import BytesIO
from telebot import types
from PIL import ImageTk, ImageGrab

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcom(message):
    #ketboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_send_dekstop = types.KeyboardButton("Скриншот рабочего стола")
    item_send_nudes = types.KeyboardButton("Nudes")
    markup.add(item_send_dekstop,item_send_nudes)

    bot.send_message(message.chat.id, "Хай {0.first_name}!".format(message.from_user,
    bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.chat.type == 'private':
        if message.text == 'Скриншот рабочего стола':
            bio = BytesIO()
            bio.name = 'image.jpeg'
            pyautogui.screenshot().save(bio,'JPEG')
            bio.seek(0)
            bot.send_photo(message.chat.id, bio)
            bot.send_message(message.chat.id,
                'kek ' + datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))

        elif message.text == 'Nudes':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item_young = types.InlineKeyboardButton('Young', callback_data='young')
            item_mature = types.InlineKeyboardButton('Mature', callback_data='mature')

            markup.add(item_young,item_mature)

            bot.send_message(message.chat.id, 'So sad', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Nope')


@bot.callback_query_handler(func = lambda call: True)
def callback_inline(call):
    try:
        if call.data == 'young':
            bot.send_message(call.message.chat.id, 'Молодых нет')
        elif call.data == 'mature':
            bot.send_message(call.message.chat.id, 'Зрелых нет')
        #remove inline bottons
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
        text="Nudes",reply_markup=None)

    except Exception as e:
        print(repr(e))
#run

bot.polling(none_stop=True)
