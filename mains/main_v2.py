import discord
import pickle
import time
from cache import token, admin_id, channel_id, election_msg

client = discord.Client()

def check_right(author_id):
    data_file = open('data.txt', 'r')
    data = data_file.read().split()
    data_file.close()
    voters = [int(i) for i in data[3:]]

    if author_id in voters:
        return False
    else:
        return True


@client.event
async def on_ready():
    cur_time = '[' + time.strftime('%X') + ']'
    print(cur_time, 'Logged in as', client.user)

    data_file = open('data.txt', 'r')
    data = data_file.read().split()
    data_file.close()
    votes = [int(i) for i in data[:3]]
    
    print('Current election:')
    try:
        print('    Кандидат 1 -', votes[0], 
            '\n    Кандидат 2 -', votes[1],
            '\n    Кандидат 3 -', votes[2])
    except:
        print('Error. Print \'delete election\'')
    print('___________________')
    


@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.channel.id != channel_id or user.id == client.user.id:
        return

    elif str(reaction) == '1️⃣':
        if check_right(user.id):
            data_file = open('data.txt', 'r')
            data = data_file.read().split()
            data_file.close()

            votes = [int(i) for i in data[:3]]
            voters = [int(i) for i in data[3:]]
            votes[0] += 1
            voters.append(user.id)
            data = ''
            for i in votes:
                data += str(i) + ' '
            for i in voters:
                data += str(i) + ' '
            
            data_file = open('data.txt', 'w')
            data_file.write(data)
            data_file.close()

            cur_time = '[' + time.strftime('%X') + ']'
            print(cur_time, '+1 к Кандидат 1')
            print('    Кандидат 1 -', votes[0], 
                '\n    Кандидат 2 -', votes[1],
                '\n    Кандидат 3 -', votes[2])

            msg = '{0.mention}, ваш голос засчитан. Это сообщение будет удалено через 30 секунд'.format(user)
            await reaction.message.channel.send(msg)
            await reaction.remove(user)
            await reaction.message.channel.last_message.delete(delay = 30)
        else:
            cur_time = '[' + time.strftime('%X') + ']'
            print(cur_time, '{0.name} did not manage to vote'.format(user))

            msg = '{0.mention}, вы не можете голосовать'.format(user)
            await reaction.message.channel.send(msg)
            await reaction.remove(user)
            await reaction.message.channel.last_message.delete(delay = 30)


    elif str(reaction) == '2️⃣':
        if check_right(user.id):
            data_file = open('data.txt', 'r')
            data = data_file.read().split()
            data_file.close()

            votes = [int(i) for i in data[:3]]
            voters = [int(i) for i in data[3:]]
            votes[1] += 1
            voters.append(user.id)
            data = ''
            for i in votes:
                data += str(i) + ' '
            for i in voters:
                data += str(i) + ' '
            
            data_file = open('data.txt', 'w')
            data_file.write(data)
            data_file.close()

            cur_time = '[' + time.strftime('%X') + ']'
            print(cur_time, '+1 к Кандидат 2')
            print('    Кандидат 1 -', votes[0], 
                '\n    Кандидат 2 -', votes[1],
                '\n    Кандидат 3 -', votes[2])

            msg = '{0.mention}, ваш голос засчитан. Это сообщение будет удалено через 30 секунд'.format(user)
            await reaction.message.channel.send(msg)
            await reaction.remove(user)
            await reaction.message.channel.last_message.delete(delay = 30)
        else:
            cur_time = '[' + time.strftime('%X') + ']'
            print(cur_time, '{0.name} did not manage to vote'.format(user))

            msg = '{0.mention}, вы не можете голосовать'.format(user)
            await reaction.message.channel.send(msg)
            await reaction.remove(user)
            await reaction.message.channel.last_message.delete(delay = 30)


    elif str(reaction) == '3️⃣':
        if check_right(user.id):
            data_file = open('data.txt', 'r')
            data = data_file.read().split()
            data_file.close()

            votes = [int(i) for i in data[:3]]
            voters = [int(i) for i in data[3:]]
            votes[2] += 1
            voters.append(user.id)
            data = ''
            for i in votes:
                data += str(i) + ' '
            for i in voters:
                data += str(i) + ' '
            
            data_file = open('data.txt', 'w')
            data_file.write(data)
            data_file.close()

            cur_time = '[' + time.strftime('%X') + ']'
            print(cur_time, '+1 к Кандидат 3')
            print('    Кандидат 1 -', votes[0], 
                '\n    Кандидат 2 -', votes[1],
                '\n    Кандидат 3 -', votes[2])

            msg = '{0.mention}, ваш голос засчитан. Это сообщение будет удалено через 30 секунд'.format(user)
            await reaction.message.channel.send(msg)
            await reaction.remove(user)
            await reaction.message.channel.last_message.delete(delay = 30)
        else:
            cur_time = '[' + time.strftime('%X') + ']'
            print(cur_time, '{0.name} did not manage to vote'.format(user))

            msg = '{0.mention}, вы не можете голосовать'.format(user)
            await reaction.message.channel.send(msg)
            await reaction.remove(user)
            await reaction.message.channel.last_message.delete(delay = 30)


@client.event
async def on_message(message):
    if message.author.id == client.user.id or message.channel.id != channel_id:
        return

    elif message.content == 'delete election' and message.author.id == admin_id:
        data_file = open('data.txt', 'w')
        data_file.write('0 0 0 ')
        data_file.close()
        msg = '{0.author.mention}, голосование успешно удалено'.format(message)
        cur_time = '[' + time.strftime('%X') + ']'
        print(cur_time, 'Election is deleted')
        await message.channel.send(msg)
    
    elif message.content == 'election' and message.author.id == admin_id:
        await message.channel.send(election_msg)
        await message.channel.last_message.add_reaction('1️⃣')
        await message.channel.last_message.add_reaction('2️⃣')
        await message.channel.last_message.add_reaction('3️⃣')
        await message.delete()
    
    elif message.content == 'result' and message.author.id == admin_id:
        cur_time = '[' + time.strftime('%X') + ']'
        data_file = open('data.txt', 'r')
        data = data_file.read().split()
        data_file.close()
        votes = [int(i) for i in data[:3]]
        print(cur_time, 'Current election:')
        print('    Кандидат 1 -', votes[0],
            '\n    Кандидат 2 -', votes[1],
            '\n    Кандидат 3 -', votes[2])
        await message.delete()


client.run(token)
