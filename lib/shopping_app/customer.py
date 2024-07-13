class Ownable:
    def __init__(self, owner):
        self._owner = owner

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        self._owner = new_owner
from user import User
from cart import Cart

class Customer(User):
    def __init__(self, name):
        super().__init__(name)
        self.cart = Cart(self)
