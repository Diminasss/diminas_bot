from main import bot
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from os import getenv

vk_session = vk_api.VkApi(token=getenv('VK_TOKEN'))
longpoll = VkLongPoll(vk_session)
user_states = {}
from_pic_to_pic = {}
last_msg_id = 0


def set_state(user, state):
    global user_states
    user_states[user] = state


def get_state(user):
    return user_states[user]


def vk_sender(msg_id, text):
    vk_session.method('messages.send', {'user_id': msg_id, 'message': text, 'random_id': 0})


def imagehaver(event):
    result = vk_session.method('messages.getById', {"message_ids": [event.message_id], 'group_id': 176637807})
    conclusion = result['items'][0]['attachments'][0]['photo']['sizes']
    heights = []
    height_to_url = {}
    for photo_dict in conclusion:
        heights.append(int(photo_dict['height']))
        height_to_url[int(photo_dict['height'])] = photo_dict['url']
    vk_sender(event.user_id, "Картинка уже в TG")
    bot.send_photo(from_pic_to_pic[event.user_id], height_to_url[max(heights)])


def key_logger(event):
    try:
        key = ((int(event.text, 8) - 9) // 5) - 2
        user = vk_session.method("users.get", {"user_ids": event.user_id})
        fullname = user[0]['first_name'] + ' ' + user[0]['last_name']
        from_pic_to_pic[event.user_id] = key
        vk_sender(event.user_id, "Инициализирован")
        bot.send_message(key, f"Ваш ключ инициализирован пользователем {fullname}")
    except TypeError:
        vk_sender(event.user_id, "Не инициализирован, непредвиденный сценарий")


def vk_bot_funk():
    global last_msg_id
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            if event.user_id not in user_states:
                set_state(event.user_id, 0)
            att = event.attachments
            msg = event.text.lower()
            msg_id = event.user_id
            if msg == "pic":
                if event.user_id in from_pic_to_pic:
                    if get_state(event.user_id) == "pic":
                        set_state(event.user_id, 0)
                        vk_sender(msg_id, "Режим пересылки отключён")
                    else:
                        set_state(event.user_id, "pic")
                        vk_sender(msg_id, "Режим пересылки активирован")
                else:
                    vk_sender(msg_id, "Инициализируйтесь с помощью команды reg ключём из https://t.me/Diminas_Bot")

            if msg == "привет":
                set_state(event.user_id, 0)
                vk_sender(msg_id, "Привет, мой основной функционал - пересылание картинок из VK в TG.\n\n Сначала "
                                  "ты должен воспользоваться командой 'reg', и после её использования отправить мне"
                                  "ключ, который был получен в TG. \n\nЕсли ты уже инициализировался, то для включения "
                                  "режима пересылки картинок воспользуйся командой 'pic'")

            if msg == "reg":
                vk_sender(msg_id, "Отправьте ключ")
                set_state(event.user_id, 'reg')
                last_msg_id = event.message_id

            if get_state(event.user_id) == 'reg' and len(att) == 0 and '0o' in event.text:
                key_logger(event)

            if get_state(event.user_id) == 'reg' and len(
                    att) == 0 and '0o' not in event.text and event.message_id != last_msg_id:
                vk_sender(msg_id, "Данный набор не явялется ключём")
                set_state(event.user_id, 0)

            if get_state(event.user_id) == 'pic' and len(att) != 0 and att['attach1_type'] == 'photo':
                imagehaver(event)
