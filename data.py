class Data():
    def __init__(self, data_type="Data"):
        self.fail_response = self.create_response(data_type)

    def __call__(self):
        return self.data

    def get_data(self, prompt):
        while True:
            data = input(prompt+":")
            if not self.validate:
                print(self.fail_response)
            else:
                self.data = data
                break

    def validate(self, data):
        print('im here')
        pass

    @staticmethod
    def create_response(resp):
        if resp is not None:
            return f"This is not a valid {resp}"
        else:
            return "This is not a valid data"


class ApiID(Data):

    def __init__(self):
        super().__init__(data_type="API ID")

    def __call__(self):
        return int(self.data)

    def validate(self, data):
        if data.isdigit() and len(data) == 7:
            return True
        else:
            return False


class ApiHASH(Data):

    def __init__(self):
        super().__init__(data_type="API HASH")

    def validate(self, data):
        if data.isalnum() and len(data) == 32:
            return True
        else:
            return False


class BotToken(Data):

    def __init__(self):
        super().__init__(data_type="Bot Token")

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

    def __init__(self):
        super().__init__(data_type="Channel ID")

    def validate(self, data):
        if ((data.isdigit() or (data[0] == "-" and data[1:].isdigit())) and
                (len(data) == 9 or len(data) == 10 or len(data) == 14)):
            return True
        else:
            return False

channel_id = ChannelID()
print(channel_id())

