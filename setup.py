import json
import data

def first_setup():

    with open('setup_data.json', 'a+') as f:
        f.seek(0)
        content = f.read()

        if content != '':
            pass

        else:
            setup(f)

def setup(file):
    api_id = data.ApiID()
    api_id.get_data_from_input_as_int()

    api_hash = data.ApiHASH()
    api_hash.get_data_from_input()

    bot_token = data.BotToken()
    bot_token.get_data_from_input()

    target_id = data.TargetID()
    target_id.get_data_from_input_as_int()

    channels_list = data.ChannelsList()
    channels_list.get_channels_list_from_input()

    data_store = {'api_id': api_id.value,
                  'api_hash': api_hash.value,
                  'bot_token': bot_token.value,
                  'target_id': target_id.value,
                  'channels_list': channels_list.value}

    json.dump(data_store, file)
    print("Setup complete")
