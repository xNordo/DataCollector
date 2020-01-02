import json
import data

def first_setup():
    with open('setup_data.json', 'a+') as f:
        f.seek(0)
        content = f.read()

        if content != '':
            pass

        else:
            print("This is first setup")

            print("enter your api id")
            while True:
                api_id = input('api id: ')
                if api_id.isdigit() and len(api_id) == 7:
                    api_id = int(api_id)
                    break
                else:
                    print("This is not a valid api id, try again")

            print("enter your api hash")
            while True:
                api_hash = input("api hash: ")
                if api_hash.isalnum() and len(api_hash) == 32:
                    break
                else:
                    print("This is not a valid api hash, try again")

            print("enter your bot token")
            while True:
                bot_token = input("bot token: ")
                if len(bot_token) == 45:
                    if bot_token[0:9].isdigit() and bot_token[9] == ":" and bot_token[10:17].isalnum() and bot_token[17] == "-" and bot_token[18:].isalnum():
                        break
                    else:
                        print("This is not a valid bot token")
                else:
                    print("This is not a valid bot token")

            print("enter your target channel id")
            while True:
                target_id = input("target id: ")
                if target_id.isdigit() or (target_id[1:].isdigit() and target_id[0] == "-"):
                    target_id = int(target_id)
                    break
                else:
                    print("This is not a valid channel id")

            print("enter id of a channels you want to collect messages from")
            print("leave empty input and press enter when you are done")
            channels_list = []
            while True:
                new_channel = input("channel id: ")
                if new_channel == '':
                    break
                elif new_channel.isdigit() or (new_channel[1:].isdigit() and new_channel[0] == "-"):
                    channels_list.append(int(new_channel))
                else:
                    print("This is not a valid channel id")

            data_store = {'api_id':api_id,'api_hash':api_hash,'bot_token':bot_token,'target_id':target_id,'channels_list':channels_list}
            json.dump(data_store,f)
            print("Setup complete")


