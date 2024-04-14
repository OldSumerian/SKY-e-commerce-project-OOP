
class MixinInfo:

    def __init__(self, *args, **kwargs):
        print(f'создан объект {repr(self)}')

    def __repr__(self):
        return f'{self.__class__.__name__}({", ".join(map(str(self.__dict__.values())))})'

