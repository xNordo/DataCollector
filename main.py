from telethon import TelegramClient, events
from setup import first_setup
import json

# initializes first setup if detects no data in setup_data.json
first_setup()

# gets all needed data
with open('setup_data.json', 'r') as f:
    data_store = json.load(f)
    print(data_store)
    api_id = data_store['api_id']
    api_hash = data_store['api_hash']
    bot_token = data_store['bot_token']
    target_id = data_store['target_id']
    channels_list = data_store['channels_list']

# connection setup
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
client = TelegramClient("anon", api_id, api_hash)

print("___________________________________________________")
# function to send message to target channel as a bot
async def bot_send_message(target_id, message_text):
    await bot.send_message(target_id, message_text)

# new message handler
@client.on(events.NewMessage(chats=channels_list))
async def new_message_handler(event):
    # takes important stuff from event.message
    new_message_text = event.message.message
    chat_id = event.message.to_id.chat_id

    # admin info
    print("New message on chat: ", chat_id, " content: ", new_message_text)
    print("Resending message to chat: ", target_id)
    print("___________________________________________________")

    # resends new message
    await bot_send_message(target_id, new_message_text)

print()
client.start()
client.run_until_disconnected()


