# The facade pattern is used to make one object with a simple interface represent a complicated system.
# provides a simplified interface
# improves readability and testing
# for flexible and reusable code
# client calls facade interface that calls underneath classes
# https://www.codeproject.com/Articles/524231/FacadeplusPattern
# http://www.eurion.net/python-snippets/snippet/Facade.html

class Avatar:
    def create_avatar(self): pass
    def change_hair(self): pass
    def change_face(self): pass
    # ...

class Environment:
    def env_city(self): pass
    # ...

class Gui:
    def __index__(self):
        self.avatar = Avatar()
        self.env = Environment()

    def show_all(self): pass

class Stats:
    def set_level(self): pass
    # ....


class GameFacade:

    def __init__(self):
        self.gui = Gui()
        self.stats = Stats()

    def start(self):
        self.stats.set_level()
        self.gui.avatar.create_avatar()
        self.gui.env.env_city()
        # ...
        self.gui.show_all()

# Client:
if __name__ == '__main__':
    my_game = GameFacade() # here as simple as possible to use case
    my_game.start()


