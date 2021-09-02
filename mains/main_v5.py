import discord
import pickle
import time
from cache import token, admin_id, channel_id, election_msg, CANDIDATES

def check_right(author):
    data_file = open('data.txt', 'r')
    data = data_file.read().split()
    data_file.close()
    voters = [int(i) for i in data[CANDIDATES:]]

    if hash(author) in voters:
        return False
    else:
        return True

def str_votes(votes):
    return '    Кандидат 1 - ' + str(votes[0]) + '\n    Кандидат 2 - ' + str(votes[1])

def add_logs(newdata):
    logs_file = open('logs.txt', 'r')
    data = logs_file.read()
    logs_file.close()

    data += newdata

    data_file = open('logs.txt', 'w')
    data_file.write(data)
    data_file.close()

class MyClient (discord.Client):


    async def on_ready(self):
        cur_time = '[' + time.strftime('%X') + ']'
        print(cur_time, 'Logged in as', client.user)

        data_file = open('data.txt', 'r')
        data = data_file.read().split()
        data_file.close()
        votes = [int(i) for i in data[:CANDIDATES]]
        
        print('Current election:')
        try:
            print(str_votes(votes))
        except:
            print('Error. Print \'delete election\'')
        print('___________________')

        add_logs(cur_time + ' Logged in as ' + str(client.user) + '\n' + 'Current election:\n' + str_votes(votes) + '\n')
    

    async def on_raw_reaction_add(self, event):
        if event.channel_id != channel_id or event.member.id == client.user.id:
            return

        elif str(event.emoji) == '1️⃣':
            if check_right(event.member):
                data_file = open('data.txt', 'r')
                data = data_file.read().split()
                data_file.close()

                votes = [int(i) for i in data[:CANDIDATES]]
                voters = [int(i) for i in data[CANDIDATES:]]
                votes[0] += 1
                voters.append(hash(event.member))
                data = ''
                voters.sort()
                for i in votes:
                    data += str(i) + ' '
                for i in voters:
                    data += str(i) + ' '
                
                data_file = open('data.txt', 'w')
                data_file.write(data)
                data_file.close()

                cur_time = '[' + time.strftime('%X') + ']'
                print(cur_time, '+1 к Кандидат 1')
                print(str_votes(votes))

                add_logs(cur_time + ' +1 к Кандидат 1\n' + str_votes(votes) + '\n')

                msg = '{0}, ваш голос засчитан. Это сообщение будет удалено через 15 секунд.'.format(event.member.mention)
                channel = client.get_channel(event.channel_id)
                newmsg = await channel.send(msg)
                await event.emoji.remove(event.member)
                await newmsg.delete(delay = 15)

            else:
                cur_time = '[' + time.strftime('%X') + ']'
                print(cur_time, '{0} did not manage to vote'.format(event.member.name))

                add_logs(cur_time + ' {0} did not manage to vote\n'.format(event.member.name))

                msg = '{0}, вы не можете голосовать повторно. Это сообщение будет удалено через 15 секунд.'.format(event.member.mention)
                channel = client.get_channel(event.channel_id)
                newmsg = await channel.send(msg)
                await event.emoji.remove(event.member)
                await newmsg.delete(delay = 15)


        elif str(event.emoji) == '2️⃣':
            if check_right(event.member):
                data_file = open('data.txt', 'r')
                data = data_file.read().split()
                data_file.close()

                votes = [int(i) for i in data[:CANDIDATES]]
                voters = [int(i) for i in data[CANDIDATES:]]
                votes[0] += 1
                voters.append(hash(event.member))
                data = ''
                voters.sort()
                for i in votes:
                    data += str(i) + ' '
                for i in voters:
                    data += str(i) + ' '
                
                data_file = open('data.txt', 'w')
                data_file.write(data)
                data_file.close()

                cur_time = '[' + time.strftime('%X') + ']'
                print(cur_time, '+1 к Кандидат 1')
                print(str_votes(votes))

                add_logs(cur_time + ' +1 к Кандидат 1\n' + str_votes(votes) + '\n')

                msg = '{0}, ваш голос засчитан. Это сообщение будет удалено через 15 секунд.'.format(event.member.mention)
                channel = client.get_channel(event.channel_id)
                newmsg = await channel.send(msg)
                await event.emoji.remove(event.member)
                await newmsg.delete(delay = 15)

            else:
                cur_time = '[' + time.strftime('%X') + ']'
                print(cur_time, '{0} did not manage to vote'.format(event.member.name))

                add_logs(cur_time + ' {0} did not manage to vote\n'.format(event.member.name))

                msg = '{0}, вы не можете голосовать повторно. Это сообщение будет удалено через 15 секунд.'.format(event.member.mention)
                channel = client.get_channel(event.channel_id)
                newmsg = await channel.send(msg)
                await event.emoji.remove(event.member)
                await newmsg.delete(delay = 15)


        else:
            await event.emoji.remove(event.member)

    async def on_message(self, message):
        if message.author.id == client.user.id or message.channel.id != channel_id:
            return

        elif message.content == 'delete election' and message.author.id == admin_id:
            data_file = open('data.txt', 'w')
            data_file.write('0 0 0 0 ')
            data_file.close()
            msg = '{0.author.mention}, голосование успешно удалено'.format(message)
            cur_time = '[' + time.strftime('%X') + ']'
            print(cur_time, 'Election is deleted')
            add_logs(cur_time + ' Election is deleted')
            await message.channel.send(msg)
            await message.delete()

        elif message.content == 'delete logs' and message.author.id == admin_id:
            msg = '{0.author.mention}, логи успешно удалены'.format(message)
            cur_time = '[' + time.strftime('%X') + ']'
            print(cur_time, 'Logs are deleted')
            data_file = open('logs.txt', 'w')
            data_file.write(cur_time + ' Logs are deleted\n')
            data_file.close()
            await message.channel.send(msg)
            await message.delete()
        
        elif message.content == 'election' and message.author.id == admin_id:
            await message.channel.send(file=discord.File('header1.png'))
            await message.channel.send(file=discord.File('header2.png'))
            await message.channel.send(election_msg)
            await message.channel.last_message.add_reaction('1️⃣')
            await message.channel.last_message.add_reaction('2️⃣')
            await message.channel.last_message.add_reaction('3️⃣')
            await message.channel.last_message.add_reaction('4️⃣')
            await message.delete()
        
        elif message.content == 'result' and message.author.id == admin_id:
            cur_time = '[' + time.strftime('%X') + ']'
            data_file = open('data.txt', 'r')
            data = data_file.read().split()
            data_file.close()
            votes = [int(i) for i in data[:4]]
            print(cur_time, 'Current election:')
            print(str_votes(votes))
            await message.delete()

    

#MyIntents = discord.Intents.all()
#MyIntents.reactions = True


client = MyClient()
client.run(token)