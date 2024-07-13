
class Ownable:
    def __init__(self, owner):
        self._owner = owner

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        self._owner = new_owner

class Wallet:
    def __init__(self, balance=0):
        self.balance = balance

class User:
    def __init__(self, name):
        self.name = name
        self.wallet = Wallet()


from ownable import Ownable

class Item(Ownable):
    instances = []

    def __init__(self, name, price, owner=None):
        Ownable.__init__(self, owner)
        self.name = name
        self.price = price
        # Itemインスタンスの生成時、そのItemインスタンス(self)は、instancesというクラス変数に格納されます。
        Item.instances.append(self)

    def label(self):
        return {"name": self.name, "price": self.price}

    @staticmethod
    def item_all():
        # instancesを返します ==> Item.item_all()でこれまでに生成されたItemインスタンスを全て返すということです。
        return Item.instances

