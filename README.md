# Figurine

**Simple, structure only models with inheritance**

Figurine is intended for dumb models. In other words, data only, no methods.
For web apps, view models come to mind, or anywhere you would like a model that
does nothing but represent data.

Currently run on Python 2.6+, 3.x will be supported shortly.

**What about namedtuples?**

Yes, you could just use namedtuple for this, and that might even be better.
If you want your model defs to look more like traditional python objects however,
Figurine can help.

It still may be that namedtuples are a better solution, though you may 
need a factory function to start them off with defaults of your choosing.

The base of a figuerine object is a dict, which is a bit better, for my need, for 
JSON serialization if needed, which you could also just do with namedtuple._asdict
if you really wanted to use a namedtuple.


### Using Figurine

```python
import figurine

class FacebookData(figurine.Model):
    def __init__(self):
        self.posts = ['facebook']

class TwitterData(figurine.Model):
    def __init__(self):
            self.tweets = ['twitter']

class SocialData(FacebookData, TwitterData):
    pass

class SimplePage(figurine.Model):
    
    def __init__(self):
        self.title = ""
        self.stylesheets = []
        self.javascript = []
        self.meta = {}
        self.value = 1

class HomePage(SimplePage, SocialData):
    
    def __init__(self):
        self.username = "lucy_the_dog"

model1 = HomePage()
print(model.tweets)
# {'username': 'lucy_the_dog', 'title': '', 'javascript': [], 'posts': ['facebook'], 'value': 1, 'stylesheets': [], 'meta': {}, 'tweets': ['twitter']}

# kwarg overrides or init
model2 = HomePage(title="My Great Title",
                  value=2)

print(model2)
# {'username': 'lucy_the_dog', 'title': 'My Great Title', 'javascript': [], 'posts': ['facebook'], 'value': 2, 'stylesheets': [], 'meta': {}, 'tweets': ['twitter']}
```