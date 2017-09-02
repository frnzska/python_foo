# hide object creation
# share common interface
# -> decouples decision of obj from calling obj (decision in one factory not every where in code base)

### simple factory ###

class SomeObj:
    def __init__(self):
        self._val = None

    def get_val(self):
        return self._val

class A(SomeObj):
    def __init__(self, x):
        print('I am A')
        self._val = 1.2 * x

class B(SomeObj):
    def __init__(self, x):
        print('I am B')
        self._val = 1.9 * x

class ObjFactory:

    @staticmethod
    def create_obj( _type, x):
        """ Decide here on concrete type"""
        if _type == 'A':
            return A(x)
        elif _type == 'B':
            return B(x)
        else:
            return None


some_obj = ObjFactory.create_obj('A', 4)

# get lowest val for x=4
subclass_names = map(lambda x: x.__name__, SomeObj.__subclasses__())
lowest_val = min([ObjFactory.create_obj(t, 4).get_val() for t in subclass_names])
print(lowest_val)


