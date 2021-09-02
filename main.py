import discord
import time
import mysql.connector
from cache import admin_id, admin_id2, channel_id, election_msg, CANDIDATES
from token import token

emojis = {'1️⃣': 1, '2️⃣': 2, '3️⃣': 3, '4️⃣': 4, '5️⃣': 5}

client = discord.Client()

class Elections:
    def __init__(self, candidates) -> None:
        self.candidates = candidates

    def check_right(self, author):
        data_file = open('data.txt', 'r')
        data = data_file.read().split()
        data_file.close()
        voters = [int(i) for i in data[self.candidates:]]

        if hash(author) in voters:
            return False
        else:
            return True
    
    def str_votes(self, votes):
        string = '    Кандидат 1 - ' + str(votes[0])
        for i in range(1, self.candidates):
            string += '\n    Кандидат ' + str(i+1) + ' - ' + str(votes[i])

        return string

    def add_logs(self, newdata):
        logs_file = open('logs.txt', 'r')
        data = logs_file.read()
        logs_file.close()

        data += newdata

        data_file = open('logs.txt', 'w')
        data_file.write(data)
        data_file.close()

    def on_ready(self):
        cur_time = '[' + time.strftime('%X') + ']'
        print(cur_time, 'Logged in as', client.user)

        data_file = open('data.txt', 'r')
        data = data_file.read().split()
        data_file.close()
        votes = [int(i) for i in data[:self.candidates]]
        
        print('Current election:')
        try:
            print(self.str_votes(votes))
        except:
            print('Error. Print \'delete election\'')
        print('___________________')

        self.add_logs(cur_time + ' Logged in as ' + str(client.user) + '\n' + 'Current election:\n' + self.str_votes(votes) + '\n')

    def vote_for(self, number, user):
        if self.check_right(user):
            data_file = open('data.txt', 'r')
            data = data_file.read().split()
            data_file.close()

            votes = [int(i) for i in data[:self.candidates]]
            voters = [int(i) for i in data[self.candidates:]]
            votes[number-1] += 1
            voters.append(hash(user))
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
            print(cur_time, '+1 к Кандидат ' + str(number))
            print(self.str_votes(votes))

            mydb = mysql.connector.connect(
                host="mydb.tamk.fi",
                user="cpsvva",
                password="6S52I9So",
                database="dbcpsvva1"
            )

            mycursor = mydb.cursor()

            sql = "INSERT INTO votes (candidate) VALUES ({0});".format(number)
            mycursor.execute(sql)
            mydb.commit()
            mydb.close()

            self.add_logs(cur_time + ' +1 к Кандидат ' + str(number) + '\n' + self.str_votes(votes) + '\n')

            return '{0.mention}, ваш голос засчитан. Это сообщение будет удалено через 15 секунд.'.format(user)

        else:
            cur_time = '[' + time.strftime('%X') + ']'
            print(cur_time, '{0.name} did not manage to vote'.format(user))

            self.add_logs(cur_time + ' {0.name} did not manage to vote\n'.format(user))

            return '{0.mention}, вы не можете голосовать повторно. Это сообщение будет удалено через 15 секунд.'.format(user)

    def delete(self, message):
        data_file = open('data.txt', 'w')
        data_file.write('0 ' * self.candidates)
        data_file.close()

        mydb = mysql.connector.connect(
            host="mydb.tamk.fi",
            user="cpsvva",
            password="6S52I9So",
            database="dbcpsvva1"
        )

        mycursor = mydb.cursor()

        sql = "TRUNCATE TABLE votes;"
        mycursor.execute(sql)
        mydb.commit()
        mydb.close()

        cur_time = '[' + time.strftime('%X') + ']'
        print(cur_time, 'Election is deleted')
        self.add_logs(cur_time + ' Election is deleted')
        return '{0.author.mention}, голосование успешно удалено'.format(message)

    def delete_logs(self, message):
        cur_time = '[' + time.strftime('%X') + ']'
        print(cur_time, 'Logs are deleted')
        data_file = open('logs.txt', 'w')
        data_file.write(cur_time + ' Logs are deleted\n')
        data_file.close()
        return '{0.author.mention}, логи успешно удалены'.format(message)

    def result(self):
        cur_time = '[' + time.strftime('%X') + ']'
        data_file = open('data.txt', 'r')
        data = data_file.read().split()
        data_file.close()
        votes = [int(i) for i in data[:self.candidates]]
        print(cur_time, 'Current election:')
        print(self.str_votes(votes))
        







newElections = Elections(CANDIDATES)

@client.event
async def on_ready():
    newElections.on_ready()

@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.channel.id != channel_id or user.id == client.user.id:
        return

    elif str(reaction) in emojis:
        if emojis[str(reaction)] <= newElections.candidates:
            msg = newElections.vote_for(emojis[str(reaction)], user)
            newmsg = await reaction.message.channel.send(msg)
            await reaction.remove(user)
            await newmsg.delete(delay = 15)
        else:
            await reaction.remove(user)

    else:
            await reaction.remove(user)

@client.event
async def on_message(message):
    if message.author.id == client.user.id or message.channel.id != channel_id:
        return

    elif message.author.id == admin_id or message.author.id == admin_id2:
        if message.content == 'delete election':
            msg = await message.channel.send(newElections.delete(message))
            await message.delete()
            await msg.delete(delay = 10)
        elif message.content == 'delete logs':
            msg = await message.channel.send(newElections.delete_logs(message))
            await message.delete()
            await msg.delete(delay = 10)
        elif message.content == 'election':
            await message.channel.send(file=discord.File('header1.png'))
            await message.channel.send(file=discord.File('header2.png'))
            await message.channel.send(election_msg)
            for i in range(newElections.candidates):
                await message.channel.last_message.add_reaction(list(emojis)[i])
            await message.delete()
        elif message.content == 'result':
            newElections.result()
            await message.delete()

client.run(token)