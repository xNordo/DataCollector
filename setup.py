import json

def first_setup():
    f = open('setup_data.json', 'a+')
    f.seek(0)
    print(f)
    content = f.read()
    print(content)
    if content == '':
        print("This is first setup")
        print("enter your api id")
        api_id = int(input('api id: '))
        print("enter your api hash")
        api_hash = input("api hash: ")
        print("enter your bot token")
        bot_token = input("bot token: ")
        print("enter your target channel id")
        target_id = int(input("target id: "))
        print("enter id of a channels you want to collect messages from")
        print("leave empty input and press enter when you are done")
        channels_list = []
        while True:
            new_channel = input("channel id: ")
            if new_channel == '':
                break
            else:
                channels_list.append(int(new_channel))
        data_store = {'api_id':api_id,'api_hash':api_hash,'bot_token':bot_token,'target_id':target_id,'channels_list':channels_list}
        json.dump(data_store,f)
        print("Setup complete")
    f.close()
