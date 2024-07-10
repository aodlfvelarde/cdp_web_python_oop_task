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

class Seller(User, Ownable):
    def __init__(self, name):
        User.__init__(self, name)  # Inicializar la parte de User
        Ownable.__init__(self, self)