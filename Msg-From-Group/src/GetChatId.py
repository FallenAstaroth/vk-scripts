import vk_api

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

f = open("authorization.txt", "r")
data = f.read()
line = data.split(':')
group_id = line[0]
group_token = line[1]

vk = vk_api.VkApi(token=group_token)
vk._auth_token()
vk.get_api()
longpoll = VkBotLongPoll(vk, group_id)

while True:
    try:
        print("Отправьте " + f'"1"' + " в беседу если бот имеет полный доступ к переписке/права администратора.\n"
              "Отправьте " + f'"[club{group_id}|1]"' + " в беседу если бот не имеет полного доступа к переписке/прав администратора.\n")
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.peer_id != event.object.from_id:
                    if event.object.text == "1" or event.object.text == f'[club{group_id}|1]':
                        chat = event.chat_id
                        print("Айди беседы: " + f'{chat}')
    except Exception as e:
        print(repr(e))
