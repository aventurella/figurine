

class AttributeDict(dict):
    """
    Lexicon's AttributeDict
    https://github.com/bitprophet/lexicon/blob/master/lexicon/attribute_dict.py
    """

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            # to conform with __getattr__ spec
            raise AttributeError(key)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            object.__setattr__(self, key, value)
        else:
            self[key] = value

    def __delattr__(self, key):
        del self[key]


class FigurineType(type):
    """
    Allow both:

    f = Foo(id=1, name="lucy")

    and

    f = Foo()
    f.id = 1
    f.name = "Lucy"

    BaseModel is the base for all of our models.
    Model def should look simple:

    class Foo(BaseModel):
        def __init__(self):
            self.id = None
            self.name = "Lucy"

    Note, it does not look like we pass **kwargs, that's where
    this MetaClass comes in.

    It basically renames __init__ of the Model to _apply_defaults
    BaseModel's __init__ will then always be called.

    It will call _apply_defaults first in order to set up the default
    values defined in the model.

    It will then, essentially, run a  dict.update() with the kwargs
    to apply the kwargs on top of the defaults.
    """
    # def __new__(cls, name, bases, dct):
    #     dct['__figurine_init__'] = ""
    #     return type.__new__(cls, name, bases, dct)
    
    def __init__(cls, name, bases, dct):
        super(FigurineType, cls).__init__(name, bases, dct)
        
        if AttributeDict in bases:
            return 
        
        def chain(cls):
            def decorator(self):
                print(cls)
                super(cls, self).__figurine_chain__()
                #super(cls, self).__figurine_chain__()
                #print('Init called: ', self)
                #init(self)
                
                #print(init)
                
            return decorator

        def init(cls, init):
            def decorator(self):
                
                print(cls.__mro__)
                #self.__class__.__figurine_chain__(self)
                #init(self)

                
                #getattr(self, '__figurine_init__')()
            return decorator
        cls.__figurine_init__ = init(cls, cls.__init__)
        cls.__figurine_chain__ = cls.__init__
        

        # #print(name, bases)
        del dct['__init__']
        del cls.__init__

    # def __init__(cls, name, bases, dct):
    #     pass
        #o = super(FigurineType, cls).__init__(name, bases, dct)
        #print(cls, cls.__subclasses__())
    #     # don't process anything on the inheritance
    #     # chain at or less than FigurineModel
    #     if AttributeDict in bases:
    #         return
        
    #     # pick up the initializers 
    #     # so we can set their defaults
    #     #defaults = []

    #     # for item in bases:
    #     #     if item is FigurineModel:
    #     #         continue
            
    #         #defaults.append(item.__init__)
    #     #     #del item.__init__

    #     # cls._figurine_defaults = defaults
    #     #cls._figurine_bases = bases
    #     cls.__figurine_init__ = dct['__init__']

    #     del dct['__init__']
    #     del cls.__init__
    #     #print(dir(cls))
    #     #del cls.__init__
    #     super(FigurineType, cls).__init__(name, bases, dct)

class FigurineModel(AttributeDict):

    __metaclass__ = FigurineType

    def __init__(self, *args, **kwargs):
        super(FigurineModel, self).__init__(**kwargs)

        try:
            #print(self.__subclasses__())
            #t = type(self.__class__)
            #print(t.__subclasses__())
            #map(lambda x : x(), self._figurine_defaults)
            #for item in self._figurine_bases:
                #print(item.__init__(self))
            #print('Here', self._figurine_bases)
            # for item in self._figurine_defaults:
            #     print('1', item)
            #print(self._figurine_defaults)
            #print(type(self))
            #print(vars(self))
            
            #self.__figurine_chain__()
            self.__figurine_init__()
            #print(self)
            #print(self.__class__.__figurine_init__)
            #print(dir(self))
            #super(FigurineModel, self).__figurine_init__()
            #self._apply_defaults()
        except AttributeError as e:
            print(e)

        