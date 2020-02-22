admin_id = '224464016515268609'
channel_id = '498924583789920256'
token = 'NTUzMzA2MDA2NDQ5MjkxMjY0.D2MNrQ.FB6Ge8abT9ohIWsiy2JdbhMrXlQ'
election_msg = '__Для того чтобы проголосовать отправьте в чат цифру с номером кандидата__. Ваше сообщение будет удалено автоматически, чтобы сделать ваш голос тайным. Изменить свой голос **нельзя**. Голосовать дважды **нельзя**. Прием голосов будет завершен завтра в 22:00. __Если вы столкнулись с трудностями при голосовании - пишите <@!224464016515268609>__. \nКандидаты: \n1 - <@!346043390598578198>\n2 - <@!412979002391789571>\n3 - <@!342324906236575765>'
'''
bot-test_channel - 553696175572910082
госдума_channel - 588054912143851522
правительство_channel - 588064390205407234
plebiscite_channel - 498924583789920256
Lavash225 - 346043390598578198
Hirohito - 224464016515268609
slivachu - 342324906236575765
Adolf Igorev - 412979002391789571
'''
'''
    if message.content == 'channel':
        await client.send_message(message.channel, message.channel.id)

    if message.content == 'user':
        await client.send_message(message.channel, message.author.id)
'''