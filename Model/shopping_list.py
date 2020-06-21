import uuid


class shopping_list:

    def __init__(self):
        self.name = ''
        self.id = uuid.uuid4().hex
        self.items = []
        self.owners = []


