import telebot
from telebot.types import InlineQueryResultArticle

bot = telebot.TeleBot('1163794464:AAFygKq8I_5geMng2myONjIRIy60-ePzj30')


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Краткая история меня', callback_data='about-me'),
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Социальные сети', callback_data='social'),
        telebot.types.InlineKeyboardButton('Связь со мной', callback_data='contact-with-me')
    )

    bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name + '\n Выбери, что бы ты хотел узнать:\n', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    result = list()
    if query.data == 'about-me':
        bot.answer_callback_query(query.id)
        bot.send_message(query.message.chat.id, 'Меня зовут Артур')
      #  query.
     #   bot.answerInlineQuery(query.id, results=result)
   # else:
     #   repeat(query)

#def send_info_about_me(query):
#    return InlineQueryResultArticle(
#        id = 0,
##        title = "Title",
 #       input_message_content = "message_test"
 #   )

bot.polling()
