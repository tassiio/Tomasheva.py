class MyDict(dict):
    def __init__(self):
        super().__init__()
        # print('My Dict')

    def get(self, user_key):
        if user_key not in self.keys():
            return 0
        else:
            return self[user_key]
