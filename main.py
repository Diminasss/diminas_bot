import telebot
import requests
import json
import time
import multiprocessing
from random import randint
from unicodedata import normalize
from functools import lru_cache
from os import listdir
from dotenv import load_dotenv
from os import getenv
from VkBot import *
from Textes import *

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


# ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾#
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ #
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠫⠬⠽⢞⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ #
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣳⣋⡩⠍⢉⣎⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ #
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡕⠂⠂⠒⠐⠀⠂⢎⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ #
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⠄⣉⡋⠩⠠⠄⠥⠌⣑⢊⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿ #
# ⣿⣿⣿⣿⣿⣿⣿⣿⢫⣘⡵⠶⠛⠝⠫⠕⡰⠷⢶⣯⠃⣻⣿⣿⣿⣿⣿⣿⣿⣿ #
# ⣿⣿⣿⣿⣿⣿⡿⣱⣝⣯⠭⠄⠴⠂⠖⠺⠢⣦⢡⢙⣹⢷⡹⣿⣿⣿⣿⣿⣿⣿ #
# ⣿⣿⣿⣿⣿⣟⣕⡿⠏⣂⣡⣤⠴⠶⣶⣶⣤⣔⡣⢙⢮⠟⣷⡽⣿⣿⣿⣿⣿⣿ #
# ⣿⣿⣿⣿⢏⡞⣡⣼⢿⢇⢣⢿⢄⣨⣿⢟⣿⠇⡎⣷⣕⠳⡺⣟⡙⣿⣿⣿⣿⣿ #
# ⣿⣿⣿⠣⣆⣑⡍⠙⠳⠎⠄⠛⠶⠦⠶⠟⢋⠎⢔⡫⡵⣮⠮⡓⠶⣾⣿⣿⣿⣿ #
# ⣿⡿⣱⣑⣔⣃⠀⠅⠀⢀⠠⠒⠒⠢⠒⠒⢂⣉⠢⠭⢉⣒⡮⣉⠽⠬⡟⣿⣿⣿ #
# ⡟⡸⢖⡚⢲⡎⠨⠁⠀⡐⠖⠒⢒⠒⠒⠒⠂⠠⠩⠍⠠⢜⢒⡲⢝⣺⠭⡼⢿⣿ #
# ⣾⣷⣷⣾⣶⣾⣶⣷⣿⣶⣷⣶⣶⣷⣷⣶⣾⣶⣷⣾⣶⣶⣶⣶⣶⣶⣶⣷⣾⣿ #
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ #
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ #
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _#

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# хитрые переменные Влада Л
limit = 1
mass = listdir(path='meme')

joke_voc = {}
jasons_voc = {}
jason_sub_set = set()

load_dotenv()
bot = telebot.TeleBot(getenv("TELEGRAM_TOKEN"))


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def set_changer(operation_type, user_id):
    global jason_sub_set
    if operation_type == 1:
        jason_sub_set.add(user_id)
    elif operation_type == 0:
        jason_sub_set.remove(user_id)


# функция содержащая бота тг поностью для параллельного исполнения с функцией бота ВК


def tgbot() -> None:
    global limit
    global mass

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    # Заготовки влада для мемов
    for i in mass:
        point = i.find('.')
        limit = max(limit, int(i[:point]))
        limit += 1

    # Конец заготовок

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    # Функция нормализации строки, чтобы не учитывать регистр потом Дима
    def word(wordd: str) -> str:
        f = normalize("NFKD", wordd.casefold())
        return f

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    # Сокращение для ускорения печати кода для отправки сообщения Дима !ВАЖНО!
    def mes(inmessage, outmessage):
        return bot.send_message(inmessage.chat.id, str(outmessage))

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    @lru_cache(None)
    # команда старт
    @bot.message_handler(commands=['start'])
    def starterpack(message):
        # создание кнопки сделать заказ
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton("Заказать себе бота")
        markup.add(item1)
        bot.send_message(message.chat.id, text=f"Напиши мне привет, чтобы поздороваться со мной.", reply_markup=markup)
        # отправка сообщения с кнопкой
        printinformation(message, "!запуск бота!")

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    # Функция с цитатами
    @bot.message_handler(commands=['jasons_wisdom'])
    def jason_statham(message):
        jasons_voc[message.chat.id] = 0

        markup_inline = telebot.types.InlineKeyboardMarkup()
        item_previous = telebot.types.InlineKeyboardButton(text="<", callback_data="Previous")
        item_next = telebot.types.InlineKeyboardButton(text=">", callback_data="Next")
        item_random = telebot.types.InlineKeyboardButton(text="🇷", callback_data="Random wisdom")
        if message.chat.id not in jason_sub_set:
            item_jason_subscribe = telebot.types.InlineKeyboardButton(
                text="Подписаться на получение мудростей", callback_data="Jason Subscribe")
        else:
            item_jason_subscribe = telebot.types.InlineKeyboardButton(
                text="Отписаться от получения мудростей", callback_data="Jason Unsubscribe")
        markup_inline.add(item_previous, item_random, item_next)
        markup_inline.add(item_jason_subscribe)

        bot.send_message(message.chat.id, text=str(1) + "/" + str(
            len(jasons_wisdoms)) + "\n\n" + f"<b><i>{jasons_wisdoms[jasons_voc[message.chat.id]]}</i></b>" + "\n\n"
                                               + cjason_statham, reply_markup=markup_inline, parse_mode="HTML")
        printinformation(message, "!Вызвано окошко цитат Стетхема!")

    # ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓

    @bot.callback_query_handler(func=lambda call: True)
    def callback_jason(call):

        max_jason = len(jasons_wisdoms) - 1
        markup_inline = telebot.types.InlineKeyboardMarkup()

        item_previous = telebot.types.InlineKeyboardButton(text="<", callback_data="Previous")
        item_next = telebot.types.InlineKeyboardButton(text=">", callback_data="Next")
        item_random = telebot.types.InlineKeyboardButton(text="🇷", callback_data="Random wisdom")
        if call.message.chat.id not in jason_sub_set:
            item_jason_subscribe = telebot.types.InlineKeyboardButton(
                text="Подписаться на получение мудростей", callback_data="Jason Subscribe")
        else:
            item_jason_subscribe = telebot.types.InlineKeyboardButton(
                text="Отписаться от получения мудростей", callback_data="Jason Unsubscribe")
        markup_inline.add(item_previous, item_random, item_next)
        markup_inline.add(item_jason_subscribe)

        if call.data == "Previous" and jasons_voc[call.message.chat.id] > 0:
            jasons_voc[call.message.chat.id] -= 1
            bot.edit_message_text(str(jasons_voc[call.message.chat.id] + 1) + "/" + str(
                len(jasons_wisdoms)) + "\n\n" + f"<b><i>{jasons_wisdoms[jasons_voc[call.message.chat.id]]}</i></b>"
                                  + "\n\n" + cjason_statham, call.message.chat.id, call.message.message_id,
                                  reply_markup=markup_inline, parse_mode="HTML")
        elif call.data == "Next" and jasons_voc[call.message.chat.id] < max_jason:
            jasons_voc[call.message.chat.id] += 1
            bot.edit_message_text(str(jasons_voc[call.message.chat.id] + 1) + "/" + str(
                len(jasons_wisdoms)) + "\n\n" + f"<b><i>{jasons_wisdoms[jasons_voc[call.message.chat.id]]}</i></b>"
                                  + "\n\n" + cjason_statham, call.message.chat.id, call.message.message_id,
                                  reply_markup=markup_inline, parse_mode="HTML")
        elif call.data == "Random wisdom":
            random_number = randint(0, len(jasons_wisdoms) - 1)
            jasons_voc[call.message.chat.id] = random_number
            bot.edit_message_text(str(jasons_voc[call.message.chat.id] + 1) + "/" + str(
                len(jasons_wisdoms)) + "\n\n" + f"<b><i>{jasons_wisdoms[jasons_voc[call.message.chat.id]]}</i></b>"
                                  + "\n\n" + cjason_statham, call.message.chat.id, call.message.message_id,
                                  reply_markup=markup_inline, parse_mode="HTML")
        elif call.data == "Jason Subscribe":
            set_changer(1, call.message.chat.id)
            if call.message.chat.id in jason_sub_set:
                markup_inline = telebot.types.InlineKeyboardMarkup()
                item_previous = telebot.types.InlineKeyboardButton(text="<", callback_data="Previous")
                item_next = telebot.types.InlineKeyboardButton(text=">", callback_data="Next")
                item_random = telebot.types.InlineKeyboardButton(text="🇷", callback_data="Random wisdom")
                item_jason_subscribe = telebot.types.InlineKeyboardButton(
                    text="Вы подписаны на получение мудростей", callback_data="Jason Unsubscribe")
                markup_inline.add(item_previous, item_random, item_next)
                markup_inline.add(item_jason_subscribe)
                bot.edit_message_text(str(jasons_voc[call.message.chat.id] + 1) + "/" + str(
                    len(jasons_wisdoms)) + "\n\n" + f"<b><i>{jasons_wisdoms[jasons_voc[call.message.chat.id]]}</i></b>"
                                      + "\n\n" + cjason_statham, call.message.chat.id, call.message.message_id,
                                      reply_markup=markup_inline, parse_mode="HTML")
                printinformation(call.message, "!Подписался на циататы!")
        elif call.data == "Jason Unsubscribe":
            set_changer(0, call.message.chat.id)
            if call.message.chat.id not in jason_sub_set:
                markup_inline = telebot.types.InlineKeyboardMarkup()
                item_previous = telebot.types.InlineKeyboardButton(text="<", callback_data="Previous")
                item_next = telebot.types.InlineKeyboardButton(text=">", callback_data="Next")
                item_random = telebot.types.InlineKeyboardButton(text="🇷", callback_data="Random wisdom")
                item_jason_subscribe = telebot.types.InlineKeyboardButton(
                    text="Подписаться на получения мудростей", callback_data="Jason Subscribe")
                markup_inline.add(item_previous, item_random, item_next)
                markup_inline.add(item_jason_subscribe)
                bot.edit_message_text(str(jasons_voc[call.message.chat.id] + 1) + "/" + str(
                    len(jasons_wisdoms)) + "\n\n" + f"<b><i>{jasons_wisdoms[jasons_voc[call.message.chat.id]]}</i></b>"
                                      + "\n\n" + cjason_statham, call.message.chat.id, call.message.message_id,
                                      reply_markup=markup_inline, parse_mode="HTML")
                printinformation(call.message, "!Отписался от циатат!")

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    # заказ Дима
    @bot.message_handler(commands=['zakaz'])
    def zakaz(message):
        bot.reply_to(message,
                     text=f"Напишите мне свои пожелания в ответе на это сообщение, смахнув его влево, как это сделал я,"
                          f" чтобы подтвердить заказ, тогда в скором времени с вами свяжется Diminas для "
                          f"уточнения параметров заказа")
        bot.register_next_step_handler(message, replying)

    # ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓

    # ответ на сообщение по поводу заказа Дима
    def replying(message):
        if message.reply_to_message:
            bot.send_message(823899679,
                             f"{message.from_user.first_name} {message.from_user.last_name}: " + message.text +
                             " https://t.me/" + str(message.from_user.username))
            with open("Zakazi.txt", "a", encoding="utf-8") as file:
                file.write(vremya(time.ctime().split()) + ", " + str(message.chat.id) + " " + str(
                    message.from_user.first_name) + " " + str(
                    message.from_user.last_name) + ":" + " " + message.text + "\n" + "https://t.me/" + str(
                    message.from_user.username) + "\n")
                file.close()
            bot.send_photo(message.chat.id, open('picture.jpg', 'rb'),
                           caption=f"{message.from_user.first_name}, ваши пожелания будут переданы Diminas")
        else:
            bot.send_message(message.chat.id, "Заказ отменён")

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    # Команда погода
    @bot.message_handler(commands=['weather'])
    def vivodpogoda(message):
        printinformation(message, "!вызов погоды!")
        bot.send_message(message.chat.id, "Введи название населенного пункта: ")
        bot.register_next_step_handler(message, get_weather)

    # ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓

    # Функция погоды Влад П
    def get_weather(message):
        city = message.text.strip().lower()
        res = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={getenv("WEATHER_TOKEN")}&units=metric')
        if res.status_code == 200:
            data = json.loads(res.text)
            temp = data["main"]["temp"]
            bot.reply_to(message,
                         f'Сейчас погода в населённом пункте:\n'
                         f'Температура воздуха   -   {round(data["main"]["temp"], 1)}°C\n'
                         f'Ощущается как   -   {round(data["main"]["feels_like"], 1)}°C\n'
                         f'Влажность   -   {data["main"]["humidity"]}%\n'
                         f'Скорость ветра   -   {round(data["wind"]["speed"], 1)}м/c')
            printinformation(message, f"!вызов погоды, успешно: {city}!")
            if int(temp) < 10:
                bot.send_message(message.chat.id, "Не забудьте надеть шапку 🙂")
        else:
            printinformation(message, "!вызов погоды, провал!")
            bot.reply_to(message, 'Город указан неверно')

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    @bot.message_handler(commands=['key'])
    def get_key(message):
        # создание уникального восьмеричного ключа для пересылки с использованием chat.id
        key = oct(((message.chat.id + 2) * 5) + 9)
        bot.send_message(message.chat.id, f'Ваш ключ от чата для пересылки картинок из VK в следующем сообщении.\n\n '
                                          f'Напишите слово "Привет" в сообщения сообщества https://vk.me/gooryewood и '
                                          f'следуйте дальнейшим инструкциям.')
        bot.send_message(message.chat.id, key)
        printinformation(message, f"!получен ключ {key}!")

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    # Команда время
    @bot.message_handler(commands=['time'])
    def vivodvremya(message):
        bot.send_message(message.chat.id, vremya(time.ctime().split()))
        printinformation(message, "!вызов времени!")

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    # Команда анекдоты
    @bot.message_handler(commands=['joke'])
    def anekdot(message):
        anekdoti(message)

    # ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓

    # Функция с анекдотами Дима
    def anekdoti(message):
        mid = message.chat.id
        if mid not in joke_voc.keys():
            joke_voc[mid] = manekdoti.copy()
            random_number = randint(0, len(joke_voc[mid]) - 1)
            mes(message, joke_voc[mid][random_number])
            del joke_voc[mid][random_number]
            printinformation(message, "!выдача шутки, впервые создан массив шуток!")
        elif len(joke_voc[mid]) == 0:
            joke_voc[mid] = manekdoti.copy()
            random_number = randint(0, len(joke_voc[mid]) - 1)
            mes(message, "Вы посмотрели все анекдоты, сейчас они пойдут заново)")
            mes(message, joke_voc[mid][random_number])
            del joke_voc[mid][random_number]
            printinformation(message, "!выдача шутки, обновлён массив шуток!")
        else:
            random_number = randint(0, len(joke_voc[mid]) - 1)
            mes(message, joke_voc[mid][random_number])
            del joke_voc[mid][random_number]
            printinformation(message, "!выдача шутки!")

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    # Функция Влада для выдачи мемов
    @bot.message_handler(commands=['meme'])
    def meme(message):
        if len(mass) != 0:
            rand = randint(0, len(mass) - 1)
            photo = open(f'meme/{mass[rand]}', 'rb')
            bot.send_photo(message.chat.id, photo)
            photo.close()
            del mass[rand]
            printinformation(message, "!вызов выдачи мема, мем выдан!")
        else:
            bot.send_message(message.chat.id, "Мемы закончились :( \nЖелаете вернуться на начало?"
                                              " Если хотите это сделать, напишите 'да'")
            printinformation(message, "!вызов выдачи мема, мемы кончились!")
            bot.register_next_step_handler(message, meme2)

    # ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓

    # 50/50 Димы и Влада Л функция для восстановления длины списка
    def meme2(message):
        global mass
        if message.content_type == 'text' and word(message.text) == "да":
            mass = listdir(path='meme')
            bot.send_message(message.chat.id, text="Список восстановлен")
            printinformation(message, "!вызов восставновления мема, успешно!")
        else:
            bot.send_message(message.chat.id, text="Список не восстановлен")
            printinformation(message, "!вызов восставновления мема, не восстановлено!")

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    # моя функция для активаии сохранения мемов через команду
    @bot.message_handler(commands=['photo'])
    def photos(message):
        bot.send_message(message.chat.id, text="Жду мемчик для отправления на модерацию)")
        printinformation(message, "!вызов отправления мема на модерацию!")
        bot.register_next_step_handler(message, photosaver)

    # ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓

    # Функция для сохраниения мемов в папке не модерированные Влад Л
    def photosaver(message):
        global limit
        if message.content_type == 'photo':
            file_id = message.photo[-1].file_id
            file_info = bot.get_file(file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            with open(f"not moderated/{str(limit)}.jpg", 'wb') as new_file:
                new_file.write(downloaded_file)
                new_file.close()
            limit += 1
            printinformation(message, "!вызов отправления мема на модерацию, успешно!")
            bot.send_message(chat_id=message.chat.id, text="Картинка отправлена на модерацию")
        else:
            printinformation(message, "!вызов отправления мема на модерацию, провален!")
            bot.send_message(message.chat.id, text="Кажется, это не картинка")
            bot.send_message(message.chat.id, text="😢")

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    # Начало функции преобразующей английскую раскладку в русскую
    @bot.message_handler(commands=['en_to_ru'])
    def keyboard_transfer(message):
        printinformation(message, "!вызов перевода на русскую раскладку!")
        bot.send_message(message.chat.id, "Отправьте текст")
        bot.register_next_step_handler(message, en_to_ru)

    # ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓

    # Функция, преобразующая английскую раскладку в русскую
    def en_to_ru(message):
        en_ru = {" ": " ", "A": "ф", "B": "И", "C": "С", "D": "В", "E": "У", "F": "А", "G": "П", "H": "Р", "I": "Ш",
                 "J": "О", "K": "Л", "L": "Д", "M": "Ь", "N": "Т", "O": "Щ", "P": "З", "Q": "Й", "R": "К", "S": "Ы",
                 "T": "Е", "U": "Г", "V": "М", "W": "Ц", "X": "Ч", "Y": "Н", "Z": "Я", "~": "Ё", "a": "ф", "b": "и",
                 "c": "с", "d": "в", "e": "у", "f": "а", "g": "п", "h": "р", "i": "ш", "j": "о", "k": "л", "l": "д",
                 "m": "ь", "n": "т", "o": "щ", "p": "з", "q": "й", "r": "к", "s": "ы", "t": "е", "u": "г", "v": "м",
                 "w": "ц", "x": "ч", "y": "н", "z": "я", "`": "ё", ",": "б", "<": "Б", ".": "ю", ">": "Ю", "[": "х",
                 "{": "Х", "_": "_", "\n": "\n", "’": "’", "]": "ъ", "}": "Ъ", "'": "э", '"': "Э", ";": "ж", ":": "Ж",
                 "/": ".", "?": ",", "&": "?", "@": '"', "#": "№", "$": ";", "^": ":", "|": "/"}
        text = message.text
        for x in en_ru:
            if x in text:
                text = text.replace(x, en_ru[x])
        bot.send_message(message.chat.id, text)
        printinformation(message, "!вызов перевода на русскую раскладку успешно!")

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    # функция для вывода информации об использовании в консоль Дима
    def printinformation(message, reason):
        print(vremya(time.ctime().split()), message.chat.id, message.from_user.first_name,
              str(message.from_user.last_name) + ":", message.text,
              "https://t.me/" + str(message.from_user.username) + reason)

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    # Функция, переводящая время на русский язык Дима
    def vremya(rtime):
        p = []
        datas = {"Mon": "Понедельник - бездельник", "Tue": "Вторник - затворник", "Wed": "Среда - тамада",
                 "Thu": "Четверг - в шок поверг", "Fri": "Пятница - развратница", "Sat": "Суббота - вполоборота",
                 "Sun": "Воскресенье - день веселья", "Feb": "Февраля", "Mar": "Марта", "Apr": "Апреля", "May": "Мая",
                 "Jun": "Июня", "Jul": "Июля", "Sep": "Сентября", "Oct": "Октября", 'Nov': 'Ноября'}
        for x in range(2):
            p.append(datas[rtime[x]])
        for x in range(2, 5):
            p.append(rtime[x])
        vremena = p[3][:5] + "," + " " + p[2] + " " + p[1] + " " + p[4] + "," + " " + p[0]
        return vremena

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    # Член Дима
    def chlen(message):
        k = 0
        ll = message.text.split()
        for x in ll:
            if x.isdigit() and len(ll) == 3:
                k += 1
        bot.send_message(message.chat.id, text=f"Начало вычислений")
        for x in range(5, 0, -1):
            time.sleep(1)
            bot.send_message(message.chat.id, str(x))
        if k == 3:
            bot.send_photo(message.chat.id, requests.get(
                "https://4lapy.ru/resize/1664x1000/upload/medialibrary/270/2703fd71a17c0843c0b91bbe28c4fe0f.jpg"
                "").content,
                           caption="Длина рассчитываемого члена равна " + str(randint(5, 20)) + " сантиметров")
        else:
            bot.send_message(message.chat.id, str("Размеры не соответствуют общепринятым стандартам"))

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    @bot.message_handler(content_types=['text'])  # функция реагирующая на текст, использующая его, как команды
    # основная функция Дима
    def privetstvie(umessage):
        w = word(f"{umessage.text}")
        if w == "привет":
            bot.send_message(umessage.chat.id,
                             text=f"Привет, я Diminas Bot, у меня есть несколько различных команд, чтобы узнать их, "
                                  f"напиши «Команды»")
        elif w == "команды":
            bot.send_message(umessage.chat.id,
                             text=f"Команды: \nПогода - узнать погоду\nВремя - узнать время по мск\nАнекдот(ы) - "
                                  f"попросить анекдот\nКлюч - получить ключ для VK\nМем - получить мем\nЗагрузить - "
                                  f"загрузить мем в бота\nРаскладка - перевести текст с английской раскладки на русскую"
                                  f" \nТакже можно воспользоваться быстрыми командами, нажав сюда\n⬇️")
        elif w == "время":
            bot.send_message(umessage.chat.id, text=str(vremya(time.ctime().split())))
        elif w == "погода":
            bot.send_message(umessage.chat.id, "Введи название населенного пункта: ")
            bot.register_next_step_handler(umessage, get_weather)
        elif w == "анекдот" or word(w) == "анекдоты":
            anekdoti(umessage)
        elif w == "спасибо":
            blagodar = ["Обращайся, бро", "Бажожо"]
            bot.send_message(umessage.chat.id, text=str(blagodar[randint(0, len(blagodar) - 1)]))
        elif w == "заказать себе бота":
            zakaz(umessage)
        elif w == "как дела?" or w == "как дела":
            bot.send_message(umessage.chat.id, text=f"Нормально")
        elif w == "мем":
            meme(umessage)
        elif w == "загрузить":
            photos(umessage)
        elif w == "ключ":
            get_key(umessage)
        elif word(w) == "член":
            bot.send_message(umessage.chat.id,
                             text=f"Напишите параметры пятки человека через пробел д×ш×в в миллиметрах,"
                                  f" например:\n 40 30 10")
            bot.register_next_step_handler(umessage, chlen)
        elif word(w) == "раскладка":
            en_to_ru(umessage)
        else:
            bot.send_message(umessage.chat.id, text=umessage.text)
        printinformation(umessage, "!случайное слово!")

    bot.polling(none_stop=True, timeout=123)


# def sander() -> None:
#     while True:
#         print(jason_sub_set)
#         if len(jason_sub_set) > 0:
#             for x in jason_sub_set:
#                 bot.send_message(x, jasons_wisdoms[randint(0, len(jasons_wisdoms() - 1))])
#                 time.sleep(5)
#         time.sleep(10)

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


# ...........................................,:;;,..........................................
# ..........................................+%%S%%+,........................................
# .........................................*%%%%%%%*,.......................................
# ........................................;%%%?:*%%%+.......................................
# .......................................,?%%%:.:%%%%,......................................
# .......................................;%%%*...*%%%+......................................
# .......................................*%%%;...:%%%?,.....................................
# ......................................,??%?,...,?%?%:.....................................
# ......................................;%?%*.....*%?%;.....................................
# ......................................+%?%+.....+%?%+.....................................
# ...............................,,,,,::*%%%*;;,..;%%%?:::,,,,..............................
# ......................,,::;++***????%%%%%%%%%?,.:%%%%SSSSSS%%??*+;;:,.....................
# ...................,;+**????????????**%%%%***;..:%%%%??%%%SSS#####SS%?+:..................
# ..................;******++;:::,,,,..,?%%%:.....,%%%%,.,,,,::;;+*?%SSS#S?,................
# .................,*****;:,...........,%%%%:......+??;............,:+%SS##:................
# ..................:+**???***++;;;:::,:%SSS;,,,,,,,,,,,:::;;++*??%SS###S%;.................
# ....................,:++*???????????%%SSSS%?%%%%%%%%%SSSSSSS####SS%%*+:...................
# ........................,,::;;+++***??%SSS%%%%%%%%SSS%%%???**++;:,,.......................
# .....................................,*SSS+,,,,,+SSS?,,...................................
# ......................................+SSS*.....*SSS*.....................................
# ......................................;SSS%,....?SSS;.....................................
# ......................................,SSSS:...,SSSS:.....................................
# .......................................?SSS+...;SSS?......................................
# .......................................;SSS%,..?SSS+......................................
# .......................................,%SSS+.;SSS%,......................................
# ........................................:SSS%+%SSS;.......................................
# .........................................;SSSSSSS+........................................
# ..........................................:*%%%?;.........................................
# ............................................,,,...........................................


# Главная функция, которая запускает 2 процессса
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=tgbot)
    p1.start()
    p2 = multiprocessing.Process(target=vk_bot_funk)
    p2.start()
    # p3 = multiprocessing.Process(target=sander)
    # p3.start()
