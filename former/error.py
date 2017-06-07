class Error:
    def __init__(self, messages=[]):
        self.messages = messages

    def get_messages(self):
        return self.messages

    def add_message(self, message):
        self.messages.append(message)

    def is_valid(self):
        return self.messages.count == 0
