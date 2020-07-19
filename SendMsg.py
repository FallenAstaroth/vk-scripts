import vk_api


def send_msg(user_id: int, message: str, attachment: str = ""):
    return vk.messages.send(**locals(), random_id=0)


def captcha_handler(captcha):
    key = input("Введите капчу {0}: ".format(captcha.get_url())).strip()
    return captcha.try_again(key)


def get_users(name):
    return vk.users.search(q=name, count=1000, fields='can_write_private_message')


token = input('Введите токен: ')
print('Введите имя, из которого нужно составить список пользователей. Рекомендую использовать каждое имя по 1 разу.')
name = input('Введите имя: ')

vk_session = vk_api.VkApi(token=token, captcha_handler=captcha_handler)
vk = vk_session.get_api()

while True:
    try:
        users = get_users(name)
        for user in users["items"]:
            if user["can_write_private_message"] == 1:
                msg = send_msg(user["id"], 'тест')
                print('Сообщение отправлено')
            else:
                print('Лс закрытые')
    except Exception as e:
        print(repr(e))
