import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as', client.user)

@client.event
async def on_message(message):
    if message.content == 'publish':
        await message.delete()
        await message.channel.send('@here\n__Уважаемые граждане сервера СДСП! К вам обращается кандидат на должность Генерального секретаря СДСП <@!346043390598578198>!__\n\nАгитационные кампании идут на сервере полным ходом и мы показываем **высокие успехи**! Несмотря на это, ещё рано объявлять победу и мы должны **бороться до конца**!\n\nElla Baker, активистка движения за **права человека**, говорила мудрые слова:\n> \n> *Дайте людям свет и они найдут свой путь.*\n> \nЭти слова так хорошо описывают наше время. Генеральный секретарь Михаил Трап долго держал СДСП в темноте, страхе и агрессии. Из-за его импульсивности некоторые наши сограждане были репрессированы, но мы не позволим этому забыться. **Я обещаю быть союзником света**, а не тьмы. **Голосуйте за нас**, ведь только так мы сможем найти свой истинный путь.\n\nПозавчера был запущен хэштег #БИДОН2020. Если вы хотите поддержать кампанию, при этом не прилагая никаких усилий, **добавьте к своему нику #БИДОН2020**. Также, главой комитета по мемам был назначен администратор паблика "слышу мемы" <@!224464016515268609>.\n\n__Голосуйте за <@!346043390598578198>! **Сделаем СДСП лучше чем когда-либо!**__')
        await message.channel.send(file=discord.File('bidon.jpg'))

client.run('NTUzMzA2MDA2NDQ5MjkxMjY0.XxBaRA.TPt7PIIKJPYdcCWxiG0XH3h4ahQ')
