import vk_api
import random
import time


def send_msg(user_id: int, message: str, attachment: str = ""):
    return vk.messages.send(**locals(), random_id=0)


def captcha_handler(captcha):
    key = input("Введите капчу {0}: ".format(captcha.get_url())).strip()
    return captcha.try_again(key)


def get_users(name):
    return vk.users.search(q=name, count=1000)


names = ['Ярослав', 'Богдан', 'Алина', 'Анна', 'Андрей', 'Максим', 'Альбина', 'Эрика', 'Никита', 'Даня', 'Стас', 'Захар', 'Василий', 'Лера', 'Игорь']

token = input('Введите токен: ')

vk_session = vk_api.VkApi(token=token, captcha_handler=captcha_handler)
vk = vk_session.get_api()

while True:
    try:
        name = random.choice(names)
        users = get_users(name)
        for user in users["items"]:
            msg = send_msg(user["id"], 'тест')
            time.sleep(1)
            print('Сообщение отправлено')

    except Exception as e:
        print(repr(e))