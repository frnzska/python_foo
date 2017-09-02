# One instance of class with global access to state

# 1. Method: overwrite __new__() at instance creation
class Foo:
    __instance = None
    def __new__(cls, val):
        if Foo.__instance is None:
            Foo.__instance = object.__new__(cls)
        Foo.__instance.val = val
        return Foo.__instance

    def get_val(self):
        return Foo.__instance.val



# a = Foo(1)
# b = Foo(2)
# print(a.get_val()) # 2
# print(a == b) # True
# c = Foo(3).__class__
# print(c == a) # False -> voilated principle



# 2. Method: Decorator returns class instance
def singleton(cls):
    return cls()

@singleton
class Bar:
    def set_val(self, val):
        self.val = val

    def get_val(self):
        return self.val


# a = Bar
# a.set_val(1)
# b = Bar
# b.set_val(2)
# print(a == b) # True
# b.set_val(3)
# print(a == b) # True
# print(Foo.__class__ == b) # False


# 3. Method: Dont care if different instances exist as long as state is globally the same -> Borg
class Borg:
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

class Foo(Borg): # type Borg
    def __init__(self, arg):
        Borg.__init__(self)
        self.val = arg


a = Foo(3)
b = Foo(8)
print(a == b) # False, dont care
print(b.val == a.val) # True
# subclassing possible