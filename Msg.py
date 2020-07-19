import vk_api

token = input('Введите токен: ')

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

msg_count = ['0', '200', '400', '600', '800', '1000', '1200', '1400', '1600', '1800', '2000', '2200', '2400', '2600', '2800', '3000']

while True:
    try:
        index = 0
        for count in msg_count:
            for msg in range(10):
                msgs = vk.execute(code='var offset =' + f'{msg_count[index]}' + ',chats=API.messages.getConversations({count:200,offset:offset}).items,i=0;while(i<chats.length){if(!chats[i].conversation.is_marked_unread){API.messages.markAsUnreadConversation({peer_id:chats[i].conversation.peer.id});}i=i+1;}return 1;')
            index += 1
            print('Сообщения накручены')
            print('Возобновление процесса накрутки')
    except Exception as e:
        print(repr(e))