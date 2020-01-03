from telethon import TelegramClient, events
from setup import first_setup
import json
import data

# TODO picture handler

if __name__ == '__main__':
    # initializes first setup if detects no data in setup_data.json
    first_setup()

    # gets all needed data from setup_data.json
    api_id = data.ApiID()
    api_id.get_data_from_json()
    api_id = api_id.value

    api_hash = data.ApiHASH()
    api_hash.get_data_from_json()
    api_hash = api_hash.value

    bot_token = data.BotToken()
    bot_token.get_data_from_json()
    bot_token = bot_token.value

    target_id = data.TargetID()
    target_id.get_data_from_json()
    target_id = target_id.value

    channels_list = data.ChannelsList()
    channels_list.get_data_from_json()
    channels_list = channels_list.value

    # connection setup
    try:
        bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
        client = TelegramClient("anon", api_id, api_hash)
    except:
        print("Something went wrong with connection, please check if api id, api hash and bot token is correct")

    print("___________________________________________________")

    # function to send message to target channel as a bot
    async def bot_send_message(channel_id, message_text):
        await bot.send_message(channel_id, message_text)

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


