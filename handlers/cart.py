class Cart:
    def __init__(self, userid):
        self.userid = userid
        self.items = list()
        self.total = 0

    def add_item(self, item):
        self.items.append(item)
        self.total += float(item["price"]) * int(item["amount"])

    def remove_item(self, item):
        self.items.remove(item)
        self.total -= item["price"] * item["amount"]

    def get_userid(self):
        return self.userid

    def __repr__(self):
        result = {
            "userid": self.userid,
            "items": self.items,
            "total": self.total
        }
        return str(result)

