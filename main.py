from datetime import date, datetime

import telebot
from aiogram.types import ParseMode
from aiogram.utils.markdown import text, bold, italic, code, pre

bot = telebot.TeleBot('1163794464:AAFygKq8I_5geMng2myONjIRIy60-ePzj30')


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Краткая история обо мне', callback_data='about-me'),
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Социальные сети', callback_data='social'),
        telebot.types.InlineKeyboardButton('Связь со мной', callback_data='contact-with-me')
    )

    bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name + '\n Чтобы ты хотел узнать?\n', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    if query.data == 'about-me':
        bot.answer_callback_query(query.id)
        send_about_me(query)

    if query.data == 'social':
        bot.answer_callback_query(query.id)
        send_social_network(query)

    if query.data == 'contact-with-me':
        bot.answer_callback_query(query.id)
        send_contact_info(query)

def send_about_me(query):
    bot.send_message(query.message.chat.id,
                    '*Турундаев Артур Эдуардович*\n' +
                    '_Программист_\n\n' +
                    '*Дата рождения*: 14 октября 1990 (' + get_diff_full_age(datetime.strptime('14-10-1990', '%d-%m-%Y')) + ')\n' +
                    '*Гражданство*: Российская Федерация\n' +
                    '*Место*: Москва\n' +
                    '*Образование*: Высшее\n' +
                    '*Пол*: мужской\n' +
                    '*Семейное положение*: Женат\n\n' +
                    '*Образование*\n\n' +
                    '*Учебное заведение*: Обнинский институт атомной энергетики (филиал) Национального исследовательского ядерного университета "МИФИ", Обнинск\n' +
                    '*Год окончания*: 2013 (' + get_diff_full_age(datetime.strptime('01-06-2013', '%d-%m-%Y')) + ' назад)\n' +
                    '*Факультет*: Кибернетика\n' +
                    '*Специальность*: Информационные системы и технологии\n' +
                    '*Должность*: студент\n' +
                    '*Форма обучения*: очная\n\n' +
                    '*Учебное заведение*: Обнинский институт атомной энергетики (филиал) Национального исследовательского ядерного университета "МИФИ", Обнинск\n' +
                    '*Год окончания*: 2014 (' + get_diff_full_age(datetime.strptime('01-06-2014', '%d-%m-%Y')) + ' назад)\n' +
                    '*Факультет*: Кибернетика\n' +
                    '*Специальность*: Информационные системы и технологии\n' +
                    '*Должность*: аспирант\n' +
                    '*Форма обучения*: очная\n\n'
            , parse_mode=ParseMode.MARKDOWN)


def get_diff_full_age(date):
       yrs = {'1': 'год', '234': 'года', '567890': 'лет'}
       today = date.today()
       age = today.year - date.year - ((today.month, today.day) < (date.month, date.day))

       yrs_str = next(v for k, v in yrs.items() if str(age % 10) in k)
       if age > 10 and str(age)[-2] == '1': yrs_str = 'лет'

       return str(age) + ' ' + yrs_str


def send_social_network(query):
    bot.send_message(query.message.chat.id,
                     '*Instagram*: instagram.com/arturundaev\n' +
                     '*Facebook*: facebook.com/profile.php?id=100013703143653\n' +
                     '*VK*: vk.com/@turundaev\n' +
                     '*LinkedIn*: linkedin.com/in/arturturundaev'
                     , parse_mode=ParseMode.MARKDOWN)

def send_contact_info(query):
    bot.send_message(query.message.chat.id,
                     '*Телефон*: +7 (925) 730-82-23\n' +
                     '*Телеграм*: @artur\_turundaev\n' +
                     '*Почта*: artur.turundaev@gmail.com\n' +
                     '*Skype*: kiberhetik'
                     , parse_mode=ParseMode.MARKDOWN)

bot.polling()
