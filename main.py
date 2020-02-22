import discord
import pickle
import time
from cache import token, admin_id, channel_id, election_msg

client = discord.Client()

def check_right(author_id):
    voters = pickle.load(open('voters.p', 'rb'))

    for i in voters:
        if author_id == i:
            vote_right = False
            return
        else:
            vote_right = True
    if len(voters) == 0:
        vote_right = True
    return vote_right


@client.event
async def on_ready():
    cur_time = '[' + time.strftime('%X') + ']'
    print(cur_time, 'Logged in as', client.user)

    votes = pickle.load(open('votes.p', 'rb'))
    print('Current election:')
    try:
        print('    Кандидат 1 -', votes[0], 
            '\n    Кандидат 2 -', votes[1],
            '\n    Кандидат 3 -', votes[2])
    except:
        print('Error. Print \'delete election\'')
    print('___________________')
    


@client.event
async def on_message(message):
    if message.author.id == client.user.id or message.channel.id != channel_id:
        return

    elif message.content == 'delete election' and message.author.id == admin_id:
        votes = [0, 0, 0]
        voters = []
        pickle.dump(votes, open("votes.p", "wb"))
        pickle.dump(voters, open("voters.p", "wb"))
        msg = '{0.author.mention}, голосование успешно удалено'.format(message)
        cur_time = '[' + time.strftime('%X') + ']'
        print(cur_time, 'Election is deleted')
        await client.send_message(message.channel, msg)
    
    elif message.content == 'election' and message.author.id == admin_id:
        await client.send_message(message.channel, election_msg)
    
    elif message.content == 'result' and message.author.id == admin_id:
        cur_time = '[' + time.strftime('%X') + ']'
        votes = pickle.load(open('votes.p', 'rb'))
        print(cur_time, 'Current election:')
        print('    Кандидат 1 -', votes[0], 
            '\n    Кандидат 2 -', votes[1],
            '\n    Кандидат 3 -', votes[2])
        await client.delete_message(message)

    elif message.content.startswith('1'):
        if check_right(message.author.id):
            voters = pickle.load(open('voters.p', 'rb'))
            votes = pickle.load(open('votes.p', 'rb'))
            votes[0] += 1
            voters.append(message.author.id)
            pickle.dump(voters, open("voters.p", "wb"))
            pickle.dump(votes, open("votes.p", "wb"))
            msg = '{0.author.mention}, ваш голос засчитан'.format(message)
            cur_time = '[' + time.strftime('%X') + ']'
            print(cur_time, '+1 к Кандидат 1')
            print('    Кандидат 1 -', votes[0], 
                '\n    Кандидат 2 -', votes[1],
                '\n    Кандидат 3 -', votes[2])
            await client.delete_message(message)
            await client.send_message(message.channel, msg)
        else:
            msg = '{0.author.mention}, вы не можете голосовать'.format(message)
            await client.delete_message(message)
            await client.send_message(message.channel, msg)

    elif message.content.startswith('2'):
        if check_right(message.author.id):
            voters = pickle.load(open('voters.p', 'rb'))
            votes = pickle.load(open('votes.p', 'rb'))
            votes[1] += 1
            voters.append(message.author.id)
            pickle.dump(voters, open("voters.p", "wb"))
            pickle.dump(votes, open("votes.p", "wb"))
            msg = '{0.author.mention}, ваш голос засчитан'.format(message)
            cur_time = '[' + time.strftime('%X') + ']'
            print(cur_time, '+1 к Кандидат 2')
            print('    Кандидат 1 -', votes[0], 
                '\n    Кандидат 2 -', votes[1],
                '\n    Кандидат 3 -', votes[2])
            await client.delete_message(message)
            await client.send_message(message.channel, msg)
        else:
            msg = '{0.author.mention}, вы не можете голосовать'.format(message)
            await client.delete_message(message)
            await client.send_message(message.channel, msg)

    elif message.content.startswith('3'):
        if check_right(message.author.id):
            voters = pickle.load(open('voters.p', 'rb'))
            votes = pickle.load(open('votes.p', 'rb'))
            votes[2] += 1
            voters.append(message.author.id)
            pickle.dump(voters, open("voters.p", "wb"))
            pickle.dump(votes, open("votes.p", "wb"))
            msg = '{0.author.mention}, ваш голос засчитан'.format(message)
            cur_time = '[' + time.strftime('%X') + ']'
            print(cur_time, '+1 к Кандидат 2')
            print('    Кандидат 1 -', votes[0], 
                '\n    Кандидат 2 -', votes[1],
                '\n    Кандидат 3 -', votes[2])
            await client.delete_message(message)
            await client.send_message(message.channel, msg)
        else:
            msg = '{0.author.mention}, вы не можете голосовать'.format(message)
            await client.delete_message(message)
            await client.send_message(message.channel, msg)

    elif message.content.startswith('clear'):
        amount = message.content.split()[1]
        print(amount)
        channel = message.channel
        messages = []
        async for message in client.logs_from(channel, limit=int(amount)):
            messages.append(message)
        await client.delete_messages(messages)

client.run(token)