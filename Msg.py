import vk_api

token = input('Введите токен: ')

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()


while True:
    try:
        index = 0
        for msg in range(10):
            msgs = vk.execute(code='var offset =' + f'{index}' + ',chats=API.messages.getConversations({count:200,offset:offset}).items,i=0;while(i<chats.length){if(!chats[i].conversation.is_marked_unread){API.messages.markAsUnreadConversation({peer_id:chats[i].conversation.peer.id});}i=i+1;}return 1;')
        index += 100
        print('Сообщения накручены')
        print('Возобновление процесса накрутки')
    except Exception as e:
        print(repr(e))
