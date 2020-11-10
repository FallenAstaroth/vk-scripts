import vk_api

token = input('Введите токен: ')

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

index = 0

print("\nЗапуск процесса накрутки...")
print("Обработка сообщений...\n")

while True:
    try:
        for msg in range(10):
            msgs = vk.execute(code='var offset =' + f'{index}' + ',chats=API.messages.getConversations({count:200,offset:offset}).items,i=0;while(i<chats.length){if(!chats[i].conversation.is_marked_unread){API.messages.markAsUnreadConversation({peer_id:chats[i].conversation.peer.id});}i=i+1;}return 1;')
        index += 100
        print(f'{index} сообщений обработано')
    except Exception as e:
        print(repr(e))
