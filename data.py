import json


class Data(object):

    data_type = None
    value = None
    json_file = "setup_data.json"

    def __init__(self):
        self.fail_response = self.create_response()

    def get_data_from_input(self):
        while True:
            temp = input("enter your "+self.data_type+": ")

            if not self.validate(temp):
                print(self.fail_response)
            else:
                self.value = temp
                break

    def get_data_from_input_as_int(self):
        self.get_data_from_input()
        self.value = int(self.value)

    def get_data_from_json(self):
        if self.data_type is not None:
            key = self.data_type
            with open(self.json_file, 'r') as f:
                temp_store = json.load(f)
                temp = temp_store[key]

            if not self.validate(temp):
                print("Received " + self.data_type + " is not valid.")
                print(f"Please check your {self.json_file}.")
            else:
                self.value = temp

    def validate(self, data):
        pass

    def create_response(self):
        if self.data_type is not None:
            return f"This is not a valid {self.data_type}"
        else:
            return "This is not a valid data"


class ApiID(Data):
    data_type = "api_id"

    def validate(self, data):
        data = str(data)
        if data.isdigit() and len(data) == 7:
            return True
        else:
            return False


class ApiHASH(Data):
    data_type = "api_hash"

    def validate(self, data):
        if data.isalnum() and len(data) == 32:
            return True
        else:
            return False


class BotToken(Data):
    data_type = "bot_token"

    def validate(self, data):
        if (len(data) == 45 and
                data[0:9].isdigit() and
                data[9] == ":" and
                data[10:17].isalnum() and
                data[17] == "-" and
                data[18:].isalnum()):
            return True
        else:
            return False


class ChannelID(Data):
    data_type = "channel_id"

    def validate(self, data):
        data = str(data)
        if ((data.isdigit() or (data[0] == "-" and data[1:].isdigit())) and
                (len(data) == 9 or len(data) == 10 or len(data) == 14)):
            return True
        else:
            return False



class TargetID(ChannelID):
    data_type = "target_id"


class ChannelsList(ChannelID):
    data_type = "channels_list"
    value = []

    def get_channels_list_from_input(self):
        print("enter id of a channels you want to collect messages from")
        print("leave empty input and press enter when you are done")
        while True:
            channel_id = input("enter channel id: ")
            if channel_id == '':
                break
            else:
                if self.validate(channel_id):
                    self.value.append(int(channel_id))
                else:
                    print("This is not a valid channel id.")

    def get_data_from_json(self):
        key = self.data_type
        with open(self.json_file, 'r') as f:
            temp_store = json.load(f)
            temp = temp_store[key]

        if not self.validate_id_list(temp):
            print("Received " + self.data_type + " is not valid.")
            print(f"Please check your {self.json_file}.")
        else:
            self.value = temp

    def get_data_from_input(self):
        while True:
            temp = int(input("enter channel id: "))
            if not self.validate(temp):
                print("This is not a valid channel id")
            else:
                self.value.append(temp)
                break

    def validate_id_list(self, id_list):
        outcome = True
        for id in id_list:
            if self.validate(id):
                pass
            else:
                outcome = False
                break
        return outcome





